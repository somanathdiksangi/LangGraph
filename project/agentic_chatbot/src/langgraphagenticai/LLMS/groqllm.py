import os
import streamlit as st
from langchain_groq import ChatGroq
class groqLLM:
    def __init__(self,user_contols_input):
        self.user_controls_input=user_contols_input

    def get_llm(self):
        try:
            groq_api_key=self.user_controls_input["GROQ_API_KEY"]
            selected_groq_model=self.user_controls_input["selected_groq_model"]
            if groq_api_key=='' and os.environ["GROQ_API_KEY"]=='':
                st.error("please enter the Groq api key")
            llm=ChatGroq(api_key=groq_api_key,model=selected_groq_model)
        except Exception as e:
            raise ValueError(e)
        return llm

