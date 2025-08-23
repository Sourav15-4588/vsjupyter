Financial Policy Chatbot
A simple AI chatbot that answers questions from financial policy documents using smart search.

What We Built
Document Processor: Extracts text and tables from PDFs
Smart Search: Finds relevant information using vector database (ChromaDB)
AI Answers: Uses language model to generate expert responses

<img width="692" height="328" alt="image" src="https://github.com/user-attachments/assets/fe6cf28d-61e6-4ebd-a420-705d89a26e4c" />

Phase 1: Document Processing ✅
  PDF text extraction with pdfplumber (handles tables)
  Text cleaning and chunking (3-5 sentences per chunk)
  Financial topic identification (budget, debt, infrastructure, etc.)
  Metadata preservation (page numbers, topics, table flags)

Phase 2: Vector Database Setup ✅
  ChromaDB vector database with persistent storage
  SentenceTransformer embeddings (all-MiniLM-L6-v2)
  Semantic search implementation
  Metadata indexing for filtered searches

Phase 3: LLM Integration ✅
  Microsoft DialoGPT for answer generation
  Expert prompt engineering: "You are a financial expert..."
  Context-aware response generation
  Error handling and fallback mechanisms

How to Run
  I have processed the data, so there is no need to do it again. All the steps are given above. The notebook's sequence is given in the project structure. I just need to run from the quick start cell in the model.ipynb file. I saved the learnings of the model. So no need to run the entire code again.


Phase 4: Conversation Memory ✅
  About that, I'm currently working and learning generative AI. At this moment, I can't implement the conversation memory, but I'll learn and implement it very soon.
