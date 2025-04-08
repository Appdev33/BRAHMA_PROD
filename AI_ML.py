from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import Chroma
from langchain.chat_models import ChatOpenAI
from langchain.retrievers import BM25Retriever, EnsembleRetriever
from langchain_core.prompts import ChatPromptTemplate
import requests

# Load Embedding Model
EMBED_MODEL = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2",
    encode_kwargs={"normalize_embeddings": True},
    model_kwargs={"device": 'cpu'}
)

# Load LLM with Streaming Support
api_key = "your_api_key_here"
llm = ChatOpenAI(
    model="gpt-35-turbo",
    base_url="https://cxai-playground.cisco.com",
    api_key=api_key,
    streaming=True  # Enables real-time response streaming
)

# Query Refinement using LLM
query_refinement_prompt = ChatPromptTemplate.from_template(
    """
    You are a network engineer optimizing a search query for retrieving network configurations. 
    Refine the user query into a concise search query.
    
    User Query: {user_query}
    """
)

def refine_query(user_query):
    refined_query = llm.invoke(query_refinement_prompt.format(user_query=user_query))
    return refined_query.content.strip()

# Hybrid Search (BM25 + Vector Search)
def query_data(database_name, res_count):
    # BM25 Retriever
    bm25_retriever = BM25Retriever.from_documents(documents)  # Load pre-split documents
    bm25_retriever.k = res_count
    
    # Vector Search Retriever
    vector_retriever = Chroma(
        collection_name=database_name,
        embedding_function=EMBED_MODEL
    ).as_retriever(search_kwargs={'k': res_count})
    
    # Hybrid Ensemble Retrieval
    retriever = EnsembleRetriever(
        retrievers=[bm25_retriever, vector_retriever],
        weights=[0.5, 0.5]  # Adjust lambda_mult
    )
    
    return retriever

# Multi-Query Expansion
def expand_query(original_query):
    expansion_prompt = ChatPromptTemplate.from_template(
        """
        Generate multiple versions of the following query to improve search accuracy:
        
        Original Query: {query}
        """
    )
    response = llm.invoke(expansion_prompt.format(query=original_query))
    return response.content.split("\n")

# Configuration Evaluation Prompt
self_review_prompt = ChatPromptTemplate.from_template(
    """
    Review the following network configuration:
    - Is it complete?
    - Is it optimized?
    - Are best practices followed?
    
    Configuration:
    {config_response}
    """
)

def review_response(config_response):
    return llm.invoke(self_review_prompt.format(config_response=config_response)).content

# Autonomic Deployment

def deploy_config(config, device_ip):
    url = f"http://{device_ip}/api/deploy"
    response = requests.post(url, json={"config": config})
    return response.json()

# Main Execution
if __name__ == "__main__":
    user_query = input("Enter your network query: ")
    
    # Step 1: Query Refinement
    refined_query_text = refine_query(user_query)
    
    # Step 2: Expand Queries
    expanded_queries = expand_query(refined_query_text)
    
    # Step 3: Hybrid Retrieval
    retriever = query_data("uc_auto_config_gen_test_db3", 2)
    retrieved_docs = []
    for q in expanded_queries:
        retrieved_docs.extend(retriever.get_relevant_documents(q))
    
    # Step 4: Remove Duplicates
    retrieved_docs = list({doc.page_content: doc for doc in retrieved_docs}.values())
    retrieved_text = "\n".join([doc.page_content for doc in retrieved_docs])
    
    # Step 5: Generate Configurations
    config_prompt = ChatPromptTemplate.from_template(
        """
        Generate the necessary network configurations based on the given information:
        
        Context:
        {context}
        
        User Input:
        {input}
        """
    )
    
    response = llm.invoke(config_prompt.format(context=retrieved_text, input=user_query))
    final_response = response.content.strip()
    
    # Step 6: Self-Evaluation of Config
    reviewed_config = review_response(final_response)
    
    print("\nGenerated Configuration:")
    print(reviewed_config)
    
    # Step 7: Optional Deployment
    deploy_choice = input("Do you want to deploy this config? (yes/no): ").strip().lower()
    if deploy_choice == "yes":
        device_ip = input("Enter device IP: ")
        result = deploy_config(reviewed_config, device_ip)
        print("✅ Deployment Result:", result)
