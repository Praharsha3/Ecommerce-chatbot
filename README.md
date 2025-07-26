# E-commerce Clothing Chatbot
A customer support chatbot for answering product and order-related queries using an E-commerce dataset.
Ecommerce Chatbot

Project Overview

An AI-powered full-stack customer support chatbot for an e-commerce clothing platform.

Features

Chat interface powered by React

FastAPI backend with conversation history

SQLite or PostgreSQL integration

LLM-ready via Groq or OpenAI


Setup Instructions

Prerequisites

Node.js + npm

Python 3.9+

Docker & Docker Compose


Local Setup

git clone https://github.com/your-username/ecommerce-chatbot.git
cd ecommerce-chatbot

# Load dataset (optional)
cd backend
pip install -r requirements.txt
python load_data.py

# Start FastAPI server
uvicorn chatbot:app --reload --host 0.0.0.0 --port 8000

# In another terminal
cd frontend
npm install
npm start

Dockerized Setup

docker-compose up --build

API Endpoints

POST /api/chat - Chat with AI

GET /api/conversations - List past conversations

GET /api/messages/{session_id} - Get chat history


Technologies

React, FastAPI, SQLAlchemy, SQLite/PostgreSQL, Docker
