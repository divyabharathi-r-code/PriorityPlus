# 🧠 Priority+

### AI-Assisted Healthcare Context & Review Support

Priority+ is a biomedical decision-support prototype designed to organize healthcare information from multiple sources, identify missing context, prioritize information that may require review, and provide structured AI-assisted reasoning.

Instead of focusing only on prediction, Priority+ focuses on **understanding context and deciding what information deserves attention next**.

> ⚠️ **Disclaimer:** Priority+ is a prototype for healthcare information organization and professional review support. It is not a diagnostic system and does not prescribe treatment.

---

## 🚀 Overview

Healthcare information can be scattered across symptoms, vital signs, medical history, and laboratory results.

When some information is missing or difficult to interpret together, important context may be overlooked.

Priority+ addresses this through a structured workflow:

```text
Patient Information
        ↓
   Context Engine
        ↓
 Biomedical Checks
        ↓
  Priority Decision
        ↓
   AI Reasoning
        ↓
 Structured Dashboard
```
## Problem
### Healthcare information may contain:
- Symptoms
- Vital signs
- Medical history
- Laboratory results
- Missing information
- Multiple pieces of context that need to be considered together
A general-purpose AI assistant can analyze this information when prompted, but Priority+ is designed around a structured biomedical workflow.
The goal is to help organize the available information and highlight what may deserve professional review.
---
## 💡 Solution
### Priority+ processes healthcare information through multiple stages.
### 1. Context Engine
The Context Engine organizes patient information into structured categories:
- Demographics
- Symptoms
- Vitals
- Medical history
- Laboratory results
- Missing context
It identifies which important information has not been provided.
### 2. Biomedical Checks
The Biomedical Checks layer examines the structured information and applies configured biomedical rules.
It can identify:
- Contextual findings
- Data-quality warnings
- Configured reference-range findings
- Missing information
Biomedical reference rules are kept separate from the AI reasoning layer so that the AI does not independently invent clinical thresholds.
### 3. Priority Decision
The Priority Agent determines the review state based on the structured checks.
Possible states include:
REVIEW
INCOMPLETE CONTEXT
NO FLAGS

This creates a deterministic layer between raw patient information and AI reasoning.

### 4. AI Reasoning
Groq-powered AI reasoning receives the structured context and biomedical checks.
The AI generates a structured explanation covering:
- Summary
- What was identified
- Contextual findings
- Missing information
- Why review may matter
- Next steps for professional review
The AI is instructed not to diagnose conditions or prescribe treatment.
---
## Architecture
```
                    ┌──────────────────────┐
                    │   Patient Dashboard  │
                    │   HTML / CSS / JS     │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │      FastAPI         │
                    │      Backend         │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │    Context Engine    │
                    │                      │
                    │ Symptoms              │
                    │ Vitals                │
                    │ History               │
                    │ Labs                  │
                    │ Missing Context       │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │  Biomedical Checks   │
                    │                      │
                    │ Findings              │
                    │ Warnings              │
                    │ Reference Checks      │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │   Priority Agent     │
                    │                      │
                    │ REVIEW                │
                    │ INCOMPLETE CONTEXT    │
                    │ NO FLAGS              │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │    AI Reasoning      │
                    │       Groq           │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │   Priority+ Output   │
                    │                      │
                    │ Priority              │
                    │ Findings              │
                    │ Missing Context       │
                    │ Why It Matters        │
                    │ Next-Step Support     │
                    │ AI Reasoning          │
                    └──────────────────────┘
```
----
## ✨ Features
### Patient Context
Priority+ accepts:
- Age
- Symptoms
- Heart rate
- SpO₂
- Temperature
- Medical history
- Laboratory results
---
## 🔎 Context Awareness
The system detects missing information and reports it separately.
Example:
Missing Context

• Lab results

When laboratory information is provided:
No missing context detected.

---
## 🧪 Biomedical Reference Checks
Priority+ supports configurable biomedical reference rules.
The rules are stored separately in:
backend/biomedical_rules.json

This allows verified biomedical reference information to be added without hard-coding it into the AI layer.

