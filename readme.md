# 📄 DocuMind AI

An AI-powered document chatbot that lets you upload any PDF and ask questions about it in natural language. Built with a RAG (Retrieval-Augmented Generation) pipeline.

🔗 **Live Demo:** [doc-umind-ai.streamlit.app](https://doc-umind-ai.streamlit.app)

---

## 🧠 How It Works

1. Upload a PDF document
2. The document is split into chunks and converted to embeddings
3. Embeddings are stored in a local vector database (ChromaDB)
4. When you ask a question, it finds the most relevant chunks using semantic search
5. Those chunks are sent to an LLM which answers strictly based on your document

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Frontend | Streamlit |
| LLM | Google Gemini |
| RAG Framework | LangChain |
| Embeddings | sentence-transformers (all-MiniLM-L6-v2) |
| Vector Database | ChromaDB |
| PDF Processing | PyMuPDF |

---

## 🚀 Run Locally

**1. Clone the repository**
```bash
git clone https://github.com/ravinduWP/DocuMind_AI.git
cd DocuMind_AI
```

**2. Create virtual environment**
```bash
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Mac/Linux
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

**4. Add your API key**

Create a `.env` file in the root folder:
GEMINI_API_KEY=your_key_here

Get a free key at [aistudio.google.com](https://aistudio.google.com)

**5. Run the app**
```bash
streamlit run app.py
```

---

## ✅ Features

- Upload any text-based PDF
- Ask questions in plain English
- Answers grounded strictly in your document
- Chat history within a session
- Automatically resets when a new PDF is uploaded

---

## 🚀 Upcoming Features

- 📚 Multiple PDF support
- 🌐 Website URL ingestion
- 📊 Document summarization
- 🌍 Multi-language support

---

## 👨‍💻 Author

**Ravindu** — [GitHub](https://github.com/ravinduWP)
