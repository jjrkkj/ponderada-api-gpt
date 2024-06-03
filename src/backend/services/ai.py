# Create
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import google.generativeai as genai

API_KEY = 'AIzaSyDEvmxws7CcSIqJr6CUVGqnXnjpH5IXz-M'
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-pro')

router = APIRouter()

class Prompt(BaseModel):
    prompt: str

# Read
@router.post("/ai/")
def get_ai_response(prompt: Prompt):
    response = model.generate_content(prompt.prompt)
    return {"response": response.text}
