# Persona-Aware Customer Support Agent

## Overview

This project is an AI-powered customer support assistant that combines:

* Persona Detection
* Retrieval-Augmented Generation (RAG)
* Gemini LLM Response Generation
* Human Escalation Workflow

The system identifies customer personas, retrieves relevant information from a knowledge base, generates contextual responses, and escalates sensitive issues to human support agents when required.

---

## Features

### Persona Detection

Detects customer types:

* Technical Expert
* Frustrated User
* Business Executive

### Retrieval-Augmented Generation (RAG)

Retrieves relevant information from internal documentation using:

* LangChain
* FAISS Vector Database
* HuggingFace Embeddings

### AI Response Generation

Generates contextual responses using:

* Google Gemini 3.5 Flash

### Human Escalation

Automatically escalates sensitive requests such as:

* Refund requests
* Billing issues
* Legal concerns
* Human assistance requests

### Handoff Summary

Creates a concise summary for support agents containing:

* Customer persona
* Customer query
* AI-generated response

---

## Project Structure

persona-support-agent/

├── app.py

├── docs/

│ ├── password_reset.md

│ ├── api_authentication.md

│ └── billing_policy.md

├── src/

│ ├── persona_detector.py

│ ├── rag.py

│ ├── response_generator.py

│ ├── escalation.py

│ └── handoff.py

└── .env

---

## Technologies Used

* Python
* Google Gemini 3.5 Flash
* LangChain
* FAISS
* HuggingFace Embeddings
* python-dotenv

---

## Installation

### Clone Repository

git clone <repository-url>

cd persona-support-agent

### Create Virtual Environment

python -m venv venv

### Activate Environment

Windows:

venv\Scripts\activate

### Install Dependencies

pip install -r requirements.txt

### Configure Environment Variables

Create a .env file:

GEMINI_API_KEY=your_api_key_here

---

## Run Application

python app.py

---

## Sample Queries

Password Reset:

I forgot my password

Technical Support:

My API token is expired and authentication is failing

Refund Escalation:

I want a refund for my subscription

---

## Expected Workflow

1. Detect customer persona
2. Retrieve relevant knowledge-base documents
3. Generate AI response using Gemini
4. Check escalation requirements
5. Generate handoff summary if escalation is needed

---

## Author

Bhargav Gudikandula
