from agents.agent import Agent
from services.llm_client import LLMClient
from models import DietResponse
from pydantic import ValidationError
import json


class DietAgent(Agent):
    def __init__(self):
        self.llm = LLMClient()
        
    async def run(self, items: list[str], diet: str) -> DietResponse:
        prompt = (
            f"You are a dietitian. Given the JSON array of ingredients:\n"
            f"{json.dumps(items)}\n"
            f"And the dietary preference: {diet}\n"
            "Return a JSON object with:\n"
            f"  compatible_items: an array of ingredients that comply with the {diet} diet,\n"
            "  suggested_recipe_ideas: an array of exactly five meal ideas using only the compatible ingredients.\n"
            "Respond ONLY with valid JSON."
        )
        response = await self.llm.call_model(prompt)
        try:
            response_dict = json.loads(response)
            return DietResponse(**response_dict)
        except (json.JSONDecodeError, ValidationError, TypeError):
            return DietResponse(compatible_items=[], suggested_recipe_ideas=[])
        
