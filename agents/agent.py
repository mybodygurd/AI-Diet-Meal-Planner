from services.llm_client import LLMClient 
from abc import ABC, abstractmethod


class Agent(ABC):
    @abstractmethod
    def __init__(self):
        self.llm = LLMClient()
        
    @abstractmethod    
    async def run(self):
        pass