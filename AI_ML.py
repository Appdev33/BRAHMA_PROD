# # from langchain.embeddings import HuggingFaceEmbeddings
# # from langchain.vectorstores import Chroma
# # from langchain.chat_models import ChatOpenAI
# # from langchain.retrievers import BM25Retriever, EnsembleRetriever
# # from langchain_core.prompts import ChatPromptTemplate
# # import requests

# # # Load Embedding Model
# # EMBED_MODEL = HuggingFaceEmbeddings(
# #     model_name="sentence-transformers/all-MiniLM-L6-v2",
# #     encode_kwargs={"normalize_embeddings": True},
# #     model_kwargs={"device": 'cpu'}
# # )

# # # Load LLM with Streaming Support
# # api_key = "your_api_key_here"
# # llm = ChatOpenAI(
# #     model="gpt-35-turbo",
# #     base_url="https://cxai-playground.cisco.com",
# #     api_key=api_key,
# #     streaming=True  # Enables real-time response streaming
# # )

# # # Query Refinement using LLM
# # query_refinement_prompt = ChatPromptTemplate.from_template(
# #     """
# #     You are a network engineer optimizing a search query for retrieving network configurations. 
# #     Refine the user query into a concise search query.
    
# #     User Query: {user_query}
# #     """
# # )

# # def refine_query(user_query):
# #     refined_query = llm.invoke(query_refinement_prompt.format(user_query=user_query))
# #     return refined_query.content.strip()

# # # Hybrid Search (BM25 + Vector Search)
# # def query_data(database_name, res_count):
# #     # BM25 Retriever
# #     bm25_retriever = BM25Retriever.from_documents(documents)  # Load pre-split documents
# #     bm25_retriever.k = res_count
    
# #     # Vector Search Retriever
# #     vector_retriever = Chroma(
# #         collection_name=database_name,
# #         embedding_function=EMBED_MODEL
# #     ).as_retriever(search_kwargs={'k': res_count})
    
# #     # Hybrid Ensemble Retrieval
# #     retriever = EnsembleRetriever(
# #         retrievers=[bm25_retriever, vector_retriever],
# #         weights=[0.5, 0.5]  # Adjust lambda_mult
# #     )
    
# #     return retriever

# # # Multi-Query Expansion
# # def expand_query(original_query):
# #     expansion_prompt = ChatPromptTemplate.from_template(
# #         """
# #         Generate multiple versions of the following query to improve search accuracy:
        
# #         Original Query: {query}
# #         """
# #     )
# #     response = llm.invoke(expansion_prompt.format(query=original_query))
# #     return response.content.split("\n")

# # # Configuration Evaluation Prompt
# # self_review_prompt = ChatPromptTemplate.from_template(
# #     """
# #     Review the following network configuration:
# #     - Is it complete?
# #     - Is it optimized?
# #     - Are best practices followed?
    
# #     Configuration:
# #     {config_response}
# #     """
# # )

# # def review_response(config_response):
# #     return llm.invoke(self_review_prompt.format(config_response=config_response)).content

# # # Autonomic Deployment

# # def deploy_config(config, device_ip):
# #     url = f"http://{device_ip}/api/deploy"
# #     response = requests.post(url, json={"config": config})
# #     return response.json()

# # # Main Execution
# # if __name__ == "__main__":
# #     user_query = input("Enter your network query: ")
    
# #     # Step 1: Query Refinement
# #     refined_query_text = refine_query(user_query)
    
# #     # Step 2: Expand Queries
# #     expanded_queries = expand_query(refined_query_text)
    
# #     # Step 3: Hybrid Retrieval
# #     retriever = query_data("uc_auto_config_gen_test_db3", 2)
# #     retrieved_docs = []
# #     for q in expanded_queries:
# #         retrieved_docs.extend(retriever.get_relevant_documents(q))
    
# #     # Step 4: Remove Duplicates
# #     retrieved_docs = list({doc.page_content: doc for doc in retrieved_docs}.values())
# #     retrieved_text = "\n".join([doc.page_content for doc in retrieved_docs])
    
# #     # Step 5: Generate Configurations
# #     config_prompt = ChatPromptTemplate.from_template(
# #         """
# #         Generate the necessary network configurations based on the given information:
        
# #         Context:
# #         {context}
        
# #         User Input:
# #         {input}
# #         """
# #     )
    
