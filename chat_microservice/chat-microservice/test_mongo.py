from pymongo import MongoClient

# Update the URI as per your MongoDB container settings
MONGODB_URI = "mongodb://user:password@localhost:27017"  # Adjust as necessary

def test_mongo_connection():
    try:
        client = MongoClient(MONGODB_URI)
        db = client['chat_microservice']  # Use your database name
        # Attempt to fetch the list of collections
        collections = db.list_collection_names()
        print("MongoDB Connection Successful!")
        print("Collections:", collections)
    except Exception as e:
        print("MongoDB Connection Failed:", str(e))
    finally:
        client.close()

if __name__ == "__main__":
    test_mongo_connection()

