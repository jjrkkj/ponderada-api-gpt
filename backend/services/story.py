# Create
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import sqlite3

router = APIRouter()

class Story(BaseModel):
    title: str
    description: str
    category: str

# Create
@router.post("/story/")
def create_story(story: Story):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO story (title, description, category) VALUES (?, ?, ?)''',
                   (story.title, story.description, story.category))
    conn.commit()
    conn.close()
    return story

# Read
@router.get("/story/{story_id}")
def read_story(story_id: int):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''SELECT * FROM story WHERE id = ?''', (story_id,))
    story = cursor.fetchone()
    conn.close()
    if story:
        return {"title": story[0], "description": story[1], "category": story[2]}
    else:
        return {"message": "Story not found"}

# Update
@router.put("/story/{story_id}")
def update_story(story_id: int, story: Story):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''UPDATE story SET title=?, description=?, category=? WHERE id=?''',
                   (story.title, story.description, story.category, story_id))
    conn.commit()
    conn.close()
    return {"message": "story updated successfully"}

# Delete
@router.delete("/story/{story_id}")
def delete_story(story_id: int):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''DELETE FROM story WHERE id=?''', (story_id,))
    conn.commit()
    conn.close()
    return {"message": "story deleted successfully"}