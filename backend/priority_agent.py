from context_engine import build_context
from biomedical_checks import run_biomedical_checks
from ai_reasoning import generate_reasoning


def run_priority_agent(patient):

    # Stage 1: Build patient context
    context = build_context(patient)

    # Stage 2: Run biomedical checks
    checks = run_biomedical_checks(context)

    # Stage 3: Generate AI reasoning
    reasoning = generate_reasoning(
        context,
        checks
    )

    # Stage 4: Combine everything
    return {
        "context": context,
        "biomedical_checks": checks,
        "ai_reasoning": reasoning
    }