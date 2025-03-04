# Yaatra AI: AI-Powered Trip Planner

Yaatra AI is an advanced AI-powered trip planner that leverages cutting-edge technologies to generate personalized travel itineraries. At its core, it utilizes **DeepSeek-R1:1.5B**, an **Ollama-based model**, renowned for its advanced reasoning capabilities, ensuring well-thought-out and optimized travel plans. 

## 🧠 AI and Technical Backbone

### **DeepSeek-R1:1.5B for Intelligent Planning**
DeepSeek-R1:1.5B is pivotal to Yaatra AI, as it enables deep contextual understanding and decision-making. Unlike traditional models, DeepSeek's advanced logical reasoning allows it to analyze multiple travel factors, optimize costs, and tailor recommendations based on user preferences.

### **ChromaDB for Efficient Retrieval**
Yaatra AI stores and retrieves travel data using **ChromaDB**, a high-performance vector database. This ensures quick and relevant access to travel information, enabling the AI to provide recommendations that align with user preferences.

### **Multi-Chain RAG Architecture**
By implementing **multi-chain Retrieval-Augmented Generation (RAG)**, Yaatra AI dynamically fetches and generates trip plans based on real-time user input, ensuring personalized and optimized itineraries.

Together, these technologies power an intelligent, AI-driven travel assistant that simplifies trip planning with **highly optimized and context-aware recommendations**.

## 🚀 Features

- **Multi-step user input process** to generate a trip plan dynamically.
- **AI-generated trip itinerary** using Llama models from ChatGroq.
- **ChromaDB for efficient data retrieval** and semantic search.
- **Multi-chain RAG architecture** for modular trip generation.
- **Cost optimization chain** to ensure the trip fits within the budget.
- **API-based data retrieval** for top destinations and attractions.
- **PDF download option** for saving the generated trip plan.

---

## 🎥 Demo: How Yaatra AI Works

Below is a step-by-step guide on how Yaatra AI generates a personalized trip plan using AI.

## 1️⃣ **User Input Stage**  

The trip planning process starts with the user entering key details about their journey. This step-by-step input process ensures that Yatra AI generates a personalized itinerary based on user preferences.  

### 📌 **Step 1: Enter Destination & Date**  
The user begins by selecting the **destination** they want to visit and the **travel dates**. This helps the AI retrieve relevant location-specific data.  

![Step 1 - Destination & Date](images/input_1.png)  

### 📌 **Step 2: Set Trip Duration & Budget**  
Next, the user specifies how long they plan to stay and their total **budget**. The AI considers these constraints when generating an optimized itinerary.  

![Step 2 - Duration & Budget](images/input_2.png)  

### 📌 **Step 3: Choose Trip Type**  
Users can select the type of trip they want, such as:  
- **Solo** – Traveling alone.  
- **Friends** – A group trip with friends.  
- **Couple** – A romantic getaway.  
- **Family** – A vacation with family.  
- **Business** – A work-related trip.  

![Step 3 - Trip Type](images/input_3.png)  

### 📌 **Step 4: Select Mode of Transport**  
The user picks their preferred transportation method, which can include:  
- **Train**  
- **Bus**  
- **Plane**  

This choice affects the travel time and overall cost calculations.  

![Step 4 - Transport Mode](images/input_4.png)  

### 📌 **Step 5: Select Interests & Activities**  
Finally, the user selects their **areas of interest** for their trip.
The AI curates the itinerary based on these preferences.  

![Step 5 - Interests & Activities](images/input_5.png)  

---

### 2️⃣ **AI Processing & Trip Plan Generation**  
Once the user submits their preferences, Yaatra AI processes the data and retrieves relevant travel information using **ChromaDB and multi-chain RAG architecture**.  

The AI model generates a **personalized itinerary, estimated costs, and optimized travel plans**.

![AI Processing](images/output_1.png)  

After processing, the app dynamically updates and presents a **structured trip plan**.

![Generated Itinerary](images/output_2.png)

The itinerary consists of a plan for each day for the number of days the user is planning trip for.

![Generated Itinerary](images/output_3.png)

---

### 3️⃣ **Downloading the Trip Plan as a PDF**  
Users can download the AI-generated itinerary in **PDF format** for offline access.

Clicking the **"Download Trip PDF"** button generates a structured travel document.

![PDF Download](images/pdf_1.png)  

The downloaded PDF contains **all trip details, cost breakdown, and AI recommendations**.

![PDF Preview](images/pdf_2.png)
![PDF Preview](images/pdf_3.png)

---

### ✅ **Final Output**  
Yaatra AI provides a **well-structured trip itinerary** optimized for the user's preferences and budget. The system ensures that all aspects of the trip—including accommodation, transport, and activities—are planned efficiently.

This **intelligent travel planner** allows users to **save time, reduce planning effort, and get AI-powered recommendations**.

---

## 🛠 Tech Stack

Yaatra AI is built using a combination of **cutting-edge AI models, databases, and frameworks** to provide a seamless trip-planning experience.

