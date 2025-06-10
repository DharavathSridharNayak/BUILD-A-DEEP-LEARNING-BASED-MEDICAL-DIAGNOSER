import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image
import time

# Set page configuration
st.set_page_config(
    page_title="🩺MEDICAL DIAGNOSER🏥",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for styling
st.markdown("""
    <style>
    .main {
        background-color: #f5f5f5;
    }
    .sidebar .sidebar-content {
        background-color: #2e7d32;
        color: white;
    }
    .stButton>button {
        background-color: #2e7d32;
        color: white;
        border-radius: 5px;
        padding: 0.5rem 1rem;
        border: none;
    }
    .stButton>button:hover {
        background-color: #1b5e20;
        color: white;
    }
    .stTextInput>div>div>input {
        border-radius: 5px;
    }
    .stSelectbox>div>div>select {
        border-radius: 5px;
    }
    .stNumberInput>div>div>input {
        border-radius: 5px;
    }
    .reportview-container .main .block-container {
        padding-top: 2rem;
    }
    h1 {
        color: #2e7d32;
    }
    h2 {
        color: #1b5e20;
    }
    </style>
    """, unsafe_allow_html=True)

# App header
st.title("🩺MEDICAL DIAGNOSER🏥")
st.markdown("""
    Welcome to our AI-powered medical diagnosis tool. This application helps predict potential 
    health conditions based on your symptoms and medical history. Please fill in the details below.
    """)

# Sidebar
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/2781/2781395.png", width=100)
    st.title("About")
    st.info("""
        This AI medical diagnoser uses deep learning models trained on thousands of medical records 
        to provide preliminary health assessments. Always consult with a healthcare professional 
        for accurate diagnosis.
        """)
    
    st.title("Disclaimer")
    st.warning("""
        This tool is not a substitute for professional medical advice, diagnosis, or treatment. 
        Always seek the advice of your physician or other qualified health provider with any 
        questions you may have regarding a medical condition.
        """)

# Main content
tab1, tab2, tab3 = st.tabs(["Diagnosis", "Health Tips", "About"])

with tab1:
    st.header("Patient Information")
    col1, col2 = st.columns(2)
    
    with col1:
        name = st.text_input("Full Name")
        age = st.number_input("Age", min_value=0, max_value=120, value=30)
        gender = st.selectbox("Gender", ["Male", "Female", "Other"])
        
    with col2:
        weight = st.number_input("Weight (kg)", min_value=0, max_value=300, value=70)
        height = st.number_input("Height (cm)", min_value=0, max_value=250, value=170)
        blood_pressure = st.text_input("Blood Pressure (e.g., 120/80)")
    
    st.header("Symptoms")
    symptoms = st.multiselect("Select your symptoms", [
        "Fever", "Headache", "Fatigue", "Cough", "Shortness of breath",
        "Chest pain", "Nausea", "Dizziness", "Abdominal pain", "Joint pain",
        "Rash", "Weight loss", "Weight gain", "Blurred vision", "Frequent urination"
    ])
    
    additional_info = st.text_area("Additional information about your condition")
    
    # Simulate diagnosis (in a real app, this would call your DL model)
    if st.button("Run Diagnosis"):
        if not symptoms:
            st.error("Please select at least one symptom")
        else:
            with st.spinner("Analyzing your symptoms..."):
                time.sleep(3)  # Simulate model processing
                
                # Generate a "diagnosis" (in a real app, this would be your model's prediction)
                conditions = {
                    "Fever": ["Common cold", "Flu", "COVID-19"],
                    "Headache": ["Migraine", "Tension headache", "Sinusitis"],
                    "Fatigue": ["Anemia", "Chronic fatigue syndrome", "Depression"],
                    "Cough": ["Bronchitis", "Pneumonia", "Asthma"]
                }
                
                possible_conditions = []
                for symptom in symptoms:
                    if symptom in conditions:
                        possible_conditions.extend(conditions[symptom])
                
                if not possible_conditions:
                    possible_conditions = ["No specific condition identified based on symptoms"]
                
                # Display results
                st.success("Analysis complete!")
                st.subheader("Possible Conditions")
                
                # Remove duplicates and show top 3
                possible_conditions = list(set(possible_conditions))[:3]
                
                for i, condition in enumerate(possible_conditions, 1):
                    st.markdown(f"{i}. **{condition}**")
                
                # Show some stats (simulated)
                st.subheader("Health Insights")
                col1, col2, col3 = st.columns(3)
                
                with col1:
                    st.metric("Risk Level", "Medium", "5% higher than average")
                
                with col2:
                    st.metric("Recommended Tests", "Blood work", "Complete blood count")
                
                with col3:
                    st.metric("Suggested Specialist", "General Physician", "For initial consultation")
                
                # Generate a simple health chart (simulated)
                st.subheader("Health Indicators")
                fig, ax = plt.subplots(figsize=(10, 4))
                indicators = ['Heart Rate', 'Blood Sugar', 'Cholesterol', 'Blood Pressure']
                values = [72, 95, 180, 120]
                sns.barplot(x=indicators, y=values, palette="viridis", ax=ax)
                ax.set_ylabel("Value")
                ax.set_title("Simulated Health Metrics")
                st.pyplot(fig)
                
                st.info("""
                    **Next Steps**: 
                    - Consult with a healthcare professional
                    - Consider the recommended tests
                    - Monitor your symptoms
                    """)

with tab2:
    st.header("Health Tips & Prevention")
    
    tips = {
        "General Health": [
            "Get 7-9 hours of sleep each night",
            "Stay hydrated by drinking plenty of water",
            "Wash your hands frequently to prevent infections"
        ],
        "Nutrition": [
            "Eat a balanced diet with plenty of fruits and vegetables",
            "Limit processed foods and added sugars",
            "Choose whole grains over refined grains"
        ],
        "Exercise": [
            "Aim for at least 150 minutes of moderate exercise per week",
            "Include strength training exercises 2-3 times per week",
            "Take short walking breaks if you sit for long periods"
        ],
        "Mental Health": [
            "Practice stress-reduction techniques like meditation",
            "Stay connected with friends and family",
            "Seek professional help if you feel overwhelmed"
        ]
    }
    
    for category, items in tips.items():
        with st.expander(category):
            for item in items:
                st.markdown(f"- {item}")
    
    st.image("https://images.unsplash.com/photo-1498837167922-ddd27525d352?ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&q=80", 
             caption="Healthy lifestyle choices can prevent many common health issues")

with tab3:
    st.header("About This Application")
    st.markdown("""
        This AI Medical Diagnoser is powered by deep learning models trained on extensive medical datasets 
        to provide preliminary health assessments based on reported symptoms.
        
        **How it works:**
        1. Patients input their symptoms and basic health information
        2. Our AI analyzes the patterns against known medical conditions
        3. The system suggests possible conditions and next steps
        
        **Technology Stack:**
        - Deep Learning Models (TensorFlow/PyTorch)
        - Medical Ontologies for symptom-disease mapping
        - Natural Language Processing for understanding free-text inputs
        
        **Important Notes:**
        - This tool is for informational purposes only
        - Always consult with a qualified healthcare provider
        - The accuracy depends on the information provided
        """)
    
    st.header("Development Team")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=100)
        st.markdown("**Dr. Sarah Johnson**\n\nMedical Director")
    
    with col2:
        st.image("https://cdn-icons-png.flaticon.com/512/3135/3135768.png", width=100)
        st.markdown("**Alex Chen**\n\nAI Engineer")
    
    with col3:
        st.image("https://cdn-icons-png.flaticon.com/512/3135/3135823.png", width=100)
        st.markdown("**Maria Garcia**\n\nData Scientist")
    
    st.markdown("---")
    st.markdown("© 2023 AI Medical Diagnoser. All rights reserved.")
