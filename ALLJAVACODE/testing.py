from pymongo import MongoClient
from pymongo.errors import OperationFailure
from concurrent.futures import ThreadPoolExecutor
import random
import time


# MongoDB URI
MONGODB_URI = "mongodb://user:password@localhost:27017"  # Adjust as necessary

# # Function to generate query batches
# def batch_queries(queries, batch_size):
#     for i in range(0, len(queries), batch_size):
#         yield queries[i:i + batch_size]

# # Optimized worker function to query MongoDB
# def query_count_worker(batch, collection):
#     return collection.count_documents({"$or": batch})

# # Optimized query execution function
# def query_with_timing():
#     try:
#         # MongoDB client and collection setup
#         client = MongoClient(MONGODB_URI)
#         db = client['chat_microservice']
#         users_collection = db['users']

#         # Fetch distinct values for 'first_name' and 'surname' and cache them
#         first_names = list(users_collection.distinct('first_name'))
#         surnames_all = list(users_collection.distinct('surname'))

#         if not first_names or not surnames_all:
#             raise ValueError("Empty 'first_name' or 'surname' values in the collection.")

#         print(f"Total first names: {len(first_names)}")
#         print(f"Total surnames: {len(surnames_all)}")

#         # Generate queries using random sampling for better randomness
#         total_queries = 500000
#         queries = [{"first_name": random.choice(first_names), "surname": random.choice(surnames_all)}
#                    for _ in range(total_queries)]

#         # Batch the queries to reduce MongoDB overhead
#         batch_size = 500  # Optimal batch size for MongoDB queries
#         batches = list(batch_queries(queries, batch_size))

#         # Start timer
#         start_time = time.time()

#         # Use ThreadPoolExecutor for parallel processing
#         with ThreadPoolExecutor(max_workers=10) as executor:
#             results = list(executor.map(query_count_worker, batches, [users_collection] * len(batches)))

#         # Calculate the total number of matching documents
#         total_count = sum(results)

#         # End timer
#         total_execution_time = time.time() - start_time
#         print(f"Total execution time for all queries: {total_execution_time:.4f} seconds")
#         print(f"Total number of matching documents across all queries: {total_count}")

#     except OperationFailure as e:
#         print(f"MongoDB Operation Error: {str(e)}")
#     except Exception as e:
#         print(f"An error occurred: {str(e)}")
#     finally:
#         # Ensure client is closed
#         client.close()


def batch_queries(queries, batch_size):
    """Helper function to batch queries."""
    for i in range(0, len(queries), batch_size):
        yield queries[i:i + batch_size]

def get_explain_report(collection, sample_query):
    """Run explain on a representative sample query to get index usage and execution stats."""
    explain_result = collection.find(sample_query).explain("executionStats")
    return explain_result

def query_count_worker(batch, collection):
    """Worker function to run queries in parallel and get the count."""
    total_count = 0
    total_execution_time = 0
    for query in batch:
        try:
            # Execute the query and get the count (no explain here, just the query)
            total_count += collection.count_documents(query)
        
        except Exception as e:
            print(f"Error executing query {query}: {str(e)}")

    return total_count, total_execution_time

def query_with_timing():
    try:
        # MongoDB client and collection setup
        client = MongoClient(MONGODB_URI)
        db = client['chat_microservice']
        users_collection = db['users']

        # Fetch distinct values for 'first_name' and 'surname' and cache them
        first_names = list(users_collection.distinct('first_name'))
        surnames_all = list(users_collection.distinct('surname'))

        if not first_names or not surnames_all:
            raise ValueError("Empty 'first_name' or 'surname' values in the collection.")

        print(f"Total first names: {len(first_names)}")
        print(f"Total surnames: {len(surnames_all)}")

        # Generate queries using random sampling for better randomness
        total_queries = 500000
        queries = [{"first_name": random.choice(first_names), "surname": random.choice(surnames_all)}
                   for _ in range(total_queries)]

        # Batch the queries to reduce MongoDB overhead
        batch_size = 500  # Optimal batch size for MongoDB queries
        batches = list(batch_queries(queries, batch_size))

        # Select a representative query to run explain on
        sample_query = queries[0]  # You can select any query here as a representative
        explain_report = get_explain_report(users_collection, sample_query)

        # Start timer for query execution
        start_time = time.time()

        # Use ThreadPoolExecutor for parallel processing of batches
        with ThreadPoolExecutor(max_workers=10) as executor:
            results = list(executor.map(query_count_worker, batches, [users_collection] * len(batches)))

        # Calculate the total number of matching documents and execution time
        total_count = sum(result[0] for result in results)
        total_execution_time = sum(result[1] for result in results)

        # End timer
        total_time_taken = time.time() - start_time

        # Output the overall execution details
        print(f"Total execution time for all queries: {total_time_taken:.4f} seconds")
        print(f"Total number of matching documents across all queries: {total_count}")
        print(f"Total execution time for all queries (sum of explain times): {total_execution_time} ms")

        # Output the explain report for index analysis
        print("\nExplain Report for the Sample Query:")
        print(explain_report)

    except OperationFailure as e:
        print(f"MongoDB Operation Error: {str(e)}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
    finally:
        # Ensure client is closed
        client.close()


if __name__ == "__main__":
    query_with_timing()
