# from pymongo import MongoClient
# from faker import Faker
# import time

# # Update the URI as per your MongoDB container settings
# MONGODB_URI = "mongodb://user:password@localhost:27017"  # Adjust as necessary

# def generate_fake_users(num_users=5000):
#     fake = Faker()
#     users = []
#     for _ in range(num_users):
#         # Generate a fake username and surname
#         username = fake.user_name()
#         surname = fake.last_name()
#         users.append({"username": username, "surname": surname})
#     return users

# def test_mongo_connection():
#     try:
#         # Connect to MongoDB
#         client = MongoClient(MONGODB_URI)
#         db = client['chat_microservice']  # Use your database name

#         # Attempt to fetch the list of collections to confirm connection
#         collections = db.list_collection_names()
#         print("MongoDB Connection Successful!")
#         print("Collections:", collections)

#         # Create a new collection (if it doesn't already exist) and insert data
#         users_collection = db['users']  # The collection where user data will be stored

#         # Generate 5000 fake users
#         fake_users = generate_fake_users(50000)

#         # Bulk insert the fake users into the users collection
#         result = users_collection.insert_many(fake_users)

#         # Print the inserted document IDs
#         print(f"Inserted {len(result.inserted_ids)} documents with IDs: {result.inserted_ids[:10]}")  # Displaying the first 10 IDs

#         # Fetch and display all documents in the users collection (optional)
#         for user in users_collection.find():
#             print(user)

#     except Exception as e:
#         print("MongoDB Connection Failed:", str(e))
#     finally:
#         client.close()

# def query_with_timing(surname):
#     try:
#         client = MongoClient(MONGODB_URI)
#         db = client['chat_microservice']
#         users_collection = db['users']

#         queries = [
#             {"first_name": "John"},
#             {"first_name": "Jane", "surname": "Smith"},
#             {"first_name": "Alice", "surname": "Johnson"},
#             { "surname": "Johnson"},
#             {"surname": "Lopez"},
#         ]

#         # Count all documents in the collection
#         total_entries = users_collection.count_documents({})
        
#         print(f"Total number of entries in the 'users' collection: {total_entries}")
        
#         # Record start time
#         start_time = time.time()
        
#         # Perform the query
#         # query = {"surname": surname}
#         count = 0
#         # for query in queries:
#         users = users_collection.find(queries[3])
#         count += users_collection.count_documents(queries[3])
        
#         # Measure the time taken for the query
#         query_time = time.time() - start_time
        
#         # Count the number of documents matching the query
#         # count = users_collection.count_documents(query)
        
#         # Print the users (if any) and the time taken
#         # if count > 0:
#         #     for user in users:
#         #         print(f"User found: {user}")
#         # else:
#         #     print(f"No users found with surname: {surname}")
        
#         print(f"Query executed in {query_time:.4f} seconds")
#         print(f"Total number of matching documents: {count}")
        
#     except Exception as e:
#         print("MongoDB Query Failed:", str(e))
#     finally:
#         client.close()




# if __name__ == "__main__":
#     # test_mongo_connection()
#     query_with_timing("Lopez")  # Change the surname as needed
 

from pymongo import MongoClient
from faker import Faker
import time
from concurrent.futures import ThreadPoolExecutor
from pymongo import MongoClient, ASCENDING, DESCENDING
import random

# Update the URI as per your MongoDB container settings
MONGODB_URI = "mongodb://user:password@localhost:27017"  # Adjust as necessary


def generate_fake_users(num_users=5000):
    fake = Faker()
    users = []
    for _ in range(num_users):
        # Generate a fake username and surname
        username = fake.user_name()
        surname = fake.last_name()
        users.append({"username": username, "surname": surname})
    return users

