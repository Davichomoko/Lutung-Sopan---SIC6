from pymongo import MongoClient


client = MongoClient("mongodb+srv://fico:kuyukuyu@cluster0.um4gw.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

db = client["myDB"]  
collection = db["myCollect"]  
