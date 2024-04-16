from dotenv import load_dotenv

load_dotenv()

import streamlit as st
import os
import google.generativeai as genai
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
##function to get gemini ai model and create responses

model=genai.GenerativeModel("gemini-pro")
def get_gemini_response(question):
    response=model.generate_content(question)
    return response.text

##setup streamlit
st.set_page_config(page_title="Q&A Demo")
st.header("Reconnect")
job_title = st.text_input("Enter the job title:", key="job_title")
submit =st.button("Generate Roadmap")

input_prompt1 = """
 You are a career guide and you have to take the {job_title}  as input and in step wise bullet points generate the career
 roadmap and learning resources available on the internet."""


if submit:
    response=get_gemini_response(job_title+input_prompt1)
    st.subheader("The Repsonse is")
    st.write(response)

