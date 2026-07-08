# basic_rag.py
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

try:
    print("Loading Ollama...")
    llm = OllamaLLM(model="llama3")
    
    print("Creating prompt...")
    prompt = ChatPromptTemplate.from_template("What is the capital of {country}?")
    chain = prompt | llm
    
    print("Invoking chain...")
    response = chain.invoke({"country": "India"})
    
    print("Response:")
    print(response)
    
except Exception as e:
    print(f"Error: {e}")
