from dotenv import load_dotenv
from langchain_groq import ChatGroq
import os

load_dotenv()

llm = ChatGroq(model="llama-3.1-8b-instant", api_key=os.getenv("GROQ_API_KEY"))

print("Welcome!")
print("Do you need help with something today?")
request = input()

response = llm.invoke(request)

text_response = response['text'] if isinstance(response, dict) else str(response)
print(text_response)