### ⚡ **Core Technologies**
| Technology           | Description                                                         |
|----------------------|---------------------------------------------------------------------|
| **Streamlit**        | Frontend framework for building an interactive UI.                  |
| **LangChain**        | Framework for orchestrating LLM-based AI workflows.                 |
| **Ollama**           | Runs AI models locally for text generation and embeddings.          |
| **ChromaDB**         | Vector database for semantic search and AI-driven recommendations.  |
| **DeepSeek-R1:1.5B** | AI model used for generating trip itineraries.                      |
| **nomic-embed-text** | Embedding model for text-based similarity searches.                 |
| **Python**           | Main programming language for backend logic and AI processing.      |

---

### 🏗 **System Architecture**
The system follows a **modular approach** using the following key components:

1. **User Input Handling** → Collects user preferences and trip details via Streamlit UI.
2. **ChromaDB Retrieval** → Stores & fetches vectorized travel data for AI-based recommendations.
3. **Multi-Chain RAG Processing** →  
   - **Itinerary Chain**: Generates a structured trip plan.  
   - **Cost Optimization Chain**: Ensures the trip stays within budget.  
4. **AI-Powered Trip Generation** → Uses **deepseek-r1:1.5b** for itinerary suggestions.
5. **PDF Generation** → Formats and allows users to download their trip plan.

This **end-to-end AI pipeline** ensures that **real-time, dynamic, and cost-efficient** trip plans are generated seamlessly.

---

## 📁 Project Structure

```
yaatra-ai-trip-planner/
│── chromadb/
│    ├── chroma.sqlite3                 # ChromaDB database storing vector embeddings
│
│── data/
│    ├── __init__.py
│    ├── destination_data_extractor.py  # Extracts and processes destination data
│    ├── destination_data.json          # Stored travel data for trip generation
│    ├── destination_data.txt           # Raw text data for processing
│
│── images/                             # Input/output screenshots of the app
│
│── src/
│    │── __init__.py
│    │── chromaDB/
│    │    ├── __init__.py
│    │    ├── chroma_chunks.py          # Handles chunking and embedding storage
│    │── RAG_chains/
│    │    ├── __init__.py
│    │    ├── itinerary_chain.py        # Generates itinerary based on user input
│
│── utils/
│    ├── __init__.py
│    ├── download_trip.py               # Generates and downloads trip PDF
│    ├── trip_data.py                   # Processes and formats trip data
│
│── app.py                              # Main Streamlit application
│── requirements.txt                    # Dependencies
│── README.md                           # Project Documentation
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-repo/yaatra-ai-trip-planner.git
cd yaatra-ai-trip-planner
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Start ChromaDB

Ensure ChromaDB is running:

```bash
python -m chromadb
```

### 4️⃣ Download Required AI Models

```bash
ollama pull nomic-embed-text  # For embedding text data
ollama run deepseek-r1:1.5b   # For AI-generated trip recommendations
```

### 5️⃣ Run the App

```bash
streamlit run app.py
```

---

## 🧠 How It Works

### 🔹 AI-Driven Trip Planning

1. **User Input Collection**: Users enter their destination, budget, travel dates, and trip type. Inputs are stored in session state for dynamic updates.

2. **AI-Powered Recommendations**: The app retrieves relevant travel data using an API endpoint and generates an itinerary.
   - The app retrieves relevant travel data using an API endpoint.
   - Itinerary generation is done using a **multi-chain RAG** approach:
     - **Itinerary Chain**: Plans the day-wise schedule.

3. **PDF Generation & Download**:  
   - Users can download their AI-generated trip plan as a **PDF file**.
   - The `download_trip.py` module formats the data and saves it as a PDF.

---

## 🔗 Future Improvements

- **Integrating real-time flight & hotel data** from external APIs.
- **Adding user authentication** to save and access past trips.
- **Improving itinerary personalization** using advanced AI models.

---

## 📝 License

This project is licensed under the MIT License.

---

## 💬 Contact & Contributions

🚀 **Have feedback or want to contribute?** Feel free to open an issue or submit a pull request on GitHub. Your contributions are always welcome!  

💡 **Suggest Features & Report Issues:** If you have ideas for new features or encounter any issues, please **raise an issue** on the GitHub repository. Your feedback helps make Yaatra AI even better!  

📧 **Contact:** [Gaurav Kumar Singh](mailto:gauravsingh96753@gmail.com)  
🔗 **GitHub:** [Gaurav-576](https://github.com/Gaurav-576)  
🌐 **Portfolio:** [My Website](https://my-portfolio-website-gaurav.streamlit.app)  
🔗 **LinkedIn:** [Gaurav Singh](https://www.linkedin.com/in/gaurav-singh-mlops)  

---

## ⭐ Support & Acknowledgments  

If you found **Yaatra AI** useful, please **⭐ star this repository** on GitHub! Your support helps in improving and adding new features.  

💡 **Special thanks to the Open-Source Community** for providing the tools and resources that power this project! 🚀✨  

_“Travel far enough, you meet yourself.” — David Mitchell_  

