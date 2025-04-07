import os
import argparse
from langchain_community.llms import HuggingFaceHub


def load_prompts():
    with open("prompts/base_prompt.txt") as base, \
         open("prompts/user_config.txt") as config, \
         open("prompts/persona.txt") as persona:
        return base.read() + "\n\n" + config.read() + "\n\n" + persona.read()

def prepare_prompt(topic: str):
    base_prompt = load_prompts()
    final_prompt = f"{base_prompt}\n\nNow teach me about: {topic}\n"
    return final_prompt

def use_chatgpt(prompt: str):
    print("\n--- CHATGPT MODE ---")
    print(f"\nPrompt sent to ChatGPT:\n{prompt}")

def use_llama(prompt: str):
    print("\n--- LLaMA (via Hugging Face) MODE ---")

    # Add your Hugging Face API token here
    os.environ["HUGGINGFACEHUB_API_TOKEN"] = "hugging_face_token"
    llm = HuggingFaceHub(
    repo_id="tiiuae/falcon-7b-instruct",  # or try mistralai/Mistral-7B-Instruct-v0.1
    model_kwargs={"temperature": 0.7, "max_new_tokens": 512}
)
    response = llm(prompt)
    print(response)

def main():
    parser = argparse.ArgumentParser(description="AI Tutor CLI")
    parser.add_argument("--topic", type=str, required=True, help="Topic to learn")
    parser.add_argument("--mode", choices=["chatgpt", "llama"], default="chatgpt", help="Model backend")
    args = parser.parse_args()

    prompt = prepare_prompt(args.topic)

    if args.mode == "chatgpt":
        use_chatgpt(prompt)
    else:
        use_llama(prompt)

if __name__ == "__main__":
    main()