# #     response = llm.invoke(config_prompt.format(context=retrieved_text, input=user_query))
# #     final_response = response.content.strip()
    
# #     # Step 6: Self-Evaluation of Config
# #     reviewed_config = review_response(final_response)
    
# #     print("\nGenerated Configuration:")
# #     print(reviewed_config)
    
# #     # Step 7: Optional Deployment
# #     deploy_choice = input("Do you want to deploy this config? (yes/no): ").strip().lower()
# #     if deploy_choice == "yes":
# #         device_ip = input("Enter device IP: ")
# #         result = deploy_config(reviewed_config, device_ip)
# #         print("✅ Deployment Result:", result)


# from langchain.embeddings import HuggingFaceEmbeddings
# from langchain.vectorstores import Chroma
# from langchain.chat_models import ChatOpenAI
# from langchain_core.prompts import ChatPromptTemplate
# from langchain.retrievers import BM25Retriever
# from langchain_core.memory import ConversationBufferMemory
# from langchain.agents import initialize_agent, AgentType
# from langchain.agents.tools import Tool
# from langchain.chains import LLMChain

# # Step 1: Initialize Embeddings & LLM
# EMBED_MODEL = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
# llm = ChatOpenAI(model="gpt-35-turbo", temperature=0.5)

# # Step 2: Hybrid Retrieval - BM25 + Vector Search
# vector_store = Chroma(collection_name="network_config_db", embedding_function=EMBED_MODEL)
# bm25_retriever = BM25Retriever.from_texts(["... your data here ..."])
# vector_retriever = vector_store.as_retriever(search_type="mmr", search_kwargs={'k': 5})

# def hybrid_retrieval(query):
#     lexical_results = bm25_retriever.get_relevant_documents(query)
#     vector_results = vector_retriever.get_relevant_documents(query)
#     return lexical_results + vector_results

# # Step 3: Context Memory
# memory = ConversationBufferMemory(memory_key="chat_history")

# # Step 4: Multi-Agent Approach

# # Query Expansion Agent
# def refine_query(query):
#     prompt = ChatPromptTemplate.from_template("""
#         You are an expert network engineer. Improve the search query:
#         Original Query: {query}
#         Optimized Query: """)
#     chain = LLMChain(llm=llm, prompt=prompt)
#     return chain.run(query=query)

# # Validation Agent
# def validate_response(response):
#     return "Valid Configuration" if "config" in response.lower() else "Invalid Configuration"

# # Config Generation Agent
# def generate_config(context, user_query):
#     prompt = ChatPromptTemplate.from_template("""
#         You are a network assistant. Generate the best configuration based on:
#         Context: {context}
#         User Query: {user_query}
#         Configuration:
#     """)
#     chain = LLMChain(llm=llm, prompt=prompt)
#     return chain.run(context=context, user_query=user_query)

# # Step 5: Define Tools for the Agent
# query_expansion_tool = Tool(name="Query Expansion", func=refine_query, description="Expands queries")
# retrieval_tool = Tool(name="Hybrid Retrieval", func=hybrid_retrieval, description="Fetches relevant documents")
# validation_tool = Tool(name="Validation", func=validate_response, description="Validates generated response")
# config_tool = Tool(name="Config Generator", func=generate_config, description="Generates device configs")

# # Step 6: Initialize Agent
# agent = initialize_agent(
#     tools=[query_expansion_tool, retrieval_tool, validation_tool, config_tool],
#     llm=llm,
#     agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
#     memory=memory,
#     verbose=True
# )

# # Step 7: Run the Agent
# user_query = "Retrieve configs for IOS-XR with L2VPN"
# response = agent.run(user_query)
# print("Final Config:", response)





# # Import LangChain components
# from langchain.embeddings import HuggingFaceEmbeddings
# from langchain.vectorstores import Chroma
# from langchain.chat_models import ChatOpenAI
# from langchain_core.prompts import ChatPromptTemplate
# from langchain.retrievers import BM25Retriever
# from langchain_core.memory import ConversationBufferMemory
# from langchain.agents import initialize_agent, AgentType
# from langchain.agents.tools import Tool
# from langchain.chains import LLMChain

# # Step 1: Initialize Embeddings and LLM
# EMBED_MODEL = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
# llm = ChatOpenAI(model="gpt-4", temperature=0.2)  # You can adjust model and temperature

