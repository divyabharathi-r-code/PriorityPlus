import json
import os

def load_biomedical_rules():

    rules_path = os.path.join(
        os.path.dirname(__file__),
        "biomedical_rules.json"
    )

    with open(rules_path, "r") as file:
        return json.load(file)
def check_reference_range(value, rule):

    if not rule.get("enabled"):
        return None

    minimum = rule.get("reference_min")
    maximum = rule.get("reference_max")

    if minimum is None or maximum is None:
        return None

    if value < minimum or value > maximum:

        return {
            "observation": "outside_configured_reference",
            "value": value,
            "unit": rule.get("unit"),
            "severity": "review",
            "source": rule.get("source"),
            "explanation": (
                "The value is outside the configured "
                "reference range."
            )
        }

    return None

def run_biomedical_checks(context):
    rules = load_biomedical_rules()
    reference_checks = []
    
    findings = []
    missing_context = []
    warnings = []

    # -------------------------
    # 1. Missing context checks
    # -------------------------

    if not context["symptoms"]:
        missing_context.append("symptoms")

    if not context["vitals"]:
        missing_context.append("vitals")

    if not context["history"]:
        missing_context.append("medical history")

    if not context["labs"]:
        missing_context.append("lab results")


    # -------------------------
    # 2. Data quality checks
    # -------------------------

    vitals = context["vitals"]
    for field, rule in rules["vitals"].items():

      if field in vitals:

        result = check_reference_range(
            vitals[field],
            rule
        )

        if result:
            result["category"] = "vital"
            result["field"] = field

            reference_checks.append(result)

    if "heart_rate" in vitals:
        if not isinstance(vitals["heart_rate"], (int, float)):
            warnings.append(
                "Heart rate is not a valid numeric value."
            )

    if "spo2" in vitals:
        if not isinstance(vitals["spo2"], (int, float)):
            warnings.append(
                "SpO2 is not a valid numeric value."
            )

    if "temperature" in vitals:
        if not isinstance(vitals["temperature"], (int, float)):
            warnings.append(
                "Temperature is not a valid numeric value."
            )


    # -------------------------
    # 3. Contextual flags
    # -------------------------

    symptoms = context["symptoms"]

    respiratory_terms = [
        "shortness of breath",
        "breathing difficulty",
        "cough"
    ]

    respiratory_context = any(
        symptom in respiratory_terms
        for symptom in symptoms
    )

    if respiratory_context:

        findings.append({
            "category": "context",
            "type": "respiratory_related_information",
            "status": "review"
        })


    # -------------------------
    # 4. Calculate review level
    # -------------------------

    if warnings:
        priority = "REVIEW"

    elif findings:
        priority = "REVIEW"

    elif missing_context:
        priority = "INCOMPLETE CONTEXT"

    else:
        priority = "NO FLAGS"
        # -------------------------
    # 5. Explanation
    # -------------------------

    if findings:
        why_it_matters = (
            "Related patient information has been identified "
            "and should be reviewed together with the available context."
        )

    elif missing_context:
        why_it_matters = (
            "Some relevant patient information is missing, "
            "which may limit contextual review."
        )

    else:
        why_it_matters = (
            "No contextual review flags were identified "
            "from the currently available information."
        )


    # -------------------------
    # 6. Next-step support
    # -------------------------

    if missing_context:

        next_step = (
            "Review the missing information and obtain relevant "
            "additional context where appropriate."
        )

    elif findings:

        next_step = (
            "Review the identified findings together with the "
            "available patient context."
        )

    else:

        next_step = (
            "Continue with routine information review "
            "using the available context."
        )


    return {
        "findings": findings,
        "missing_context": missing_context,
        "warnings": warnings,
        "reference_checks": reference_checks,
        "priority": priority,
        "why_it_matters": why_it_matters,
        "next_step": next_step
        
    }