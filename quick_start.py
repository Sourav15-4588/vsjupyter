
# Financial Chatbot Quick Start
import chromadb
from transformers import pipeline

# 1. Load database
client = chromadb.PersistentClient(path="./financial_policy_chromadb")
collection = client.get_collection("financial_policy")

# 2. Load LLM
text_generator = pipeline("text-generation", model="./saved_models/financial_expert")

# 3. Ask question function
def ask_question(question):
    results = collection.query(
        query_texts=[question],
        n_results=2,
        include=['metadatas', 'documents']
    )
    
    if not results or not results['documents']:
        return "No information found."
    
    context = ""
    for doc, metadata in zip(results['documents'][0], results['metadatas'][0]):
        context += f"[Page {metadata['page_number']}]: {doc}\n"
    
    prompt = f"""You are an expert financial analyst. Answer based on this context:

{context}

Question: {question}

Expert answer:"""
    
    try:
        response = text_generator(prompt, max_new_tokens=200, temperature=0.7, truncation=True)
        return response[0]['generated_text'].split("Expert answer:")[-1].strip()
    except:
        return f"Based on document: {context[:200]}..."

# 4. Use it!
question = "What is budget?"
print(f"❓ {question}")
print(f"💼 {ask_question(question)}")
