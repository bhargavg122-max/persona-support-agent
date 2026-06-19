def create_handoff_summary(
    query,
    persona,
    response
):

    return f"""
ESCALATION SUMMARY

Customer Persona:
{persona}

Customer Query:
{query}

AI Response:
{response}
"""