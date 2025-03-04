import os
import sys
import shutil
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_ollama import OllamaEmbeddings
from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores import Chroma

class UploadData:    
    def __init__(self, data_file="../../data/destination_data.txt", persist_dir="./chroma_db"):
        self.file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), data_file))
        self.persist_dir = persist_dir
        self.collection_name = "destination_info"
        self.embedding_model = "nomic-embed-text"
    
    def clear_chroma_db(self):
        if os.path.exists(self.persist_dir):
            shutil.rmtree(self.persist_dir)
    
    def chroma_store(self):
        # self.clear_chroma_db()
        
        loader = TextLoader(self.file_path, encoding="utf-8")
        text_loader = loader.load()

        text_splitter = RecursiveCharacterTextSplitter(chunk_size=512, chunk_overlap=0)
        chunks = text_splitter.split_documents(text_loader)

        vector_store = Chroma.from_documents(
            documents=chunks,
            persist_directory=self.persist_dir,
            collection_name=self.collection_name,
            embedding=OllamaEmbeddings(model=self.embedding_model),
        )
        return vector_store