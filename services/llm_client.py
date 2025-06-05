from dotenv import load_dotenv
load_dotenv()
import os
from groq import AsyncGroq
from typing import Dict, Any


class LLMClient:
    def __init__(self):
        self.api_key = os.getenv("LLM_API_KEY")
        if not self.api_key:
            raise ValueError("LLM_API_KEY not found in environment variables")
        self.model = "llama3-8b-8192"
        self.client = AsyncGroq(api_key=self.api_key)
        self.temperature= 0.3
        
    async def call_model(self, prompt: str) -> Dict[str, Any]:
        try:
            response =  await self.client.chat.completions.create(
                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                model=self.model,
                temperature=self.temperature
            )
            return response.choices[0].message.content
        except Exception as e:
            raise Exception(f"LLM call failed: {str(e)}")