---
## 🧠 Structured AI Reasoning
### The AI output is organized into:
Summary
What was identified
Contextual findings
Missing information
Why review matters
Next steps

This makes the output easier to review than an unstructured chatbot response.

---
##  Data Quality
Priority+ also checks the structure and validity of submitted information and can report data-quality warnings separately from biomedical findings.

---
## Dashboard
### The Priority+ dashboard provides separate sections for:
- Patient Information
- Patient Context
- Priority
- Key Findings
- Missing Context
- Data Quality
- Biomedical Reference Checks
- Why It Matters
- Next-Step Support
- AI Reasoning
---
## Tech Stack
### Frontend
- HTML
- CSS
- JavaScript
### Backend
- Python
- FastAPI
- Uvicorn
## AI
- Groq API
- OpenAI-compatible Python SDK
- python-dotenv
### Biomedical Processing
- Python-based Context Engine
- Configurable JSON biomedical rules
- Deterministic biomedical checks
- Priority decision layer.
---
## 📁 Project Structure
```
PriorityPlus/
│
├── backend/
│   ├── ai_reasoning.py
│   ├── biomedical_checks.py
│   ├── biomedical_rules.json
│   ├── context_engine.py
│   ├── main.py
│   └── priority_agent.py
│
├── frontend/
│   └── index.html
│
├── .gitignore
│
└── README.md
```
---
## 🔄 Example Workflow
### Example patient information:
Age: 45

Symptoms:
fever
shortness of breath

Vitals:
Heart Rate: 105
SpO₂: 92
Temperature: 38.5

Medical History:
asthma

Laboratory Results:
Hemoglobin: 13.2
WBC: 8.5
CRP: 5

Priority+ organizes the information and produces a structured review-support output.
The system does not independently diagnose the patient.

---
## 🧠 Why Priority+?
General-purpose AI assistants can analyze healthcare information when prompted.
Priority+ takes a different approach:
Healthcare Data
      ↓
Structured Context
      ↓
Missing Context Detection
      ↓
Biomedical Checks
      ↓
Priority Decision
      ↓
AI Reasoning
      ↓
Explainable Review Support

The LLM is therefore one component of the workflow rather than the entire system.

---
## 🌟 Key Differentiators
### Context-first approach
Instead of immediately generating an answer, Priority+ first organizes the available information.
### Missing-context detection
The system explicitly identifies information that has not been provided.
### Structured biomedical layer
Biomedical checks are separated from AI reasoning.
### Explainable output
The dashboard shows:
- What was identified
- What is missing
- Why it may matter
- What should be reviewed next
### Human-in-the-loop design
Priority+ is designed to support professional review rather than replace healthcare professionals.

---
## Future Scope
### Future versions of Priority+ can explore:
- Long-term health trend analysis
- Longitudinal patient context
- Retrieval-Augmented Generation (RAG) using validated biomedical knowledge
- Specialized AI agents for different healthcare workflows
- Human-in-the-loop validation
- Integration with professional healthcare workflows
- More configurable biomedical reference rules
- Additional biomedical data sources

---
## Current Prototype Status
### Version 5
```
-✅ Context Engine
-✅ FastAPI Backend
-✅ Biomedical Checks
-✅ Missing Context Detection
-✅ Priority Agent
-✅ Groq AI Reasoning
-✅ Patient Vitals
-✅ Medical History
-✅ Laboratory Results
-✅ Structured Dashboard
-✅ Data Quality Checks
-✅ Configurable Biomedical Rules
```

---
## 🔐 Security
API credentials are stored locally in:
backend/.env

The .env file is excluded from version control using .gitignore.
The Groq API key is never exposed to the frontend.
AI requests are handled by the backend.

-----

## ⚠️ Disclaimer
```
-Priority+ is an experimental prototype developed for educational, research, and hackathon purposes.
-It is intended to organize healthcare information and provide AI-assisted professional review support.
-It should not be used as a substitute for medical professionals, clinical judgment, diagnosis, or treatment decisions.
-The biomedical reference rules used by the prototype should be independently verified before any real-world or clinical use.
```

------
