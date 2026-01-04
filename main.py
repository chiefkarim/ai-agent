import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
if api_key == None:
    raise RuntimeError("GEMINI_API_KEY not found")
model = os.getenv("MODEL")


def main():
    global model
    model = model if model != None else "gemini-2.5-flash"

    client = genai.Client(api_key=api_key)
    response = client.models.generate_content(
        model=model,
        contents="Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum.",
    )

    if response.text != None:
        print(response.text)
    else:
        raise RuntimeError("Somthing went wrong getting response from gemini API")


if __name__ == "__main__":
    main()
