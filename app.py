from src.persona_detector import detect_persona
from src.rag import retrieve_documents
from src.response_generator import generate_response
from src.escalation import should_escalate
from src.handoff import create_handoff_summary


def main():

    query = input("Customer Query: ")

    persona = detect_persona(query)

    context = retrieve_documents(query)

    response = generate_response(
        query=query,
        persona=persona,
        context=context
    )

    print("\n=== AI RESPONSE ===")
    print(response)

    if should_escalate(query):

        print("\n=== ESCALATION REQUIRED ===")

        summary = create_handoff_summary(
            query=query,
            persona=persona,
            response=response
        )

        print(summary)


if __name__ == "__main__":
    main()