from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings


def build_vector_store():
    loader = DirectoryLoader(
        "docs",
        glob="**/*.md",
        loader_cls=TextLoader
    )

    documents = loader.load()

    print("Documents Loaded:", len(documents))

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )

    chunks = splitter.split_documents(documents)

    print("Chunks Created:", len(chunks))

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    vector_store = FAISS.from_documents(
        chunks,
        embeddings
    )

    return vector_store


def retrieve_documents(query):
    vector_store = build_vector_store()

    results = vector_store.similarity_search(
        query,
        k=3
    )

    context = "\n".join(
        [doc.page_content for doc in results]
    )

    return context


