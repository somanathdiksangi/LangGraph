from langgraph.graph import StateGraph ,START,END
from src.langgraphagenticai.state.state import state
from src.langgraphagenticai.nodes.basic import basic_node


class graph:
    def __init__(self,model):
        self.llm=model
        self.graph_bilder=StateGraph(state)

    def basic_chatbot(self):

        self.basic_chatbot=basic_node(self.llm)
        self.graph_bilder.add_node("chatbot",self.basic_chatbot.process)
        self.graph_bilder.add_edge(START,'chatbot')
        self.graph_bilder.add_edge('chatbot',END)

    def setup_graph(self,usecase):
        if usecase =="Basic Chatbot":
            self.basic_chatbot()
