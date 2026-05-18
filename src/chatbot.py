import os
from dotenv import load_dotenv
import google.generativeai as genai


load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-3.1-flash-lite")

def build_prompt(question, context_chunks, history):
    context = "\n\n".join([chunk.page_content for chunk in context_chunks])
    history_text = "\n".join(f"{role}: {msg}" for role, msg in history)

    prompt = f"""You are a helpful assistant. 
Answer only based on the context below.
If the answer is not in the context, say 'I couldn't find relevant information about that in the uploaded document. 
Try rephrasing your question or ask something else!'

Context:
{context}

Conversation so far:
{history_text}

Question: {question}
Answer:"""
    return prompt

def ask_gemini(question, context_chunks, history=[]):
    prompt = build_prompt(question, context_chunks, history)
    response = model.generate_content(prompt)
    return response.text