def test_mongo_connection():
    try:
        # Connect to MongoDB
        client = MongoClient(MONGODB_URI)
        db = client['chat_microservice']  # Use your database name

        # Attempt to fetch the list of collections to confirm connection
        collections = db.list_collection_names()
        print("MongoDB Connection Successful!")
        print("Collections:", collections)

        # Create a new collection (if it doesn't already exist) and insert data
        users_collection = db['users']  # The collection where user data will be stored

        # Generate 5000 fake users
        fake_users = generate_fake_users(700000)

        # Bulk insert the fake users into the users collection
        result = users_collection.insert_many(fake_users)

        # # # Initialize Faker to generate data
        fake = Faker()

        users = users_collection.find()  # Retrieve all users from the collection

        for user in users:
            # Check if 'username' field already exists
            if 'first_name' not in user:
                # Generate a unique username
                username = fake.first_name()

                # Update the user document with the new 'username'
                users_collection.update_one(
                    {"_id": user["_id"]},
                    {"$set": {"first_name": username}}
                )

        print("Successfully added 'username' to all existing users.")

        # Print the inserted document IDs
        print(f"Inserted {len(result.inserted_ids)} documents with IDs: {result.inserted_ids[:10]}")  # Displaying the first 10 IDs

        # Fetch and display all documents in the users collection (optional)
        for user in users_collection.find():
            print(user)

    except Exception as e:
        print("MongoDB Connection Failed:", str(e))
    finally:
        client.close()

# def query_count(query, collection):
#     return collection.count_documents(query)

# def query_with_timing():
#     print("hello")
#     try:
#         client = MongoClient(MONGODB_URI)
#         db = client['chat_microservice']
#         users_collection = db['users']

#         print(users_collection)

#         # Create a composite index
#         # users_collection.drop_indexes()
#         # users_collection.create_index([("first_name", ASCENDING), ("surname", ASCENDING)])
#         # users_collection.create_index([("surname", ASCENDING), ("first_name", ASCENDING)])

#         print("Composite index on 'surname' and 'first_name' created.")
#         indexes = users_collection.list_indexes()

#         # Iterate through the indexes and print their details
#         for index in indexes:
#             print(index)

# #         # Count all documents in the collection
#         total_entries = users_collection.count_documents({})
        
#         print(f"Total number of entries in the 'users' collection: {total_entries}")

#         total_count = 0  # To keep track of total matching documents across all queries

#         first_names = users_collection.distinct('first_name')
#         surnames_all = users_collection.distinct('surname')

#         print(str(len(first_names)) + str("  count of first names") )
#         print(str(len(surnames_all))+ str("  count of second names") )


#         queries = []
#         for i in range(500000):
#             random_first_name = first_names[len(first_names)-1]
#             # random_first_name = first_names[i%len(first_names)]
#             random_surname = surnames_all[i%len(surnames_all)]
#             # random_first_name = random.choice(first_names)
#             # random_surname = random.choice(surnames_all)
#             queries.append({"first_name": random_first_name, "surname": random_surname})

#         start_time = time.time()  # Start time for all queries
        
#         # for idx, query in enumerate(queries):
#         #     query_start_time = time.time()  # Start time for this query
            
#             # Debugging: Print query
#             # print(f"Executing Query {idx + 1}: {query}")
            
#             # Execute the query and count matching documents
#             # count = users_collection.count_documents(query)
#             # if count == 0:
#             #     print("No matching documents found for query:", query)
#             # else:
#             #     print(f"Number of matching documents: {count}")
#             # total_count += count
            
#             # query_end_time = time.time()  # End time for this query
#             # explanation = users_collection.find(query).explain()
#             # query_execution_time = query_end_time - query_start_time
#             # print(explanation)
            
#             # Print query execution time
#             # print(f"Query {idx + 1} executed in {query_execution_time:.4f} seconds")
#             # print('\n')
#         # start_time = time.time()  # Start total execution timer

#         # Execute queries in parallel using ThreadPoolExecutor
#         with ThreadPoolExecutor() as executor:
#             results = list(executor.map(query_count, queries, [users_collection]*len(queries)))

#         total_count = sum(results)
        
