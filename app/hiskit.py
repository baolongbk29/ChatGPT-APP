
import os
import openai
import argparse


def main():
    
    print("Running ChatGPT 3.5")

    parser = argparse.ArgumentParser()
    parser.add_argument("--input_name", "-i", type=str, required=True)
    args = parser.parse_args()
    user_input = args.input_name

    print(f"User input: {user_input}")

    output_text = generate_history(user_input)
    print(output_text)


def generate_history(name: str) -> str:
    
    # Load your API key from an environment variable or secret management service
    openai.api_key ="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"
    prompt = f"Brief biography of {name}"

    response = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=[
            {"role": "user", "content": prompt},
        ]
    )

    output_text : str = response["choices"][0]["message"]["content"]
    
    return output_text

if __name__=="__main__":
    main()