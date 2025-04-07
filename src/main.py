import os
import argparse

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
    # Replace this placeholder with browser automation or API use
    print("\n--- CHATGPT MODE ---")
    print(f"\nPrompt sent to ChatGPT:\n{prompt}")

# def use_llama(prompt: str):
#     from llama_cpp import Llama
#     llm = Llama(model_path="models/llama-3.gguf")  # change path
#     output = llm(prompt, max_tokens=1024)
#     print("\n--- LLaMA OUTPUT ---")
#     print(output['choices'][0]['text'])

def main():
    parser = argparse.ArgumentParser(description="AI Tutor CLI")
    parser.add_argument("--topic", type=str, required=True, help="Topic to learn")
    parser.add_argument("--mode", choices=["chatgpt", "llama"], default="chatgpt", help="Model backend")
    args = parser.parse_args()

    prompt = prepare_prompt(args.topic)

    if args.mode == "chatgpt":
        use_chatgpt(prompt)
    # else:
    #     use_llama(prompt)

if __name__ == "__main__":
    main()