#         total_execution_time = time.time() - start_time  # Total time for all queries
#         print(f"\nTotal execution time for all queries: {total_execution_time:.4f} seconds")
#         print(f"Total number of matching documents across all queries: {total_count}")

#     except Exception as e:
#         print("MongoDB Query Failed:", str(e))
#     finally:
#         client.close()

# MongoDB query function
# def query_count(query, collection):
#     try:
#         # Perform the count operation
#         return collection.count_documents(query)
#     except Exception as e:
#         print(f"Error with query {query}: {e}")
#         return 0

# def query_with_timing():
#     try:
#         # Use a reusable MongoDB client
#         client = MongoClient(MONGODB_URI, maxPoolSize=100)  # Adjust maxPoolSize as needed
#         db = client['chat_microservice']
#         users_collection = db['users']

#         print(users_collection)

#         # Check for existing indexes and create if necessary
#         existing_indexes = list(users_collection.list_indexes())
#         # if not any(index['key'] == [("first_name", 1), ("surname", 1)] for index in existing_indexes):
#         #     users_collection.create_index([("first_name", ASCENDING), ("surname", ASCENDING)])
#         #     print("Composite index on 'first_name' and 'surname' created.")

#         # Count all documents in the collection
#         total_entries = users_collection.count_documents({})
#         print(f"Total number of entries in the 'users' collection: {total_entries}")

#         # Get distinct values for query fields
#         first_names = users_collection.distinct('first_name')
#         surnames_all = users_collection.distinct('surname')

#         print(f"{len(first_names)} distinct first names.")
#         print(f"{len(surnames_all)} distinct surnames.")

#         # Function to generate random queries
#         def generate_query(i):
#             random_first_name = first_names[i % len(first_names)]
#             random_surname = surnames_all[i % len(surnames_all)]
#             return {"first_name": random_first_name, "surname": random_surname}

#         # Measure execution time
#         start_time = time.time()

#         # Use ThreadPoolExecutor to process queries
#         with ThreadPoolExecutor(max_workers=50) as executor:  # Adjust max_workers as needed
#             results = list(executor.map(
#                 query_count,
#                 (generate_query(i) for i in range(500000)),  # Generate queries dynamically
#                 [users_collection] * 500000
#             ))

#         # Aggregate results
#         total_count = sum(results)
#         total_execution_time = time.time() - start_time

#         print(f"\nTotal execution time for all queries: {total_execution_time:.4f} seconds")
#         print(f"Total number of matching documents across all queries: {total_count}")

#     except Exception as e:
#         print(f"MongoDB Query Failed: {e}")
#     finally:
#         # Ensure the MongoClient is closed
#         client.close()

from itertools import islice
# def query_count(query, collection):
#     """Count documents matching the query."""
#     try:
#         return collection.count_documents(query)
#     except Exception as e:
#         print(f"Error with query {query}: {e}")
#         return 0

# def generate_queries(first_names, surnames, total_queries):
#     """Generate queries efficiently in a lazy manner."""
#     first_names_len = len(first_names)
#     surnames_len = len(surnames)
#     for i in range(total_queries):
#         yield {
#             "first_name": first_names[i % first_names_len],
#             "surname": surnames[i % surnames_len]
#         }

# def query_with_timing():
#     """Optimized query processing with MongoDB."""
#     try:
#         client = MongoClient(MONGODB_URI, maxPoolSize=100)
#         db = client['chat_microservice']
#         users_collection = db['users']

#         # Ensure necessary index exists
#         existing_indexes = list(users_collection.list_indexes())
#         if not any(index['key'] == [("first_name", 1), ("surname", 1)] for index in existing_indexes):
#             users_collection.create_index([("first_name", ASCENDING), ("surname", ASCENDING)])
#             print("Composite index on 'first_name' and 'surname' created.")

#         # Get collection statistics
#         total_entries = users_collection.count_documents({})
#         print(f"Total number of entries in the 'users' collection: {total_entries}")

