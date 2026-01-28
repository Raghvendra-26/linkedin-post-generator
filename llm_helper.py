from dotenv import load_dotenv 
from langchain_groq import ChatGroq
import os

load_dotenv()

llm = ChatGroq(model='openai/gpt-oss-20b',groq_api_key = os.getenv("GROQ_API_KEY"))

if __name__ == "__main__":
    res = llm.invoke('How to make samosa?')
    print(res.content)