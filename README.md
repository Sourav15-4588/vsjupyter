Financial Policy Chatbot
A simple AI chatbot that answers questions from financial policy documents using smart search and conversation memory.

What We Built
Document Processor: Extracts text and tables from PDFs
Smart Search: Finds relevant information using vector database (ChromaDB)
AI Answers: Uses language model to generate expert responses
Conversation Memory: Remembers what you asked for follow-up questions


📁 Project Structure
financial-chatbot/
├── saved_models/
│   ├── financial_expert/          # Saved LLM model
│   └── chatbot_function.py           # Chatbot class definition
├── financial_policy_chromadb/     # Vector database (auto-created)
├── Policy_file.pdf                # Your financial document
├── chat.ipynb                     # Data extracting and vector DB creating notebook
├── model.ipynb                    # Preparing model
├── bot.ipynb                      # Conversation memory and the interface
└── README.md                      # This file


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

Phase 4: Conversation Memory ✅
  Context tracking across conversations
  Follow-up question understanding ("What about...?")
  Topic persistence and memory management
  Natural conversation flow

Phase 5: User Interface ✅
  VS Code-compatible widget interface

How to Run
  I have done the processing of the data, so no need to do it again. All the steps are given above. The sequence for the notebook is given in the project structure. All I just need to run the cells from bot.ipynb file run sequentially and the bot will start working.


