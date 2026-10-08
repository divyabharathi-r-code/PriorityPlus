
import json
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

MODEL = os.getenv("GROQ_MODEL")


def generate_reasoning(context, checks):

    prompt = f"""
You are the AI reasoning component of Priority+,
a biomedical information-context and prioritization prototype.

Your job is to explain the structured information provided
by the system.

Do NOT diagnose a disease.
Do NOT prescribe treatment.
Do NOT invent medical facts or missing patient information.

Focus on:
1. What information was identified.
2. What contextual findings were detected.
3. What information is missing.
4. Why the identified information may deserve professional review.
5. What should be reviewed next.

Patient context:
{context}

Biomedical checks:
{checks}

Return ONLY valid JSON in exactly this structure:

{{
  "summary": "",
  "identified": "",
  "contextual_findings": "",
  "missing_information": "",
  "why_review_matters": "",
  "next_steps": ""
}}

Rules:
- Return valid JSON only.
- Do not use Markdown.
- Do not use tables.
- Do not use asterisks or bullet symbols.
- Keep each field concise.
- Do not diagnose diseases.
- Do not prescribe treatment or medication.
- Do not invent patient information.
- Base the response only on the provided context and biomedical checks.
- Focus on professional review support.
IMPORTANT:
Do not classify any laboratory or vital-sign value as normal,
abnormal, elevated, reduced, mild, severe, tachycardic, hypoxic,
or any other clinical category unless that classification is
explicitly provided by the biomedical checks.

When a value is provided without a configured reference check,
describe the value exactly as given.

For example:
CRP: 5

Do not write:
"mild CRP elevation"

Instead write:
"CRP was reported as 5."
"""

    response = client.responses.create(
        model=MODEL,
        input=prompt
    )

    return json.loads(response.output_text)

if __name__ == "__main__":

    test_context = {
        "demographics": {
            "age": 45
        },
        "symptoms": [
            "fever",
            "shortness of breath"
        ],
        "vitals": {
            "heart_rate": 105,
            "spo2": 92,
            "temperature": 38.5
        },
        "history": [
            "asthma"
        ],
        "labs": {},
        "missing_context": [
            "lab results"
        ]
    }

    test_checks = {
        "findings": [
            {
                "category": "context",
                "type": "respiratory_related_information",
                "status": "review"
            }
        ],
        "missing_context": [
            "lab results"
        ],
        "warnings": [],
        "reference_checks": [],
        "priority": "REVIEW"
    }

    result = generate_reasoning(
        test_context,
        test_checks
    )

    print("\n--- PRIORITY+ AI REASONING ---\n")
    print(result)