from dotenv import load_dotenv
import os
from openai import OpenAI

# Load environment variables
load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def synthesize_response(query, docs):
    context = "\n".join(docs)
    prompt = f"Answer the query using this context:\n\n{context}\n\nQuery: {query}"
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content
