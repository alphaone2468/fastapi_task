from pymongo import MongoClient
from dotenv import load_dotenv,dotenv_values
import os
value=os.getenv("MONGOURL")

client = MongoClient(value)

db=client.students_db

collection_name=db["students_collection"]

# mongodb+srv://mohdahmeduddinaaa:UZJfMwBLr7Ta5p2W@cluster0.febpr2t.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0