
from fastapi import FastAPI, Depends, HTTPException 
from sqlalchemy.orm import Session 
from models import Base, User, Session as ChatSession, Message 
from database import engine, SessionLocal 
import uuid 
import os 
import openai

Base.metadata.create_all(bind=engine)
app = FastAPI()

Dependency

def get_db(): db = SessionLocal() 
try: 
    yield db 
finally: db.close()

@app.post("/api/chat") 
def chat(user_id: int, message: str, conversation_id: int = None, db: Session = Depends(get_db)): 
    if conversation_id is None: session_obj = ChatSession(user_id=user_id) db.add(session_obj) db.commit() db.refresh(session_obj) else: session_obj = db.query(ChatSession).filter(ChatSession.id == conversation_id).first() if not session_obj: raise HTTPException(status_code=404, detail="Conversation not found")

    # Save user message
    user_msg = Message(session_id=session_obj.id, role="user", content=message)
    db.add(user_msg)

    # Dummy AI response (Replace with real LLM logic in Milestone 5)
    ai_response = f"You asked: '{message}', let me find that out for you."
    ai_msg = Message(session_id=session_obj.id, role="ai", content=ai_response)
    db.add(ai_msg)

    db.commit()
    return {"conversation_id": session_obj.id, "response": ai_response}