# # Step 2: Vector Store and BM25 Retriever
# vector_store = Chroma(collection_name="network_config_db", embedding_function=EMBED_MODEL)
# bm25_retriever = BM25Retriever.from_texts(["... your data here ..."])
# vector_retriever = vector_store.as_retriever(search_type="mmr", search_kwargs={'k': 5})

# # Step 3: Define Retrieval Fusion Function
# def hybrid_retrieval(query):
#     lexical_results = bm25_retriever.get_relevant_documents(query)
#     vector_results = vector_retriever.get_relevant_documents(query)
#     combined_results = lexical_results + vector_results
#     # Simple deduplication if needed
#     seen = set()
#     final_results = []
#     for doc in combined_results:
#         if doc.page_content not in seen:
#             seen.add(doc.page_content)
#             final_results.append(doc)
#     return final_results

# # Step 4: Define Agent Functions
# # 4.1 Query Expansion
# def refine_query(query):
#     prompt = ChatPromptTemplate.from_template("""
#         You are a senior network engineer specializing in Cisco, Juniper, and Nokia devices.
#         Improve and optimize the user's search query to maximize relevant retrieval.
        
#         Original Query: {query}
        
#         Optimized Query:
#     """)
#     chain = LLMChain(llm=llm, prompt=prompt)
#     return chain.run(query=query).strip()

# # 4.2 Validation of Retrieved Content
# def validate_documents(documents):
#     # Very basic validation based on whether 'config' or 'interface' appears
#     good_docs = []
#     for doc in documents:
#         if "config" in doc.page_content.lower() or "interface" in doc.page_content.lower():
#             good_docs.append(doc)
#     return good_docs

# # 4.3 Config Generation
# def generate_config(context, user_query):
#     context_text = "\n\n".join([doc.page_content for doc in context])
#     prompt = ChatPromptTemplate.from_template("""
#         You are a professional network configuration generator.
        
#         Given the following documents and user query, generate the best possible configuration.
        
#         Context Documents:
#         {context}
        
#         User Query:
#         {user_query}
        
#         Final Device Configuration:
#     """)
#     chain = LLMChain(llm=llm, prompt=prompt)
#     return chain.run(context=context_text, user_query=user_query).strip()

# # Step 5: Wrap into Tools for the Agent
# query_expansion_tool = Tool(name="Query Expansion", func=refine_query, description="Expand and optimize user queries.")
# retrieval_tool = Tool(name="Hybrid Retrieval", func=hybrid_retrieval, description="Hybrid BM25 and vector document retrieval.")
# validation_tool = Tool(name="Validation", func=validate_documents, description="Validate retrieved documents for relevance.")
# config_tool = Tool(name="Config Generator", func=generate_config, description="Generate network device configuration from documents.")

# # Step 6: Conversation Memory
# memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

# # Step 7: Initialize Agent
# agent = initialize_agent(
#     tools=[query_expansion_tool, retrieval_tool, validation_tool, config_tool],
#     llm=llm,
#     agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
#     memory=memory,
#     verbose=True
# )

# # Step 8: Run Agent
# user_query = "Retrieve configs for IOS-XR with L2VPN"
# final_config = agent.run(user_query)
# print("\nGenerated Configuration:\n", final_config)



# Advanced Agent-Based RAG System with Enhancements for Network Config Generation

from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import Chroma
from langchain.chat_models import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain.retrievers import BM25Retriever
from langchain_core.memory import ConversationBufferMemory
from langchain.agents import initialize_agent, AgentType
from langchain.agents.tools import Tool
from langchain.chains import LLMChain
from sentence_transformers import CrossEncoder

# Step 1: Initialize Models
embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
llm = ChatOpenAI(model="gpt-4", temperature=0.2)
cross_encoder = CrossEncoder('cross-encoder/ms-marco-MiniLM-L-6-v2')  # Re-ranker

# Step 2: Setup Vector Store and BM25 Retriever
vector_store = Chroma(collection_name="network_config_db", embedding_function=embedding_model)
vector_retriever = vector_store.as_retriever(search_type="mmr", search_kwargs={"k": 10})
bm25_retriever = BM25Retriever.from_texts(["...pre-loaded data chunks..."])

