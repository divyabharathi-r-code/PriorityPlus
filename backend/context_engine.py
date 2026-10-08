def build_context(patient):

    context = {
        "demographics": {},
        "symptoms": [],
        "vitals": {},
        "history": [],
        "labs": {},
        "missing_context": []
    }

    # Age
    if patient.get("age") is not None:
        context["demographics"]["age"] = patient["age"]
    else:
        context["missing_context"].append("age")

    # Symptoms
    symptoms = patient.get("symptoms", [])

    if symptoms:
        context["symptoms"] = [
            symptom.strip().lower()
            for symptom in symptoms
        ]
    else:
        context["missing_context"].append("symptoms")

    # Vitals
    vitals = patient.get("vitals", {})

    if vitals:
        context["vitals"] = vitals
    else:
        context["missing_context"].append("vitals")

    # Medical history
    history = patient.get("history", [])

    if history:
        context["history"] = [
            item.strip().lower()
            for item in history
        ]
    else:
        context["missing_context"].append("medical history")

    # Lab results
    labs = patient.get("labs", {})

    if labs:
        context["labs"] = labs
    else:
        context["missing_context"].append("lab results")

    return context