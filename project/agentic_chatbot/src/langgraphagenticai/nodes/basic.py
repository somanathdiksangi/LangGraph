from src.langgraphagenticai.state.state import state



class basic_node:
    def __init__(self,model):
        self.llm=model
    def process(self,state:state)->dict:
        return{'message':self.llm.invoke(state['message'])}

    