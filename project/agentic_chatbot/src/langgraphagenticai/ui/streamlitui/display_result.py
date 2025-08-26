import streamlit as st
from langchain_core.messages import AIMessage,HumanMessage,ToolMessage
import json

class displayresult:
    def __init__(self,usecase,graph,user_message):
        self.usecase=usecase
        self.graph=graph
        self.user_message=user_message
    
    def displayonui(self):
        usecase=self.usecase
        graph=self.graph
        user_message=self.user_message
        if usecase == "Basic Chatbot":
            for event in graph.stream({'message':("user",user_message)}):
                print(event.values())
                for 
        