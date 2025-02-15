import streamlit as st
import openai
import os
import fitz  # PyMuPDF for PDF processing
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Streamlit UI
st.title("RFP AI Assistant - MVP")

st.sidebar.header("Company Settings")
company_name = st.sidebar.text_input("Company Name")
company_description = st.sidebar.text_area("Company Description")

st.header("Upload an RFP")
uploaded_file = st.file_uploader("Upload an RFP document (PDF/TXT)", type=["txt", "pdf"])

# Function to extract text from PDF
def extract_text_from_pdf(pdf_file):
    text = ""
    with fitz.open(stream=pdf_file.read(), filetype="pdf") as doc:
        for page in doc:
            text += page.get_text("text") + "\n"
    return text

if uploaded_file:
    file_content = ""

    # Handle TXT and PDF files separately
    if uploaded_file.type == "text/plain":
        file_content = uploaded_file.read().decode("utf-8")
    elif uploaded_file.type == "application/pdf":
        file_content = extract_text_from_pdf(uploaded_file)

    st.text_area("RFP Content", file_content, height=300)

    if st.button("Generate AI Response"):
        with st.spinner("Generating response..."):
            prompt = f"""
            You are an AI specialized in responding to RFPs. The company details are:
            Company: {company_name}
            Description: {company_description}

            The RFP document is as follows:
            {file_content}

            Generate a professional response.
            """
            response = openai.chat.completions.create(
                model="gpt-4",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.7
            )
            st.subheader("AI-Generated Response")
            st.write(response.choices[0].message.content)