import streamlit as st
from src.pdf_processor import extract_text, split_into_chunks
from src.vector_store import load_embedding, build_vectorstore, search

from src.chatbot import ask_gemini

st.set_page_config(
    page_title="Sannasa AI",
    page_icon="📄"
)

st.markdown("""
    <h1 style='text-align: center;'>📄 Sannasa AI</h1>
    <p style='text-align: center; color: gray;'>
        Upload any PDF and chat with it instantly using AI.
        Powered by LLaMA 3 + Semantic Search.
    </p>
    <hr>
""", unsafe_allow_html=True)
st.write("Turn any PDF into an interactive conversation.\nAsk questions, get precise answers, and explore your document intelligently.\nWorks with reports, research papers, manuals, and more.The AI will answer strictly based on your document.Questions outside the document will return not be answered")

#file uploader
uploaded_file = st.file_uploader("Upload your PDF Document", type="pdf")

#sidebar
with st.sidebar:
    
    st.markdown("---")
    st.markdown("### 🚀 Upcoming Features")
    st.markdown("""
    - 📚 Multiple PDF support
    - 🌐 Website URL ingestion
    - 📊 Document summarization
    - 🌍 Multi-language support
    """)
    
    st.markdown("---")
    st.caption("Built with LLaMA 3 + LangChain + ChromaDB")
    st.markdown("""
    <div style='text-align: center; padding: 10px;'>
        <a href='https://github.com/ravinduWP' target='_blank' 
        style='color: #CBC1AE; text-decoration: none; font-size: 16px;'>
            🐙 GitHub
        </a><br>
                <a href='https://ravindusaputhanthri.vercel.app/' target='_blank' 
        style='color: #CBC1AE; text-decoration: none; font-size: 16px;'>
            🌐 MyProtfolio
        </a>
    </div>
""", unsafe_allow_html=True)

#after process of file upload
if uploaded_file:
    file_bytes = uploaded_file.read()
    file_hash = hash(file_bytes)
    
    if "current_pdf_hash" not in st.session_state or st.session_state.current_pdf_hash != file_hash:
        with st.spinner("Processing your PDF..."):
            import io
            text = extract_text(io.BytesIO(file_bytes))
            chunks = split_into_chunks(text)
            embeddings = load_embedding()
            vectorstore = build_vectorstore(chunks, embeddings)
            st.session_state.vectorstore = vectorstore
            st.session_state.history = []
            st.session_state.current_pdf_hash = file_hash
            st.session_state.current_pdf = uploaded_file.name
    st.success("Ready! Ask me anything about your document.")


    if "history" not in st.session_state:
        st.session_state.history = []

    for role, msg in st.session_state.history:
        st.chat_message(role).write(msg)

    question = st.chat_input("Hi! how can i help you...")
    if question:
        st.chat_message("user").write(question)
        results = search(st.session_state.vectorstore, question)
        answer = ask_gemini(question, results, st.session_state.history)
        st.chat_message("assistant").write(answer)
        st.session_state.history += [("user", question), ("assistant", answer)]