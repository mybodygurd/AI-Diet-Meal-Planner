from inventory_agent import InventoryAgent
from diet_agent import DietAgent
from models import AskResponse
from pydantic import ValidationError
import json


class AgentManager:
    def __init__(self):
        self.inv_agent = InventoryAgent()
        self.diet_agent = DietAgent()
        
    async def run(self, items: list[str], diet: str):
        try:
            inv_response = await self.inv_agent.run(items)
            usable_items = json.loads(inv_response.usable_items)
            diet_response = await self.diet_agent.run(usable_items, diet)
            response_dict = json.loads(diet_response)
            return AskResponse(**response_dict)
        except (json.JSONDecodeError, ValidationError, TypeError):
            return AskResponse(usable_items=[], diet_filtered=[], suggestions=[])
