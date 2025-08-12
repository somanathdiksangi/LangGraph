from configparser import ConfigParser

class Config:
    def __init__(self, config_file=r"C:\Users\acer\Desktop\LangGraph-WorkSpace\project\agentic_chatbot\src\langgraphagenticai\ui\uiconfig.ini"):
        self.config = ConfigParser()
        self.config.read(config_file)

    def get_llm_options(self):
        value = self.config["DEFAULT"].get("LLM_OPTION", "")
        return [opt.strip() for opt in value.split(",") if opt.strip()]
    
    def get_usecase_options(self):
        value = self.config["DEFAULT"].get("USECASE_OPTION", "")
        return [opt.strip() for opt in value.split(",") if opt.strip()]
    
    def get_groq_model_options(self):
        value = self.config["DEFAULT"].get("GROQ_MODEL_OPTION", "")
        return [opt.strip() for opt in value.split(",") if opt.strip()]
    
    def get_page_title(self):
        return self.config["DEFAULT"].get("PAGE_TITLE", "Agentic Chatbot")
