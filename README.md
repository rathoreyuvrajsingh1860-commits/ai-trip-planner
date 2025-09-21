# 🌍 AI Trip Planner (Hackathon Prototype)

An AI-powered travel planning assistant that creates **personalized itineraries** based on destination, budget, duration, and interests.  
Built for **GenAI Exchange Hackathon** 🏆.

---

## ✨ Problem Statement
Planning trips is often stressful and time-consuming.  
Users spend hours searching blogs, reviews, and maps to design a good travel plan.  
Existing tools are either too generic or too complex.

---

## 💡 Our Solution
The **AI Trip Planner** uses **Google Gemini (Vertex AI)** to:
- Understand user preferences (budget, days, interests).
- Generate **personalized travel itineraries** instantly.
- Suggest activities, places, and tips for each day.

---

## 🚀 Features
- 📝 Input trip details (Destination, Budget, Days, Interests).  
- 🤖 AI-generated itinerary with day-wise breakdown.  
- 🌐 Deployed on **Google Cloud Run**.  
- 📦 Containerized with **Docker**.  

---

## 🛠️ Tech Stack
- **Frontend**: Streamlit (UI for form + results).  
- **Backend**: Python (app logic).  
- **AI Model**: Google Gemini (via Vertex AI).  
- **Cloud**: Google Cloud Run, Artifact Registry.  
- **Version Control**: GitHub.  

---

## 📂 Project Structure

├── app.py # Main Streamlit app ├── agent.py # AI assistant logic ├── Dockerfile # Container definition ├── requirements.txt # Dependencies └── README.md # Documentation

---

## ⚡ How to Run Locally
1. Clone repo:
   ```bash
   git clone https://github.com/rathoreyuvrajsingh1860-commits/ai-trip-planner.git
   cd ai-trip-planner