#         # Get distinct field values
#         first_names = users_collection.distinct('first_name')
#         surnames_all = users_collection.distinct('surname')

#         print(f"{len(first_names)} distinct first names.")
#         print(f"{len(surnames_all)} distinct surnames.")

#         total_queries = 500_000
#         batch_size = 10_000  # Process in smaller batches for memory efficiency
#         start_time = time.time()

#         total_count = 0
#         num_batches = (total_queries + batch_size - 1) // batch_size  # Ceiling division

#         for batch_index in range(num_batches):
#             print(f"Processing batch {batch_index + 1} of {num_batches}...")
#             batch_queries = list(islice(generate_queries(first_names, surnames_all, total_queries), batch_size))

#             # Execute queries in parallel with ThreadPoolExecutor
#             with ThreadPoolExecutor(max_workers=50) as executor:
#                 results = executor.map(query_count, batch_queries, [users_collection] * len(batch_queries))
#             total_count += sum(results)

#         total_execution_time = time.time() - start_time
#         print(f"\nTotal execution time: {total_execution_time:.4f} seconds")
#         print(f"Total number of matching documents across all queries: {total_count}")

#     except Exception as e:
#         print(f"MongoDB Query Failed: {e}")
#     finally:
#         client.close()

# def query_count(query, collection):
#     """Count documents matching the query."""
#     return collection.count_documents(query)

# def query_with_timing():
#     """Optimized query processing with MongoDB."""
#     try:
#         client = MongoClient(MONGODB_URI, maxPoolSize=200)  # Increase connection pool size
#         db = client['chat_microservice']
#         users_collection = db['users']

#         # Ensure necessary index exists
#         users_collection.create_index([("first_name", ASCENDING), ("surname", ASCENDING)], background=True)

#         # Fetch distinct field values
#         first_names = users_collection.distinct('first_name')
#         surnames_all = users_collection.distinct('surname')

#         print(f"Distinct first names: {len(first_names)}")
#         print(f"Distinct surnames: {len(surnames_all)}")

#         # Generate queries
#         total_queries = 500_000
#         queries = (
#             {"first_name": first_names[random.randint(0, len(first_names) - 1)],
#              "surname": surnames_all[random.randint(0, len(surnames_all) - 1)]}
#             for _ in range(total_queries)
#         )

#         # Process queries in batches
#         batch_size = 50_000  # Larger batch size to reduce overhead
#         total_count = 0
#         start_time = time.time()

#         def batch_process(batch):
#             with ThreadPoolExecutor(max_workers=50) as executor:
#                 results = executor.map(query_count, batch, [users_collection] * len(batch))
#             return sum(results)

#         batch = []
#         for i, query in enumerate(queries):
#             batch.append(query)
#             if len(batch) == batch_size or i == total_queries - 1:
#                 total_count += batch_process(batch)
#                 batch.clear()

#         total_execution_time = time.time() - start_time
#         print(f"\nTotal execution time: {total_execution_time:.4f} seconds")
#         print(f"Total number of matching documents across all queries: {total_count}")

#     except Exception as e:
#         print(f"MongoDB Query Failed: {e}")
#     finally:
#         client.close()

# Function to count documents in batches
def batch_queries(queries, batch_size):
    for i in range(0, len(queries), batch_size):
        yield queries[i:i + batch_size]

# Function to count documents in a batch using $or
def query_count_worker(batch, collection):
    return collection.count_documents({"$or": batch})

