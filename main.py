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
    prompt = "Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum."
    response = client.models.generate_content(
        model=model,
        contents=prompt,
    )
    if (
        response.usage_metadata == None
        or response.usage_metadata.prompt_token_count == None
    ):
        raise RuntimeError(
            "Somthing went wrong making request to GEMINI API. prompt token count is None"
        )
    if response.usage_metadata.candidates_token_count == None:
        raise RuntimeError(
            "Somthing went wrong making request to GEMINI API. candidates token count is None"
        )
    prompt_token_count = response.usage_metadata.prompt_token_count
    response_token_count = response.usage_metadata.candidates_token_count

    print(f"User prompt: {prompt}")
    print(f"Prompt tokens: {prompt_token_count}")
    print(f"Response tokens: {response_token_count}")
    if response.text != None:
        print(response.text)
    else:
        raise RuntimeError("Somthing went wrong getting response from gemini API")


if __name__ == "__main__":
    main()
