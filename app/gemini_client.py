# import google.generativeai as genai
# from .config import GEMINI_API_KEY

# genai.configure(api_key=GEMINI_API_KEY)

# model = genai.GenerativeModel('gemini-pro')

# def generate_text(prompt: str) -> str:
#     try:
#         response = model.generate_content(prompt)
#         return response.text
#     except Exception as e:
#         return f"Error: {e}"


import google.generativeai as genai
from .config import GEMINI_API_KEY

# The client gets the API key from the environment variable `GEMINI_API_KEY`.
client = genai.Client()

response = client.models.generate_content(
    model="gemini-2.5-flash", contents="Explain how AI works in a few words"
)
print(response.text)