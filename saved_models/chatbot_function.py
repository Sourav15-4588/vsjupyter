
def expert_chatbot(question):
    """Your working solution with the expert prompt"""
    
    # 1. Search document
    results = collection.query(
        query_texts=[question],
        n_results=2,
        include=['metadatas', 'documents']
    )
    
    if not results or not results['documents']:
        return "As a financial expert, I don't have enough information to answer that based on the document."
    
    # 2. Build context
    context = ""
    for doc, metadata in zip(results['documents'][0], results['metadatas'][0]):
        context += f"[Page {metadata['page_number']}]: {doc}\n"
    
    # 3. Your working expert prompt
    prompt = f"""You are an expert financial analyst with deep knowledge of government policy. 
Answer the question using only the provided context from the financial policy document.

Document Context:
{context}

Question: {question}

As a financial expert, provide a clear, professional answer:"""
    
    # 4. Generate response
    try:
        response = text_generator(
            prompt,
            max_new_tokens=200,
            temperature=0.7,
            truncation=True
        )
        return response[0]['generated_text'].split("As a financial expert, provide a clear, professional answer:")[-1].strip()
    except:
        return f"Based on the document: {context[:200]}..."
