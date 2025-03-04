# import os
# from utils.trip_data import TripPlanner
# from data.destination_data_extractor import WikiVoyageScraper
# from langchain_core.prompts import ChatPromptTemplate
# from langchain_core.runnables import RunnablePassthrough
# from langchain_core.messages import AIMessage, HumanMessage
# from langchain_huggingface import HuggingFaceEndpoint
# from dotenv import load_dotenv
# load_dotenv()

# from transformers import AutoTokenizer, AutoModelForCausalLM
# tokenizer = AutoTokenizer.from_pretrained("deepseek-ai/DeepSeek-R1-Distill-Llama-70B")
# model = AutoModelForCausalLM.from_pretrained("deepseek-ai/DeepSeek-R1-Distill-Llama-70B")

# def generate_response(prompt):
#     inputs = tokenizer(prompt, return_tensors="pt")
#     with torch.no_grad():
#         outputs = model.generate(inputs, max_length=200)
#     return tokenizer.decode(outputs[0], skip_special_tokens=True)

# class YatraRAG:
#     def __init__(self):
#         self.user_data = {
#             "destination": "Darjeeling",
#             "travel_date": "2025-03-02",
#             "duration": 4,
#             "budget": 10000,
#             "trip_type": "solo",
#             "transport_mode": "train",
#             "interests": ["popular attractions", "food"]
#         }
#         self.destination_data = WikiVoyageScraper().extract_travel_info("Darjeeling") #self.user_data["destination"])
        
#         self.transport_details = None
#         self.accommodation_details = None
#         self.itinerary_details = None
#         self.total_cost = 0

#         def generate_transport_details_chain(self):
#             transportation_template = """You are an AI travel assistant responsible for analyzing transportation options for a user's trip.  
#                 You will be given a list of transportation choices, including details such as:  

#                 Mode of transport (bus, train, flight, taxi, etc.)  
#                 Travel time  
#                 Pricing (if available)  

#                 You are an AI travel assistant responsible for analyzing and recommending the best transportation option for a user's trip 
#                 based on affordability, comfort, and travel duration. Extract and categorize all available transport modes, 
#                 filtering options that fit within 10-15% of the total budget. If no option is available within this range, 
#                 suggest the closest viable alternative while avoiding significantly over-budget choices unless necessary.
#                 Calculate the round-trip cost, ensuring it remains within budget. Compare filtered choices based on cost-effectiveness, 
#                 travel duration, and comfort, prioritizing faster and more convenient options. Provide the final recommendation with its cost 
#                 and a brief justification aligned with the user's preferences.

#                 Trip Details:  
#                 Departure Location: {location}  
#                 Destination: {destination}  
#                 Total Budget: ₹{budget}  
#                 Preferred Transport Mode (if any): {transport_mode}  
#                 Available Transport Options: {transport_details}  

#                 Response Format:
#                 ```json
#                 {
#                 "mode": "<Best Transport Option>",
#                 "details": {
#                     "<Transport Type>": {
#                     "name": "<Option Name>",
#                     "cost": <One-way Cost>,
#                     "duration": "<Travel Time>"
#                     }
#                 },
#                 "total_cost": <Round-trip Cost>,
#                 "total_duration": "<Total Travel Time>",
#                 "reason": "<Brief Justification>"
#             """

#         transport_details_prompt = ChatPromptTemplate.from_template(template=transportation_template)
#         llm_engine = ChatOllama
    
#     # def generate_accommodation_details(self):
#     #     prompt = (f"Suggest an accommodation for a {self.trip_type} trip to {self.destination} "
#     #               f"for {self.duration} days within a budget of {self.budget}. "
#     #               f"Use the following data: {self.destination_data}")
#     #     response = generate_response(prompt)
#     #     cost_per_night = random.randint(1000, 5000)  # Simulated cost
#     #     total_cost = cost_per_night * self.duration
#     #     self.accommodation_details = {"hotel": response, "cost": total_cost}
#     #     return self.accommodation_details
    
#     # def generate_itinerary_details(self):
#     #     prompt = (f"Generate a {self.duration}-day itinerary for a {self.trip_type} trip to "
#     #               f"{self.destination} including activities based on interests: {', '.join(self.interests)}. "
#     #               f"Use the following data: {self.destination_data}")
#     #     response = generate_response(prompt)
#     #     activity_cost = random.randint(500, 3000) * self.duration  # Simulated cost
#     #     self.itinerary_details = {"plan": response, "cost": activity_cost}
#     #     return self.itinerary_details
    
#     def cost_optimization(self):
#         self.total_cost = (
#             self.transport_details["cost"] +
#             self.accommodation_details["cost"] +
#             self.itinerary_details["cost"]
#         )
        
#         if self.total_cost > self.budget:
#             max_allowed_budget = self.budget * 1.25  # Allow 25% increase
#             if self.total_cost <= max_allowed_budget:
#                 return f"Total cost exceeds budget but is within the 25% allowance: {self.total_cost}"
#             else:
#                 return "Trip not feasible within budget, even with 25% increase. Consider adjusting preferences."
#         return f"Trip successfully planned within budget: {self.total_cost}"
    
#     def generate_trip_plan(self):
#         self.generate_transport_details()
#         self.generate_accommodation_details()
#         self.generate_itinerary_details()
#         return self.cost_optimization()

# # Example Usage
# if __name__ == "__main__":
#     planner = YatraRAG()
#     print(planner.show_data())