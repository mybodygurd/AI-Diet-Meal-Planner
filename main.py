from fastapi import FastAPI, HTTPException
from models import InventoryResponse, DietResponse, InventoryInput, DietInput
from agents.inventory_agent import InventoryAgent
from agents.diet_agent import DietAgent
from logger import get_logger

logger = get_logger(__name__)

app = FastAPI(
    title="AI Diet & Meal Planner",
    description="A multi-agent system for personalized meal planning"
)
@app.get('/')
async def health_check():
    logger.info("Health check endpoint called")
    return {"message": "Success!"}

@app.post('/inventory', response_model=InventoryResponse)
async def submit_inventory(input: InventoryInput):
    try:
        agent = InventoryAgent()
        response = await agent.run(input.items)
        logger.info(f"Inventory processed: {response.usable_items}")
        return response
    except Exception as e:
        logger.error(f"Error processing inventory: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))
     
@app.post('/diet', response_model=DietResponse)
async def filter_diet(input: DietInput):
    try:
        agent = DietAgent()
        response = await agent.run(input.items, input.diet)
        return response
    except Exception as e:
        logger.error(f"Error processing diet: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))
