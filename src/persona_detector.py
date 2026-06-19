def detect_persona(user_message):
    message = user_message.lower()

    technical_keywords = [
        "api",
        "authentication",
        "token",
        "configuration",
        "logs",
        "error",
        "endpoint",
        "debug",
        "server"
    ]

    frustrated_keywords = [
        "frustrated",
        "angry",
        "nothing works",
        "terrible",
        "worst",
        "urgent",
        "tried everything"
    ]

    executive_keywords = [
        "business impact",
        "operations",
        "revenue",
        "deadline",
        "client",
        "timeline",
        "resolution"
    ]

    if any(word in message for word in technical_keywords):
        return "Technical Expert"

    if any(word in message for word in frustrated_keywords):
        return "Frustrated User"

    if any(word in message for word in executive_keywords):
        return "Business Executive"

    return "Business Executive"