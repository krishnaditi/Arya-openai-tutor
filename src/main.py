import os
import argparse
from dotenv import load_dotenv, find_dotenv
from groq import Groq

# Load .env variables
load_dotenv(find_dotenv(), override=True)

# Initialize Groq client with API key
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def load_prompts():
    with open("prompts/base_prompt.txt") as base, \
         open("prompts/user_config.txt") as config, \
         open("prompts/persona.txt") as persona:
        return base.read() + "\n\n" + config.read() + "\n\n" + persona.read()

def prepare_prompt(topic: str):
    base_prompt = load_prompts()
    final_prompt = f"{base_prompt}\n\nNow teach me about: {topic}\n"
    return final_prompt

def use_groq(prompt: str):
    print("\n--- GROQ MODE ---")
    print(f"\nPrompt sent to Groq:\n{prompt}\n")

    try:
        chat_completion = client.chat.completions.create(
            model="meta-llama/llama-4-scout-17b-16e-instruct",  # You can use other available models too
            messages=[
                {"role": "system", "content": "You are a helpful AI tutor."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
        )
        print("\nResponse from Groq:\n")
        print(chat_completion.choices[0].message.content)
    except Exception as e:
        print(f"Failed to get response from Groq SDK: {e}")

def main():
    parser = argparse.ArgumentParser(description="AI Tutor CLI (Groq API)")
    parser.add_argument("--topic", type=str, required=True, help="Topic to learn about")
    args = parser.parse_args()

    prompt = prepare_prompt(args.topic)
    use_groq(prompt)

if __name__ == "__main__":
    main()
