import streamlit as st
from src.langgraphagenticai.ui.streamlitui.loadui import LoadStreamlitUI

def laod_langgraph_agentic_ai():
    ui=LoadStreamlitUI()
    user_input=ui.load_streamlit_ui()

    if not user_input:
        st.error("Error is in user input")
        return
    user_message=st.chat_input("Enter your messages")
    if user_message:
        try:
            obj_llm=

        