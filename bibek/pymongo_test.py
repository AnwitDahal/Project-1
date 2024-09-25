import os
from pymongo import MongoClient, errors
from dotenv import load_dotenv
from datetime import datetime

# Load environment variables from the .env file
load_dotenv()

# Get MongoDB URI from the environment variable
mongo_uri = os.getenv("MONGO_URI")

# MongoDB connection setup using the connection string from the .env file
try:
    client = MongoClient(mongo_uri)
    # Attempt to get server information
    client.server_info()  # This line checks the connection
    db = client['test']  # Correct database name
    collection = db['kathmandu_aqi']  # Collection name
    print("Connected to MongoDB successfully")
except errors.ConnectionError as e:
    print(f"Failed to connect to MongoDB: {e}")
    exit(1)
except errors.PyMongoError as e:
    print(f"Failed to retrieve server information: {e}")
    exit(1)

# Dummy data for AQI of Kathmandu (with AQI range: low and high)
aqi_data = [
    {"date": datetime(2024, 9, 22), "day": "Sunday", "aqi": {"low": 145, "high": 155}, "temperature": 25, "location": "Kathmandu"},
    {"date": datetime(2024, 9, 23), "day": "Monday", "aqi": {"low": 135, "high": 145}, "temperature": 26, "location": "Kathmandu"},
    {"date": datetime(2024, 9, 24), "day": "Tuesday", "aqi": {"low": 125, "high": 135}, "temperature": 27, "location": "Kathmandu"},
    {"date": datetime(2024, 9, 25), "day": "Wednesday", "aqi": {"low": 130, "high": 140}, "temperature": 24, "location": "Kathmandu"},
    {"date": datetime(2024, 9, 26), "day": "Thursday", "aqi": {"low": 140, "high": 150}, "temperature": 25, "location": "Kathmandu"},
    {"date": datetime(2024, 9, 27), "day": "Friday", "aqi": {"low": 155, "high": 165}, "temperature": 28, "location": "Kathmandu"},
    {"date": datetime(2024, 9, 28), "day": "Saturday", "aqi": {"low": 150, "high": 160}, "temperature": 29, "location": "Kathmandu"}
]

# Attempt to insert the documents into the collection
try:
    result = collection.insert_many(aqi_data)
    print("Data inserted successfully")
    print("Inserted document IDs:", result.inserted_ids)
except errors.PyMongoError as e:
    print(f"Failed to insert data into MongoDB: {e}")

