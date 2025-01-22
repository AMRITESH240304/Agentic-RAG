from pymongo import MongoClient
from langchain_mongodb import MongoDBAtlasVectorSearch
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from config import settings

def get_docs(query: str):
    client = None
    try:
        print(query)
        embeddings = GoogleGenerativeAIEmbeddings(
            model="models/embedding-001", 
            google_api_key=settings.GEMINI_API_KEY
        )
        client = MongoClient(settings.MONGO_URI)
        collection = client['mongoVector']['testvector']
        vectorStore = MongoDBAtlasVectorSearch(collection, embeddings, index_name="vector_index")
        docs = vectorStore.similarity_search(query)
        # print("Vector Search Results:")
        # print(len(docs))
        # print(docs[0])
        return docs[0]
    except Exception as e:
        print("Database timeout or error:", str(e))
        return []
    finally:
        if client:
            client.close()

from crewai.tools import tool
@tool("vector search")
def my_secret_code_tool(input_text: str) -> str:
    """
    This tool is used for generating secret codes for a given text
    the input should be a str

    :param input_text: str, input text for which to retrieve secret code
    """
    # print(input_text)
    return get_docs(input_text)
