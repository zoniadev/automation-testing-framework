from pymongo import MongoClient
from pymongo.errors import PyMongoError
from datetime import datetime, timedelta
import os
from urllib.parse import quote_plus


def connect_to_mongodb():
    username = "automationtests"
    password = quote_plus("QAZwsx@123")  # Make sure to encode special characters

    cluster_url = os.getenv("MONGO_CLUSTER_URL", "mongodb6stage.uh1qx.mongodb.net")
    db_name = os.getenv("MONGO_DB_NAME", "GoHealthyUsers")  # Replace with your actual DB name

    connection_string = (
        f"mongodb+srv://{username}:{password}@{cluster_url}/{db_name}"
        "?retryWrites=true&w=majority&appName=MongoDB6Stage"
    )

    try:
        client = MongoClient(connection_string, serverSelectionTimeoutMS=5000)
        client.admin.command("ping")  # Test the connection
        print("===> Connected to MongoDB Atlas successfully.")
    except Exception as e:
        raise Exception(f"Error connecting to MongoDB Atlas: {e}")
    return client


def count_automation_users_older_than_one_month(client):
    db_name = os.getenv("MONGO_DB_NAME", "GoHealthyUsers")
    collection_name = "users"

    db = client[db_name]
    collection = db[collection_name]

    cutoff_date = datetime.utcnow() - timedelta(days=30)

    query = {
        "fullname": {"$regex": "^Automation", "$options": "i"},
        "createdAt": {"$lt": cutoff_date}
    }

    automation_users_count = collection.count_documents(query)
    print(f"===> Number of Automation users older than one month: {automation_users_count}")


def delete_automation_users(client, days_old=30):
    db_name = os.getenv("MONGO_DB_NAME", "GoHealthyUsers")
    collection_name = "users"

    try:
        db = client[db_name]
        collection = db[collection_name]

        cutoff_date = datetime.utcnow() - timedelta(days=days_old)

        query = {
            "fullname": {"$regex": "^Automation", "$options": "i"},
            "createdAt": {"$lt": cutoff_date}
        }

        result = collection.delete_many(query)

        print(f"===> Deleted {result.deleted_count} user(s).")
    except PyMongoError as e:
        raise Exception(f"Error deleting automation users: {e}")
    except Exception as e:
        raise Exception(f"An unexpected error occurred during user deletion: {e}")
