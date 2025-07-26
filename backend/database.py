
from sqlalchemy import create_engine 
from sqlalchemy.ext.declarative import declarative_base 
from sqlalchemy.orm import sessionmaker 
import os 
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./chatbot.db")

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False}) SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine) Base = declarative_base()

File: backend/models.py

from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime 
from sqlalchemy.orm import relationship 
from datetime import datetime 
from database import Base

class User(Base): tablename = "users" 
id = Column(Integer, primary_key=True, index=True) 
name = Column(String, unique=True, index=True) 
sessions = relationship("Session", back_populates="user")

class Session(Base): tablename = "sessions" 
id = Column(Integer, primary_key=True, index=True) 
user_id = Column(Integer, ForeignKey("users.id")) 
created_at = Column(DateTime, default=datetime.utcnow) 
user = relationship("User", back_populates="sessions") 
messages = relationship("Message", back_populates="session")

class Message(Base): tablename = "messages" 
id = Column(Integer, primary_key=True, index=True) 
session_id = Column(Integer, ForeignKey("sessions.id")) 
role = Column(String) # 'user' or 'ai' content = Column(Text) timestamp = Column(DateTime, default=datetime.utcnow) session = relationship("Session", back_populates="messages")





# Milestone 5: Add real LLM logic using Groq/OpenAI later

# Add this to .env file in backend/

# DATABASE_URL=sqlite:///./chatbot.db

# OPENAI_API_KEY=your-key

# Commit Example

# git add .

# git commit -m "feat: complete Milestone 2 and 3 with schema and data ingestion"

# git push origin main