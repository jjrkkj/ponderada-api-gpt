from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import sqlite3

router = APIRouter()

class User(BaseModel):
    name: str
    username: str
    password: str

# Create
@router.post("/user/")
def create_user(user: User):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO user (name, username, password) VALUES (?)''', (user.name, user.username, user.password))
    conn.commit()
    conn.close()
    return user

# Read
@router.get("/user/{user_id}")
def read_user(user_id: int):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''SELECT * FROM user WHERE id = ?''', (user_id,))
    user = cursor.fetchone()
    conn.close()
    if user:
        return {"name": user[0]}
    else:
        return {"message": "User not found"}

# Update
@router.put("/user/{user_id}")
def update_user(user_id: int, user: User):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''UPDATE user SET name=?, username=?, password=? WHERE id=?''',
                   (user.name, user.username, user.password, user_id))
    conn.commit()
    conn.close()
    return {"message": "User updated successfully"}

# Delete
@router.delete("/user/{user_id}")
def delete_user(user_id: int):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''DELETE FROM user WHERE id=?''', (user_id,))
    conn.commit()
    conn.close()
    return {"message": "User deleted successfully"}