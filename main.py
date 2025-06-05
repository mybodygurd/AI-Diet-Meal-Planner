from fastapi import FastAPI
from models import InventoryResponse, DietResponse, InventoryInput, DietInput
from agents.inventory_agent import InventoryAgent
from agents.diet_agent import DietAgent

app = FastAPI(
    title="AI Diet & Meal Planner",
    description="A multi-agent system for personalized meal planning"
)
@app.get('/')
async def health_check():
    return {"message": "Success!"}

@app.post('/inventory', response_model=InventoryResponse)
async def submit_inventory(input: InventoryInput):
    agent = InventoryAgent()
    return await agent.run(input.items)
     
@app.post('/diet', response_model=DietResponse)
async def filter_diet(input: DietInput):
    agent = DietAgent()
    return  await agent.run(input.items, input.diet)