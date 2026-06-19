import streamlit as st

from src.persona_detector import detect_persona
from src.rag import retrieve_documents
from src.response_generator import generate_response
from src.escalation import should_escalate
from src.handoff import create_handoff_summary

st.title("Persona-Aware Customer Support Agent")

query = st.text_area("Enter customer query")

if st.button("Submit"):
    persona = detect_persona(query)
    context = retrieve_documents(query)

    response = generate_response(
        query=query,
        persona=persona,
        context=context,
    )

    st.subheader("Detected Persona")
    st.write(persona)

    st.subheader("AI Response")
    st.write(response)

    if should_escalate(query):
        st.warning("Escalation Required")

        summary = create_handoff_summary(
            query=query,
            persona=persona,
            response=response,
        )

        st.subheader("Handoff Summary")
        st.write(summary)