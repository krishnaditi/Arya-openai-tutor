# 🧠 Arya - Open Source AI Tutor

**Arya** is a fully customizable AI tutor built as an open-source alternative to projects like [Mr. Ranedeer](https://github.com/JushBJJ/Mr.-Ranedeer-AI-Tutor?tab=readme-ov-file#requirements-and-compatibility). It supports a configurable backend and allows seamless adaptation for different deployment scenarios.

> ✨ Great for learners, hobbyists, and developers building custom tutors.

---

## 🚀 Features

- 🔄 Switchable backend configuration
- 🧑‍🏫 Personalized tutor behavior (learning style, tone, level)
- 📝 Prompt customization (via config files)
- 🖼️ Easy to extend into CLI or web interfaces
- 🌐 Offline capability if applicable

---

## 📂 Project Structure

```plaintext
Arya-openai-tutor/ 
├── prompts/ 
│   ├── base_prompt.txt 
│   ├── user_config.txt 
│   └── persona.txt 
├── src/ 
│   └── main.py 
├── examples/ 
│   └── sample_output.txt 
├── requirements.txt 
├── README.md 
└── .gitignore
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

Run the tutor with your topic of interest:

```
bash

python src/main.py --topic "Quantum Physics"

```


## 🧾 Customize Your Tutor

Edit the following:

        prompts/base_prompt.txt — core behavior of the tutor

        prompts/user_config.txt — tone, style, academic level

        prompts/persona.txt — personality (e.g., fun professor, emoji use)
        

## 🧱 Built With

 🧩 llama-cpp-python

 🤖 OpenAI API / Selenium (for ChatGPT)

 🐍 Python 3.9+


## 💡 Future Ideas

- Web UI using Gradio or Streamlit

- Voice interaction

- Multiple personas (Socratic, Friendly, etc.)

- GUI with chat history


## 🤝 Acknowledgements

Inspired by Mr. Ranedeer AI Tutor.
Built by Aditi Krishana with ❤️ for open-source learning.
