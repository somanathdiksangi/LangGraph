import os
from dotenv import load_dotenv
from typing import TypedDict , Annotated
from langgraph.graph.message import add_messages
from langgraph.graph import StateGraph ,START,END
from langgraph.graph.message import add_messages
from langchain_core.messages import AnyMessage



load_dotenv()
os.environ["GROQ_API_KEY"]=os.getenv("GROQ_API_KEY")
from langchain_groq import ChatGroq
llm=ChatGroq(model="gemma2-9b-it")
os.environ["LANGSMITH_API_KEY"]=os.getenv("LANGSMITH_API_KEY")

class State(TypedDict):
    messages:Annotated[list[AnyMessage],add_messages]

def make_defalt():
    graph=StateGraph(State)
    def mosel_call(State):
        return{'messages':[llm.invoke(State['messages'])]}
    graph.add_node('mosel_call',mosel_call)
    graph.add_edge(START,'mosel_call')
    graph.add_edge('mosel_call',END)
    workflow=graph.compile()
    return workflow


agent=make_defalt()