# Step 3: Metadata-aware Hybrid Retrieval with Deduplication and Filtering
def hybrid_retrieval(query, platform=None, version=None):
    filters = {}
    if platform:
        filters["platform"] = platform.lower()
    if version:
        filters["version"] = version

    vector_results = vector_store.similarity_search_with_score(query, filter=filters, k=10)
    lexical_results = bm25_retriever.get_relevant_documents(query)

    seen = set()
    all_docs = []
    for doc, _ in vector_results:
        if doc.page_content not in seen:
            seen.add(doc.page_content)
            all_docs.append(doc)
    for doc in lexical_results:
        if doc.page_content not in seen:
            seen.add(doc.page_content)
            all_docs.append(doc)
    return all_docs

# Step 4: Re-rank Documents with Cross-Encoder
def rerank_with_cross_encoder(query, docs, top_k=5):
    pairs = [(query, doc.page_content) for doc in docs]
    scores = cross_encoder.predict(pairs)
    sorted_docs = sorted(zip(docs, scores), key=lambda x: x[1], reverse=True)
    return [doc for doc, _ in sorted_docs[:top_k]]

# Step 5: LLM-Powered Query Expansion
def refine_query(query):
    prompt = ChatPromptTemplate.from_template("""
        You are a senior network engineer. Rewrite the query to improve retrieval:
        Original: {query}
        Improved:
    """)
    return LLMChain(llm=llm, prompt=prompt).run(query=query).strip()

# Step 6: Domain-specific Document Validation
def validate_documents(documents):
    return [doc for doc in documents if any(keyword in doc.page_content.lower() for keyword in ["config", "interface", "mpls", "vpn"])]

# Step 7: Prompt-Templated Config Generation (per vendor)
def generate_config(context, user_query, platform="generic"):
    context_text = "\n\n".join([doc.page_content for doc in context])

    templates = {
        "ios-xr": """
        You are a Cisco IOS-XR config generator. Generate configuration from context:

        Context:
        {context}

        User Query:
        {user_query}

        Final Config:
        """,
        "juniper": """
        You are a Junos config generator. Generate configuration from context:

        Context:
        {context}

        User Query:
        {user_query}

        Final Config:
        """,
        "generic": """
        You are a network configuration engine. Based on the context and query, generate the best configuration.

        Context:
        {context}

        Query:
        {user_query}

        Final Config:
        """
    }
    prompt = ChatPromptTemplate.from_template(templates.get(platform.lower(), templates["generic"]))
    return LLMChain(llm=llm, prompt=prompt).run(context=context_text, user_query=user_query).strip()

# Step 8: Tool Definitions
query_expansion_tool = Tool(name="Query Expansion", func=refine_query, description="LLM-powered query expansion.")
retrieval_tool = Tool(name="Hybrid Retrieval", func=hybrid_retrieval, description="Hybrid vector + keyword retrieval with metadata filters.")
validation_tool = Tool(name="Validation", func=validate_documents, description="Domain-based content validation.")
rerank_tool = Tool(name="Reranker", func=rerank_with_cross_encoder, description="Re-rank retrieved results with cross-encoder.")
config_tool = Tool(name="Config Generator", func=lambda ctx, query: generate_config(ctx, query, platform="ios-xr"), description="Generate final network configuration.")

# Step 9: Conversation Memory
memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

# Step 10: Initialize Agent
agent = initialize_agent(
    tools=[query_expansion_tool, retrieval_tool, validation_tool, rerank_tool, config_tool],
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    memory=memory,
    verbose=Truels
)

# Step 11: Run Agent
user_query = "Get L2VPN config for IOS-XR 7.2.1"
final_config = agent.run(user_query)
print("\nGenerated Configuration:\n", final_config)





# Full-stack Agentic RAG with RLHF, Multi-LLM, Evaluation, and Observability

from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import Chroma
from langchain.chat_models import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain.retrievers import BM25Retriever
from langchain_core.memory import ConversationBufferMemory
from langchain.agents import initialize_agent, AgentType
from langchain.agents.tools import Tool
from langchain.chains import LLMChain
from sentence_transformers import CrossEncoder
import random

# Step 1: Initialize Embeddings, LLMs and Cross-Encoder
embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

llm_primary = ChatOpenAI(model="gpt-4", temperature=0.2)
llm_backup = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.2)

cross_encoder = CrossEncoder('cross-encoder/ms-marco-MiniLM-L-6-v2')