# Main function to execute queries and measure execution time
def query_with_timing():
    try:
        # MongoDB client and collection setup
        client = MongoClient(MONGODB_URI)
        db = client['chat_microservice']
        users_collection = db['users']

        # Create the composite index
        # users_collection.create_index([("first_name", 1), ("surname", 1)])

        # Get distinct values for first_name and surname
        first_names = users_collection.distinct('first_name')
        surnames_all = users_collection.distinct('surname')

        print(f"Total first names: {len(first_names)}")
        print(f"Total surnames: {len(surnames_all)}")

        # Generate queries by combining first_name and surname
        queries = []
        for i in range(500000):  # Adjust the number of queries as needed
            random_first_name = first_names[i % len(first_names)]
            random_surname = surnames_all[i % len(surnames_all)]
            queries.append({"first_name": random_first_name, "surname": random_surname})

        # Batch the queries into groups of 500 (or any appropriate batch size)
        batch_size = 500
        batches = list(batch_queries(queries, batch_size))

        # Measure execution time
        start_time = time.time()

        # Execute batched queries in parallel using ThreadPoolExecutor
        with ThreadPoolExecutor() as executor:
            results = executor.map(query_count_worker, batches, [users_collection] * len(batches))

        # Sum up the results
        total_count = sum(results)

        # Measure total execution time
        total_execution_time = time.time() - start_time
        print(f"Total execution time for all queries: {total_execution_time:.4f} seconds")
        print(f"Total number of matching documents across all queries: {total_count}")

    except Exception as e:
        print(f"MongoDB Query Failed: {str(e)}")
    finally:
        client.close()


# BATCH_SIZE = 10000
# MAX_THREADS = 200  # Dynamic thread pool size, can be adjusted

# def query_count(query, collection):
#     return collection.count_documents(query)

# def create_client():
#     """Create a MongoDB client with connection pooling enabled."""
#     return MongoClient(MONGODB_URI, maxPoolSize=10)

# def fetch_distinct_values(collection):
#     """Fetch distinct values for 'first_name' and 'surname'."""
#     first_names = collection.distinct('first_name')
#     surnames = collection.distinct('surname')
#     return first_names, surnames

# def batch_queries(first_names, surnames, batch_size):
#     """Generate query batches dynamically."""
#     queries = []
#     for _ in range(batch_size):
#         random_first_name = random.choice(first_names)
#         random_surname = random.choice(surnames)
#         queries.append({"first_name": random_first_name, "surname": random_surname})
#     return queries

# def process_batch(queries, users_collection):
#     """Process a batch of queries and return the count results."""
#     results = []
#     for query in queries:
#         result = query_count(query, users_collection)
#         results.append(result)
#     return sum(results)

# def query_with_timing():
#     """Main function to execute the optimized queries."""
#     try:
#         # Initialize MongoDB client with connection pooling
#         client = create_client()
#         db = client['chat_microservice']
#         users_collection = db['users']

#         # Ensure index is created
#         users_collection.create_index([("surname", ASCENDING), ("first_name", ASCENDING)])
#         print("Composite index on 'surname' and 'first_name' created.")

#         # Fetch distinct values
#         first_names, surnames = fetch_distinct_values(users_collection)
#         print(f"Distinct 'first_name' count: {len(first_names)}")
#         print(f"Distinct 'surname' count: {len(surnames)}")

#         total_count = 0  # Total matching documents count
#         total_execution_time = 0  # Total execution time

#         # Generate queries in dynamic batches
#         for batch_start in range(0, 500000, BATCH_SIZE):
#             queries = batch_queries(first_names, surnames, BATCH_SIZE)
#             start_time = time.time()  # Start time for batch

#             # Execute queries in parallel using ThreadPoolExecutor
#             with ThreadPoolExecutor(max_workers=MAX_THREADS) as executor:
#                 batch_results = executor.submit(process_batch, queries, users_collection)
#                 total_count += batch_results.result()  # Accumulate result

#             batch_execution_time = time.time() - start_time  # Time taken for the batch
#             total_execution_time += batch_execution_time
#             print(f"Batch {batch_start // BATCH_SIZE + 1} executed in {batch_execution_time:.4f} seconds.")

#         print(f"\nTotal execution time for all queries: {total_execution_time:.4f} seconds")
#         print(f"Total number of matching documents across all queries: {total_count}")

#     except Exception as e:
#         print(f"MongoDB Query Failed: {str(e)}")
#     finally:
#         client.close()  # Close


