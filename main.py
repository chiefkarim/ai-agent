import os
from dotenv import load_dotenv
from google import genai
import argparse

from google.genai import types

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
if api_key == None:
    raise RuntimeError("GEMINI_API_KEY not found")


def main():
    global model
    parser = argparse.ArgumentParser("Chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    parser.add_argument(
        "--model", type=str, help="Model defaults to gemini-2.5-flash", required=False
    )
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()
    model = args.model if args.model != None else "gemini-2.5-flash"
    prompt = args.user_prompt
    verbose = args.verbose

    client = genai.Client(api_key=api_key)
    messages = [types.Content(parts=[types.Part(text=prompt)], role="user")]
    response = client.models.generate_content(
        model=model,
        contents=messages,
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
    if verbose:
        printResponseMetadata(
            prompt,
            prompt_token_count=prompt_token_count,
            response_token_count=response_token_count,
        )
    if response.text != None:
        print(response.text)
    else:
        raise RuntimeError("Somthing went wrong getting response from gemini API")


def printResponseMetadata(
    prompt: str, prompt_token_count: int, response_token_count: int
):
    print(f"User prompt: {prompt}")
    print(f"Prompt tokens: {prompt_token_count}")
    print(f"Response tokens: {response_token_count}")


if __name__ == "__main__":
    main()
