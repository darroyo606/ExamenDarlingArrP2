
from pymongo.mongo_client import MongoClient
from dotenv import load_dotenv
import os
load_dotenv()
user=os.getenv('MONGO_USER')
password=os.getenv('MONGO_PASSWORD')

uri = f"mongodb+srv://{user}:{password}@cluster0.ij08aaa.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(uri)

try:
    client.admin.command('ping')
    print("Ping, La conexion ha sido exitosa!")
except Exception as e:
    print(e)