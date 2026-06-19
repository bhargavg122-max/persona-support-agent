def should_escalate(query):

    escalation_keywords = [
        "refund",
        "billing issue",
        "legal",
        "manager",
        "complaint",
        "human",
        "urgent"
    ]

    query = query.lower()

    return any(
        keyword in query
        for keyword in escalation_keywords
    )

