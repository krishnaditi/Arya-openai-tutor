# prompts/utils.py

def load_prompt_files():
    with open("prompts/base_prompt.txt", "r", encoding="utf-8") as f:
        base_prompt = f.read()

    with open("prompts/user_config.txt", "r", encoding="utf-8") as f:
        user_config = f.read()

    with open("prompts/persona.txt", "r", encoding="utf-8") as f:
        persona = f.read()

    return base_prompt, user_config, persona
