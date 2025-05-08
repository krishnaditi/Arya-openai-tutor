# 🧠 Arya - Open Source AI Tutor (Langchain)

**Arya** is a fully customizable AI tutor built as an open-source alternative to projects like [Mr. Ranedeer](https://github.com/JushBJJ/Mr.-Ranedeer-AI-Tutor?tab=readme-ov-file#requirements-and-compatibility). It supports both **local Langchain**, allowing seamless switching between open-source and hosted models.

> ✨ Great for learners, hobbyists, and developers building custom tutors.

---

## 🚀 Features

- 🔄 Switchable backends: `Langchain (hugging face token)` or `LLaMA (local)` or `ChatGPT (API/browser)`
- 🧑‍🏫 Personalized tutor behavior (learning style, tone, level)
- 📝 Prompt customization (via config files)
- 🖼️ Easy to extend into CLI or web interfaces
- 🌐 Offline capability with LLaMA

---

## 📂 Project Structure

```plaintext

Arya-openai-tutor/ 
├── prompts/ 
    │ ├── base_prompt.txt 
    │ ├── user_config.txt 
    │ |── persona.txt 
├── src/ 
    │ ├── main.py 
├── examples/ 
    │ ├── sample_output.txt 
├── requirements.txt 
├── README.md 
├── .gitignore

```

## ⚙️ Installation

1. Clone the repo:
```bash
git clone https://github.com/krishnaditi/Arya-openai-tutor.git
cd Arya-openai-tutor
```

2. (Optional) Create a virtual environment:

```
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
```

3. Install dependencies:

```
pip install -r requirements.txt
```

## 🧠 Usage

1. LLaMA Mode (local):

Make sure you have a .gguf model downloaded (e.g., llama-3.gguf) and placed in a models/ folder.

```
bash

python src/main.py --topic "Quantum Physics" --mode llama

```

2. ChatGPT Mode:

If using browser automation or API (you can add this), switch mode:

```
bash

python src/main.py --topic "Machine Learning" --mode chatgpt

```
3. Langchain Mode:

Make sure you have a hugging face token for langchain.

```
bash

python src/main.py --mode llama --topic "Neural Networks"

```


## 🧾 Customize Your Tutor

>>> Edit the following:

        prompts/base_prompt.txt — core behavior of the tutor

        prompts/user_config.txt — tone, style, academic level

        prompts/persona.txt — personality (e.g., fun professor, emoji use)
        

## 🧱 Built With

>>> 🧩 llama-cpp-python

>>> 🤖 OpenAI API / Selenium (for ChatGPT)

>>> 🐍 Python 3.9+


## 💡 Future Ideas

- Web UI using Gradio or Streamlit

- Voice interaction

- Multiple personas (Socratic, Friendly, etc.)

- GUI with chat history


## 🤝 Acknowledgements

Inspired by Mr. Ranedeer AI Tutor.
Built by Aditi Krishana with ❤️ for open-source learning.
