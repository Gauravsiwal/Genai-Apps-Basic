import streamlit as st
import google.generativeai as genai

# Configure api key
api_key = 'AIzaSyCxwLPHCeAZ7EDKoukAXXMYzMoCH3JdASU'
genai.configure(api_key=api_key)

# Get the model
model = genai.GenerativeModel("gemini-1.5-pro")

st.header('This is a sample AI App')


