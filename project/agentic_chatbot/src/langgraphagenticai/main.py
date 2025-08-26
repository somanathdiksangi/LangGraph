import streamlit as st
from src.langgraphagenticai.ui.streamlitui.loadui import LoadStreamlitUI
from src.langgraphagenticai.LLMS.groqllm import groqLLM
from src.langgraphagenticai.graph.graph_bilder import graph

def laod_langgraph_agentic_ai():
    ui=LoadStreamlitUI()
    user_input=ui.load_streamlit_ui()

    if not user_input:
        st.error("Error is in user input")
        return
    user_message=st.chat_input("Enter your messages")
    if user_message:
        try:
            obj_llm=groqLLM(user_contols_input=user_input)
            model=obj_llm.get_llm()
            if not model:
                st.error("Error llm model could not be initilize")
                return
            usecase=user_input.get("selected_usecase")
            if not usecase:
                st.error("Error no use case seleceted ")
                return
            graph_bilder=graph(model)
            try:
                graph=graph_bilder.setup_graph(usecase)
            except Exception as e:
                st.error(f"graph setup faim {e}")
        except Exception as e:
            


        