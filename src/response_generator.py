import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel("gemini-3.5-flash")


def generate_response(query, persona, context):

    prompt = f"""
You are a customer support assistant.

Customer Persona:
{persona}

Knowledge Base Context:
{context}

Customer Question:
{query}

Provide a helpful response.
"""

    response = model.generate_content(prompt)

    return response.text

