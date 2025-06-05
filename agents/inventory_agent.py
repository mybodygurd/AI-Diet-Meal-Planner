from agents.agent import Agent
from services.llm_client import LLMClient
from models import InventoryResponse
from pydantic import ValidationError
import json

class InventoryAgent(Agent):
    def __init__(self):
        self.llm = LLMClient()
        
    async def run(self, items: list[str]) -> InventoryResponse:
        prompt = (
            f"You are a kitchen assistant. Given the JSON array of ingredients:\n"
            f"{json.dumps(items)}\n"
            "Return a JSON object with:\n"
            "  usable_items: an array of ingredients that are non-empty and suitable for cooking (remove blank or invalid entries),\n"
            "  message: a short confirmation string.\n"
            "Respond ONLY with valid JSON."
        )
        response = await self.llm.call_model(prompt)
        try:
            response_dict = json.loads(response)
            return InventoryResponse(**response_dict)
        except (json.JSONDecodeError, ValidationError, TypeError):
            return InventoryResponse(usable_items=[], message="Invalid response. Please try again.")
    