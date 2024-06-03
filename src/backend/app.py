from fastapi import FastAPI, HTTPException
from services import story, user, ai

app = FastAPI()

app.include_router(story.router)
app.include_router(user.router)
app.include_router(ai.router)