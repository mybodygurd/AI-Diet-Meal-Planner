from fastapi import FastAPI

app = FastAPI(
    title="AI Diet & Meal Planner",
    description="A multi-agent system for personalized meal planning"
)
@app.get('/')
async def health_check():
    return {"message": "Success!"}