
import os
import openai
import argparse


def main():
    
    print("Running ChatGPT 3.5")

    parser = argparse.ArgumentParser()
    parser.add_argument("--input_text", "-i", type=str, required=True)
    args = parser.parse_args()
    user_input = args.input_text

    print(f"User input: {user_input}")

    output_text = generate_chat(user_input)
    print(output_text)


def generate_chat(message: str):
    
    # Load your API key from an environment variable or secret management service
    openai.api_key ="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"

    response = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=[
            {"role": "user", "content": message}
        ]
    )

    output_text = response["choices"][0]["message"]["content"]
    
    return output_text

if __name__=="__main__":
    main()