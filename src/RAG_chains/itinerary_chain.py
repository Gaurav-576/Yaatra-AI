import re
from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

import os
import sys
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))
sys.path.append(PROJECT_ROOT)
from src.chromaDB.chroma_chunks import UploadData

class ItineraryRAG:
    def __init__(self, user_details):
        self.user_details = user_details
        uploaded_data = UploadData()
        self.vector_store = uploaded_data.chroma_store().as_retriever()
        self.ai_model = ChatOllama(model="deepseek-r1:1.5b")
        self.itinerary_details = {}

    def generate_itinerary_suggestions(self):
        itinerary_prompt = """
        You are an expert travel planner. Based on the following destination details, generate a detailed {duration}-day itinerary for a trip to {destination}.

        Destination Details: {trip_details}
        
        Your task:
        Preferred Activities: Suggest activities based on the given interests.
        Balance: Ensure a mix of sightseeing, adventure, relaxation, and local experiences.
        Food & Culture: Recommend local cuisine options and cultural experiences.

        Format the response in a structured manner, separating each day's itinerary clearly.
        Question: {question}
        """
        
        interest_docs = []
        itinerary_template = ChatPromptTemplate.from_template(template=itinerary_prompt)
        for interest in self.user_details["interests"]:
            retrieved_docs = self.vector_store.invoke(interest)
            interest_docs.extend(retrieved_docs)
            
        trip_details = []
        for doc in interest_docs:
            trip_details.append(doc.page_content)
        rag_chain = (
            {
                "duration": lambda x: str(self.user_details["duration"]),
                "destination": lambda y: str(self.user_details["destination"]),
                "trip_details": lambda z: trip_details,
                "question": RunnablePassthrough()
                
            }
            | itinerary_template
            | self.ai_model
            | StrOutputParser()
        )
        response = rag_chain.invoke({"question": "Based on the given interests, suggest a detailed itinerary for a trip to Goa."})
        cleaned_response = re.sub(r"<think>.*?</think>", "", response, flags=re.DOTALL).strip()
        return cleaned_response