if __name__ == "__main__":
    query_with_timing()
    


# def query_with_timing(surname):
#     try:
#         client = MongoClient(MONGODB_URI)
#         db = client['chat_microservice']
#         users_collection = db['users']

#         # Count all documents in the collection
#         total_entries = users_collection.count_documents({})
        
#         print(f"Total number of entries in the 'users' collection: {total_entries}")
        
#         # Query to find all users with the surname 'Lopez'
#         # query = {"last_name": "Le"}

#         # # Execute the query
#         # cursor = users_collection.find("")

#         # # Print results
#         # print("Users with last_name 'Lopez':")
#         # for user in cursor:
#         #     print(user)

#         # Optional: Count the documents
#         # count = users_collection.count_documents(query)
#         # print(f"Total number of users with last_name 'Lopez': {count}")

#         # List all indexes in the collection
#         # users_collection.drop_indexes()
#         # indexes = users_collection.list_indexes()

#         # Iterate through the indexes and print their details
#         # for index in indexes:
#         #     print(index)

#         # Perform the query
#         queries = [
#             {"surname": "Smith"},
#             {"surname": "Johnson"},
#             {"surname": "Williams"},
#             {"surname": "Jones"},
#             {"surname": "Brown"},
#             {"surname": "Miller"},
#             {"surname": "Davis"},
#             {"surname": "Garcia"},
#             {"surname": "Rodriguez"},
#             {"surname": "Martinez"},
#             {"surname": "Wilson"},
#             {"surname": "Anderson"},
#             {"surname": "Taylor"},
#             {"surname": "Thomas"},
#             {"surname": "Hernandez"},
#             {"surname": "Moore"},
#             {"surname": "Martin"},
#             {"surname": "Thompson"},
#             {"surname": "Jackson"},
#             {"surname": "White"},
#             {"surname": "Lopez"},
#             {"surname": "Lee"},
#             {"surname": "Gonzalez"},
#             {"surname": "Harris"},
#             {"surname": "Clark"},
#             {"surname": "Lewis"},
#             {"surname": "Robinson"},
#             {"surname": "Walker"},
#             {"surname": "Perez"},
#             {"surname": "Hall"},
#             {"surname": "Young"},
#             {"surname": "Wright"},
#             {"surname": "Allen"},
#             {"surname": "Sanchez"},
#             {"surname": "King"},
#             {"surname": "Adams"},
#             {"surname": "Scott"},
#             {"surname": "Green"},
#             {"first_name": "Michael"},
#             {"first_name": "David"},
#             {"first_name": "James"},
#             {"first_name": "Jennifer"},
#             {"first_name": "John"},
#             {"first_name": "Christopher"},
#             {"first_name": "Robert"},
#             {"first_name": "Matthew"},
#             {"first_name": "Jessica"},
#             {"first_name": "William"},
#             {"first_name": "Daniel"},
#             {"first_name": "Lisa"},
#             {"first_name": "Joseph"},
#             {"first_name": "Brian"},
#             {"first_name": "Kimberly"},
#             {"first_name": "Jason"},
#             {"first_name": "Michelle"},
#             {"first_name": "Amanda"},
#             {"first_name": "Joshua"},
#             {"first_name": "Ashley"},
#             {"first_name": "Kevin"},
#             {"first_name": "Melissa"},
#             {"first_name": "Mark"},
#             {"first_name": "Elizabeth"},
#             {"first_name": "Sarah"},
#             {"first_name": "Richard"},
#             {"first_name": "Mary"},
#             {"first_name": "Thomas"},
#             {"first_name": "Stephanie"},
#             {"first_name": "Anthony"},
#             {"first_name": "Andrew"},
#             {"first_name": "Steven"},
#             {"first_name": "Amy"},
#             {"first_name": "Jeffrey"},
#             {"first_name": "Timothy"},
#             {"first_name": "Eric"},
#             {"first_name": "Angela"},
#             {"first_name": "Nicole"},
#             {"first_name": "Ryan"},
#             {"first_name": "Heather"},
#             {"first_name": "Laura"},
#             {"first_name": "Charles"},
#             {"first_name": "Scott"},
#             {"first_name": "Rebecca"},
#             {"first_name": "Justin"},
#             {"first_name": "Jonathan"},
#             {"first_name": "Nicholas"},
#             {"first_name": "Karen"},
#             {"first_name": "Brandon"},
#             {"first_name": "Kelly"},
#             {"first_name": "Paul"},
#             {"first_name": "Emily"},
#             {"first_name": "Susan"},
#             {"first_name": "Christina"},
#             {"first_name": "Rachel"},
#             {"first_name": "Kenneth"},
#             {"first_name": "Patricia"},
#             {"first_name": "Julie"},
#             {"first_name": "Jacob"},
#             {"first_name": "Samantha"},
#             {"first_name": "Cynthia"},
#             {"first_name": "Gregory"},
#             {"first_name": "Stephen"},
#             {"first_name": "Christine"},
#             {"first_name": "Megan"},
#             {"first_name": "Patrick"},
#             {"first_name": "Brittany"},
#             {"first_name": "Adam"},
#             {"first_name": "Andrea"},
#             {"first_name": "Lauren"},
#             {"first_name": "Amber"},
#             {"first_name": "Aaron"},
#             {"first_name": "Danielle"},
#             {"first_name": "Tiffany"},
#             {"first_name": "Benjamin"},
#             {"first_name": "Sandra"},
#             {"first_name": "Tammy"},
#             {"first_name": "Maria"},
#             {"first_name": "Linda"},
#             {"first_name": "Katherine"},
#             {"first_name": "Kyle"},
#             {"first_name": "Crystal"},
#             {"first_name": "Jeremy"},
#             {"first_name": "Lori"},
#             {"first_name": "Pamela"},
#             {"first_name": "Shannon"},
#             {"first_name": "Ronald"},
#             {"first_name": "Tyler"},
#             {"first_name": "Edward"},
#             {"first_name": "Brenda"},
#             {"first_name": "Zachary"},
#             {"first_name": "Donna"},
#             {"first_name": "Sara"},
#             {"first_name": "Deborah"},
#             {"first_name": "Donald"},
#             {"first_name": "Victoria"},
#             {"first_name": "Sean"},
#             {"first_name": "Teresa"},
#             {"first_name": "Jose"},
#             {"first_name": "Nathan"},
#             {"first_name": "Tina"},
#             {"first_name": "Erin"},
#             {"first_name": "Alexander"},
#             {"first_name": "Tracy"},
#             {"first_name": "Gary"},
#             {"first_name": "Nancy"},
#             {"first_name": "Kathleen"},
#             {"first_name": "Barbara"},
#             {"first_name": "Dawn"},
#             {"first_name": "Jamie"},
#             {"first_name": "Samuel"},
#             {"first_name": "Courtney"},
#             {"first_name": "April"},
#             {"first_name": "Sharon"},
#             {"first_name": "Bryan"},
#             {"first_name": "Kayla"}
#         ]

