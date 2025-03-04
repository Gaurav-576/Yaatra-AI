import time
import streamlit as st
from data.destination_data_extractor import WikiVoyageScraper
from src.chromaDB.chroma_chunks import UploadData
from src.RAG_chains.itinerary_chain import ItineraryRAG
from utils.download_trip import PDFDownloader

def main():
    st.set_page_config(page_title="Yaatra AI - Trip Planner", layout="centered")
    user_details = {}
    
    st.title("🌍 Yaatra AI - Your Personalized Trip Planner")

    if "step" not in st.session_state:
        st.session_state.step = 1
    if "trip_generated" not in st.session_state:
        st.session_state.trip_generated = False
    if "loading" not in st.session_state:
        st.session_state.loading = False

    if not st.session_state.trip_generated:
        progress_value = (st.session_state.step - 1) / 5
        st.progress(progress_value)

    if st.session_state.trip_generated:
        user_details["destination"] = st.session_state.destination
        user_details["travel_date"] = st.session_state.travel_date
        user_details["duration"] = st.session_state.duration
        user_details["budget"] = st.session_state.budget
        user_details["trip_type"] = st.session_state.trip_type
        user_details["transport_mode"] = st.session_state.transport_mode
        user_details["interests"] = st.session_state.activities

        destination_data_extractor = WikiVoyageScraper()
        destination_data = destination_data_extractor.extract_travel_info(st.session_state.destination)
        
        data_uploader = UploadData()
        vector_store = data_uploader.chroma_store().as_retriever()
        
        ai_itinerary_generator = ItineraryRAG(user_details)
        ai_response = ai_itinerary_generator.generate_itinerary_suggestions()

        st.title("🗺️ Your AI-Powered Trip Plan")
        st.success(f"✅ Your {user_details["duration"]}-day trip to {user_details["destination"]} is ready! 🎉")

        # Destination & Date
        st.subheader("📍 Destination & Travel Date")
        st.write(f"**{user_details["destination"]}** on **{user_details["travel_date"]}**")

        # Duration & Budget
        st.subheader("📅 Duration & Budget")
        st.write(f"🕒 Duration: {user_details["duration"]} days")
        st.write(f"💰 Budget: ₹{user_details["budget"]}")

        # Transport & Trip Type
        st.subheader("🚀 Travel Details")
        st.write(f"🛫 Mode of Transport: {user_details["transport_mode"]}")
        st.write(f"👥 Trip Type: {user_details["trip_type"]}")

        # Activities
        st.subheader("🎭 Activities Selected")
        st.write("✅ " + ", ".join(user_details["interests"]) if user_details["interests"] else "No specific activities selected.")

        # AI-Generated Itinerary
        st.subheader("📋 AI-Generated Itinerary")
        st.write(ai_response)
        
        pdf_downloader = PDFDownloader(user_details, ai_response)
        pdf_downloader.download_pdf_button()

        if st.button("🔄 Plan Another Trip", key="restart", use_container_width=True, type="primary"):
            st.session_state.clear()
            st.rerun()

    else:
        container = st.container()
        with container:
            st.markdown('<div class="swipe-right">', unsafe_allow_html=True)
            if st.session_state.step == 1:
                st.header("Step 1: Choose Your Destination")
                destination = st.text_input("Where do you want to go?", value=st.session_state.get("destination", ""))
                travel_date = st.date_input("Select your travel date", value=st.session_state.get("travel_date", None))
                col1, col2 = st.columns([9, 1])
                with col2:
                    if st.button("Next", key="next1", use_container_width=True, type="primary"):
                        if destination and travel_date:
                            st.session_state.destination = destination
                            st.session_state.travel_date = travel_date
                            st.session_state.step = 2
                            st.rerun()
            elif st.session_state.step == 2:
                st.header("Step 2: Travel Details")
                duration = st.number_input("How many days will you travel?", min_value=1, step=1, value=st.session_state.get("duration", 1))
                budget = st.number_input("What is your budget (in INR)?", min_value=10000, step=500, value=st.session_state.get("budget", 10000))

                col1, col2 = st.columns([9, 1])
                with col1:
                    if st.button("Previous", key="prev2"):
                        st.session_state.step = 1
                        st.rerun()
                with col2:
                    if st.button("Next", key="next2", use_container_width=True, type="primary"):
                        st.session_state.duration = duration
                        st.session_state.budget = budget
                        st.session_state.step = 3
                        st.rerun()

            elif st.session_state.step == 3:
                st.header("Step 3: Select Trip Type")
                trip_types = {
                    "Solo": "🧍 Solo",
                    "Friends": "🧑‍🤝‍🧑 Friends",
                    "Family": "👨‍👩‍👧‍👦 Family",
                    "Couple": "💑 Couple",
                    "Business": "💼 Business"
                }

                st.subheader("Select Your Trip Type")
                cols = st.columns(5)
                for i, (trip, label) in enumerate(trip_types.items()):
                    with cols[i]:
                        if st.button(label, key=f"trip_{trip}", use_container_width=True):
                            st.session_state.trip_type = trip
                            st.session_state.step = 4
                            st.rerun()

            elif st.session_state.step == 4:
                st.header("Step 4: Choose Transport Mode")
                transport_modes = {
                    "Flight": "✈️ Flight",
                    "Train": "🚆 Train",
                    "Bus": "🚌 Bus",
                    "Car": "🚗 Car"
                }

                st.subheader("Select Mode of Transport")
                cols = st.columns(4)
                for i, (mode, label) in enumerate(transport_modes.items()):
                    with cols[i]:
                        if st.button(label, key=f"transport_{mode}", use_container_width=True):
                            st.session_state.transport_mode = mode
                            st.session_state.step = 5
                            st.rerun()

            elif st.session_state.step == 5:
                st.header("Step 5: Select Activities")
                activities = {
                    "Popular Attractions": "🏰 Popular Attractions",
                    "Important Places": "📍 Important Places",
                    "Food and Cuisine": "🍽️ Food and Cuisine",
                    "Historical Sites": "🏛️ Historical Sites",
                    "Religious Sites": "⛪ Religious Sites"
                }

                st.subheader("Choose Activities")
                selected_activities = []
                for activity, label in activities.items():
                    if st.checkbox(label, key=f"activity_{activity}"):
                        selected_activities.append(activity)

                col1, col2 = st.columns([9, 1])
                with col2:
                    if st.button("Generate", key="generate", use_container_width=False, type="primary"):
                        st.session_state.activities = selected_activities
                        st.session_state.loading = False
                        st.session_state.step = 6
                        st.rerun()
            
            elif st.session_state.step == 6:
                st.header("Generating Your Trip Plan")
                st.write("Please wait while we generate your personalized trip plan...")
                time.sleep(5)
                st.session_state.trip_generated = True
                st.session_state.loading = False
                st.rerun()

if __name__ == "__main__":
    main()
