

import pandas as pd 
from sqlalchemy.orm import Session
from database import SessionLocal, engine 
from models import Base 
import os

# Load dataset into your database

Base.metadata.create_all(bind=engine)

def load_csv(): session = SessionLocal() 
products_df = pd.read_csv("ecommerce-dataset/products.csv") 
orders_df = pd.read_csv("ecommerce-dataset/orders.csv") # Insert into database if you define Product/Order tables # For now, this just demonstrates setup print("CSV Loaded") session.close()

if name == 'main': load_csv()