#         total_count = 0  # To keep track of total matching documents across all queries
        
#         start_time = time.time()  # Start time for all queries

        
#         for idx, query in enumerate(queries):
#             query_start_time = time.time()  # Start time for this query
            
#             # Debugging: Print query
#             # print(f"Executing Query {idx + 1}: {query}")
            
#             # Execute the query and count matching documents
#             count = users_collection.count_documents(query)
#             # if count == 0:
#             #     print("No matching documents found for query:", query)
#             # else:
#             #     print(f"Number of matching documents: {count}")
#             total_count += count
            
#             query_end_time = time.time()  # End time for this query
#             query_execution_time = query_end_time - query_start_time
            
#             # Print query execution time
#             # print(f"Query {idx + 1} executed in {query_execution_time:.4f} seconds")
#             # print('\n')
        
#         total_execution_time = time.time() - start_time  # Total time for all queries
#         print(f"\nTotal execution time for all queries: {total_execution_time:.4f} seconds")
#         print(f"Total number of matching documents across all queries: {total_count}")


#         # #Print the users (if any) and the time taken
#         # if count > 0:
#         #     for user in users_collection:
#         #         print(f"User found: {user}")
#         # else:
#         #     print(f"No users found with surname: {surname}")

#         # Aggregation pipeline
#         # pipeline = [
#         #     {"$match": {"first_name": {"$ne": None}}},  # Exclude documents where last_name is None
#         #     {"$group": {"_id": "$first_name", "count": {"$sum": 1}}},  # Group by last_name and count occurrences
#         #     {"$sort": {"count": -1}}  # Sort by frequency in descending order
#         # ]