# Step 2: Setup Vector Store and BM25 Retriever
vector_store = Chroma(collection_name="network_config_db", embedding_function=embedding_model)
vector_retriever = vector_store.as_retriever(search_type="mmr", search_kwargs={"k": 10})
bm25_retriever = BM25Retriever.from_texts(["...pre-loaded data chunks..."])

# Step 3: Metadata-aware Hybrid Retrieval with Deduplication and Filtering
def hybrid_retrieval(query, platform=None, version=None):
    filters = {}
    if platform:
        filters["platform"] = platform.lower()
    if version:
        filters["version"] = version

    vector_results = vector_store.similarity_search_with_score(query, filter=filters, k=10)
    lexical_results = bm25_retriever.get_relevant_documents(query)

    seen = set()
    all_docs = []
    for doc, _ in vector_results:
        if doc.page_content not in seen:
            seen.add(doc.page_content)
            all_docs.append(doc)
    for doc in lexical_results:
        if doc.page_content not in seen:
            seen.add(doc.page_content)
            all_docs.append(doc)
    return all_docs

# Step 4: Re-rank Documents with Cross-Encoder
def rerank_with_cross_encoder(query, docs, top_k=5):
    pairs = [(query, doc.page_content) for doc in docs]
    scores = cross_encoder.predict(pairs)
    sorted_docs = sorted(zip(docs, scores), key=lambda x: x[1], reverse=True)
    return [doc for doc, _ in sorted_docs[:top_k]]

# Step 5: LLM-Powered Query Expansion
def refine_query(query):
    prompt = ChatPromptTemplate.from_template("""
        You are a senior network engineer. Rewrite the query to improve retrieval:
        Original: {query}
        Improved:
    """)
    return LLMChain(llm=llm_primary, prompt=prompt).run(query=query).strip()

# Step 6: Domain-specific Document Validation
def validate_documents(documents):
    return [doc for doc in documents if any(keyword in doc.page_content.lower() for keyword in ["config", "interface", "mpls", "vpn"])]

# Step 7: Vendor-Specific Config Generation with Multi-LLM Fallback
def generate_config(context, user_query, platform="generic"):
    context_text = "\n\n".join([doc.page_content for doc in context])

    templates = {
        "ios-xr": """
        You are a Cisco IOS-XR config generator. Generate configuration from context:

        Context:
        {context}

        User Query:
        {user_query}

        Final Config:
        """,
        "juniper": """
        You are a Junos config generator. Generate configuration from context:

        Context:
        {context}

        User Query:
        {user_query}

        Final Config:
        """,
        "generic": """
        You are a network configuration engine. Based on the context and query, generate the best configuration.

        Context:
        {context}

        Query:
        {user_query}

        Final Config:
        """
    }
    prompt = ChatPromptTemplate.from_template(templates.get(platform.lower(), templates["generic"]))
    chain = LLMChain(llm=llm_primary, prompt=prompt)
    try:
        return chain.run(context=context_text, user_query=user_query).strip()
    except Exception:
        # Multi-LLM fallback
        fallback_chain = LLMChain(llm=llm_backup, prompt=prompt)
        return fallback_chain.run(context=context_text, user_query=user_query).strip()

# Step 8: Tool Definitions
query_expansion_tool = Tool(name="Query Expansion", func=refine_query, description="LLM-powered query expansion.")
retrieval_tool = Tool(name="Hybrid Retrieval", func=hybrid_retrieval, description="Hybrid vector + keyword retrieval with metadata filters.")
validation_tool = Tool(name="Validation", func=validate_documents, description="Domain-based content validation.")
rerank_tool = Tool(name="Reranker", func=rerank_with_cross_encoder, description="Re-rank retrieved results with cross-encoder.")
config_tool = Tool(name="Config Generator", func=lambda ctx, query: generate_config(ctx, query, platform="ios-xr"), description="Generate final network configuration.")

# Step 9: Conversation Memory
memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

# Step 10: Initialize Agent
agent = initialize_agent(
    tools=[query_expansion_tool, retrieval_tool, validation_tool, rerank_tool, config_tool],
    llm=llm_primary,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    memory=memory,
    verbose=True
)

# Step 11: Run Agent
user_query = "Get L2VPN config for IOS-XR 7.2.1"
final_config = agent.run(user_query)
print("\nGenerated Configuration:\n", final_config)