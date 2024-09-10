import os
import logging
import pymongo
from pymongo.errors import BulkWriteError, DuplicateKeyError

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Constants for environment variables
MONGO_USER_KEY = 'MONGO_USER'
MONGO_PASSWORD_KEY = 'MONGO_PASSWORD'
MONGO_CLUSTER_KEY = 'MONGO_CLUSTER'
MONGO_DB_NAME_KEY = 'MONGO_DB_NAME'

def get_mongo_credentials() -> dict:
    """
    Retrieve MongoDB credentials from environment variables.
    Raises:
        EnvironmentError: If any required environment variable is missing.
    Returns:
        dict: MongoDB connection parameters.
    """
    mongo_user = os.getenv(MONGO_USER_KEY)
    mongo_password = os.getenv(MONGO_PASSWORD_KEY)
    mongo_cluster = os.getenv(MONGO_CLUSTER_KEY)
    mongo_db_name = os.getenv(MONGO_DB_NAME_KEY)
    
    if not all([mongo_user, mongo_password, mongo_cluster, mongo_db_name]):
        raise EnvironmentError("One or more MongoDB environment variables are missing")
    
    return {
        "user": mongo_user,
        "password": mongo_password,
        "cluster": mongo_cluster,
        "db_name": mongo_db_name
    }

def get_mongo_collection(collection_name: str):
    """
    Connect to MongoDB and return the specified collection.
    Args:
        collection_name (str): The name of the collection to retrieve.
    Returns:
        pymongo.collection.Collection: MongoDB collection.
    """
    credentials = get_mongo_credentials()
    mongo_uri = (
        f"mongodb+srv://{credentials['user']}:{credentials['password']}"
        f"@{credentials['cluster']}/{credentials['db_name']}?retryWrites=true&w=majority"
    )
    client = pymongo.MongoClient(mongo_uri)
    db = client[credentials['db_name']]
    return db[collection_name]

def insert_into_mongodb(collection_name: str, filtered_candidates: list, batch_size: int = 1000):
    """
    Insert filtered candidates into MongoDB in batches.
    Args:
        collection_name (str): The name of the collection where candidates will be inserted.
        filtered_candidates (list): List of candidate documents to insert.
        batch_size (int): Number of documents to insert per batch.
    """
    try:
        collection = get_mongo_collection(collection_name)
        
        if filtered_candidates:
            for i in range(0, len(filtered_candidates), batch_size):
                batch = filtered_candidates[i:i + batch_size]
                result = collection.insert_many(batch)
                logging.info(f"Inserted {len(result.inserted_ids)} candidates into MongoDB.")
        else:
            logging.info("No candidates to insert.")
    except BulkWriteError as e:
        logging.error(f"Bulk write error: {e}")
    except DuplicateKeyError as e:
        logging.error(f"Duplicate key error: {e}")
    except Exception as e:
        logging.error(f"An error occurred: {e}")