#         # # Execute the aggregation
#         # results = users_collection.aggregate(pipeline)

#         # # Print the results
#         # print("Surnames by frequency:")
#         # for result in results:
#         #     print(f"first_name: {result['_id']}, Frequency: {result['count']}")

#     except Exception as e:
#         print("MongoDB Query Failed:", str(e))
#     finally:
#         client.close()








# Main Thread: Prepares query list and starts ThreadPoolExecutor
#      |
#      v
# ThreadPoolExecutor spawns threads: T1, T2, ..., TN (N = number of CPU cores or pool size)
#      |
# Each thread (T1, T2, ...) executes `query_count` for its assigned query:
#      - Connect to MongoDB
#      - Send query
#      - Wait for I/O (releases GIL)
#      - Retrieve result
#      - Repeat for the next query
#      |
#      v
# Main Thread: Waits for all threads, aggregates results, and shuts down ThreadPoolExecutor




# def query_count(query, collection):
#     return collection.count_documents(query)

# def query_with_timing():
#     print("hello")
#     try:
#         client = MongoClient(MONGODB_URI)
#         db = client['chat_microservice']
#         users_collection = db['users']

#         print(users_collection)

#         # Create a composite index
#         # users_collection.drop_indexes()
#         users_collection.create_index([("first_name", ASCENDING), ("surname", ASCENDING)])
#         # users_collection.create_index([("surname", ASCENDING), ("first_name", ASCENDING)])

#         print("Composite index on 'surname' and 'first_name' created.")
#         indexes = users_collection.list_indexes()

#         # Iterate through the indexes and print their details
#         for index in indexes:
#             print(index)

# #         # Count all documents in the collection
#         total_entries = users_collection.count_documents({})
        
#         print(f"Total number of entries in the 'users' collection: {total_entries}")

#         total_count = 0  # To keep track of total matching documents across all queries

#         first_names = users_collection.distinct('first_name')
#         surnames_all = users_collection.distinct('surname')

#         print(str(len(first_names)) + str("  count of first names") )
#         print(str(len(surnames_all))+ str("  count of second names") )


#         queries = []
#         for i in range(500000):
#             random_first_name = first_names[i%len(first_names)]
#             random_surname = surnames_all[i%len(surnames_all)]
#             # random_first_name = random.choice(first_names)
#             # random_surname = random.choice(surnames_all)
#             queries.append({"first_name": random_first_name, "surname": random_surname})
#             # queries.append({"first_name": random_first_name})

#         start_time = time.time()  # Start time for all queries

#         # Execute queries in parallel using ThreadPoolExecutor
#         with ThreadPoolExecutor() as executor:
#             results = list(executor.map(query_count, queries, [users_collection]*len(queries)))

#         total_count = sum(results)
        
#         total_execution_time = time.time() - start_time  # Total time for all queries
#         print(f"\nTotal execution time for all queries: {total_execution_time:.4f} seconds")
#         print(f"Total number of matching documents across all queries: {total_count}")

#     except Exception as e:
#         print("MongoDB Query Failed:", str(e))
#     finally:
#         client.close()