# 📄 Chat with Multiple PDFs

This project allows you to upload multiple PDF documents and interact with them using a conversational AI interface. It processes the PDFs, extracts their content, and enables you to ask questions about the documents. The system utilizes state-of-the-art language models and vector-based retrieval to provide accurate and contextual responses.

---

## 🚀 Features

- **Multi-PDF Support:** Upload multiple PDF files to query their content seamlessly.
- **Text Extraction:** Automatically extracts text from PDF files for analysis.
- **Chunked Text Processing:** Splits large text into manageable chunks for efficient processing.
- **Advanced Embeddings:** Leverages OpenAI embeddings for creating vectorized text representations.
- **Conversational AI:** Powered by OpenAI's conversational models for an interactive experience.
- **Retrieval-based Responses:** Combines memory and retrieval mechanisms to deliver context-aware answers.
- **User-friendly Interface:** Built with Streamlit for a smooth and intuitive user experience.

---

## 🛠️ Tech Stack

- **Streamlit:** Interactive user interface.
- **PyPDF2:** PDF text extraction.
- **LangChain:** Advanced conversational AI and retrieval workflows.
- **FAISS:** Vector database for fast similarity search.
- **OpenAI API:** Language model for conversation.
- **HuggingFace Hub (optional):** Alternate embedding model support.
- **dotenv:** Securely manage API keys and configurations.

---

## 📝 How It Works

1. **Upload PDFs:** Use the sidebar to upload your documents.
2. **Process Documents:** The system extracts and processes text from the uploaded PDFs.
3. **Interactive Querying:** Ask questions about the content, and get accurate responses in real-time.
4. **Dynamic Memory:** Retains chat history for a seamless conversational flow.

---  

## 📋 Usage Instructions

1. Clone this repository:
   ```bash
   git clone https://github.com/your-repo/chat-with-multiple-pdfs.git
   cd chat-with-multiple-pdfs
2. Install required dependencies:
   `pip install -r requirements.txt`
3. Add your API key in a .env file
   `OPENAI_API_KEY=your_openai_api_key`
4. Run the Streamlit application:
   `streamlit run app.py`




