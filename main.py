import os
from google import genai


client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
def main():
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents="Write a short poem about the sea."
    )   


    print(response.text)    


if __name__ == "__main__":
    main()  