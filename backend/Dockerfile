FROM python:3.9 WORKDIR /app COPY . . RUN pip install --no-cache-dir -r requirements.txt CMD ["uvicorn", "chatbot:app", "--host", "0.0.0.0", "--port", "8000"]
