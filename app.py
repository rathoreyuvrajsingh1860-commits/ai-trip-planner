import os
import streamlit as st
import vertexai
from vertexai.generative_models import GenerativeModel

# 1. Initialize Vertex AI
PROJECT_ID = "ai-travel-planner-472410" # your project
LOCATION = "us-central1"

vertexai.init(project=PROJECT_ID, location=LOCATION)

# 2. Load Gemini model
model = GenerativeModel("gemini-1.5-flash")

# 3. Streamlit UI
st.set_page_config(page_title="AI Trip Planner MVP", page_icon="🌍")
st.title("🌍 AI-Powered Trip Planner")
st.write("Enter your trip details and let AI create a personalized itinerary!")

# User inputs
destination = st.text_input("✈️ Destination", "Paris")
days = st.number_input("🗓️ Number of Days", min_value=1, max_value=30, value=3)
budget = st.selectbox("💰 Budget Level", ["Low", "Medium", "High"])
interests = st.multiselect(
    "🎯 Interests",
    ["Culture", "Adventure", "Food", "Nightlife", "Shopping", "Nature"],
    default=["Culture", "Food"]
)

if st.button("Generate Itinerary"):
    with st.spinner("🧳 Planning your trip..."):
        prompt = f"""
        Create a {days}-day travel itinerary for {destination}.
        Budget: {budget}.
        Interests: {', '.join(interests)}.
        Provide a daily breakdown with activities and tips.
        """

        response = model.generate_content(prompt)
        st.success("Here’s your personalized trip plan:")
        st.write(response.text)