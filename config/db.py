from pymongo import MongoClient

client = MongoClient("mongodb+srv://mohdahmeduddinaaa:UZJfMwBLr7Ta5p2W@cluster0.febpr2t.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

db=client.students_db

collection_name=db["students_collection"]