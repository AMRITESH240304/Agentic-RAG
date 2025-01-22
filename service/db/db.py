from pymongo import MongoClient
from config import settings
from langchain_mongodb import MongoDBAtlasVectorSearch
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain.schema import Document

def save_to_mongo(text):
    
    doc = Document(page_content=text)
    
    # If you have multiple texts, create a list of Document objects
    docs = [doc]
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=20)
    splits = text_splitter.split_documents(docs)
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001",google_api_key=settings.GEMINI_API_KEY)
    
    # store = [] 

    # for split in splits:
    #     store.append(split.page_content)
        
    client = MongoClient(settings.MONGO_URI)
    collection = client['mongoVector']['testvector']
    collection.delete_many({})
    
    MongoDBAtlasVectorSearch.from_documents(
    splits, embeddings, collection=collection, index_name="vectorSearch"
    )
    
    return "done"