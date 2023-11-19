import os

import dotenv
from pymongo import MongoClient
from pymongo.server_api import ServerApi

dotenv.load_dotenv()

client = None


def get_database():
    global client
    CONNECTION_STRING = os.getenv("MONGODB_CONNECT_STRING")
    if client:
        return client
    client = MongoClient(CONNECTION_STRING, server_api=ServerApi("1"))
    try:
        client.admin.command("ping")
        print("Pinged your deployment. You successfully connected to MongoDB!")
    except Exception as e:
        print("Unable to connect to MongoDB Atlas")
        print(e)
    return client


if __name__ == "__main__":
    print(get_database())
