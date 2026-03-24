import json, os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def generate_path(topic):
    try:
        completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{
                "role": "system", 
                "content": (
                    "You are a Senior Staff Engineer. Create a high-fidelity technical roadmap. "
                    "CRITICAL: Use strictly professional, industry-standard technical terms. "
                    "If the topic is 'Java', include JVM, Spring Boot, Concurrency, and Bytecode. "
                    "Return ONLY JSON: {'topic': str, 'summary': str, 'steps': [{'title': str, 'time': str, 'desc': str, 'link': str}]}"
                )
            }, {
                "role": "user", 
                "content": f"Architect a 5-step professional mastery path for {topic}"
            }],
            response_format={"type": "json_object"}
        )
        return json.loads(completion.choices[0].message.content)
    except Exception as e:
        return {"error": str(e), "steps": []}