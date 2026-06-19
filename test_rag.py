from src.rag import build_vector_store

vector_store = build_vector_store()

query = input("Ask a question: ")

results = vector_store.similarity_search(query, k=3)

print("\nRetrieved Chunks:\n")

for doc in results:
    print(doc.page_content)
    print("-" * 50)