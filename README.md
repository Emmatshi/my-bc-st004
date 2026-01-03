# my-bc-st004 — Text Summarizer

[![Open in Streamlit](https://2rpz6ewxyfuzzlernsbzjj.streamlit.app/)](https://my-bc-st004.streamlit.app)

## 📝 Text Summarizer

A Streamlit app that summarizes long text using OpenAI and LangChain.

### Features

-   Paste any text to summarize
-   Choose summary length (Short / Medium / Detailed)
-   Displays original and summary word counts
-   Copy summary to clipboard
-   Clean, responsive UI

## 🚀 Live App

👉 https://my-bc-st004.streamlit.app

## 🧰 Tech Stack

-   Python 3.11
-   Streamlit
-   LangChain
-   OpenAI API
-   Poetry

## 🧱 Architecture

The app follows a clean `src/` layout:

-   `main.py` — Streamlit UI
-   `generator.py` — summarization logic
-   `prompts.py` — prompt templates
-   `llm.py` — OpenAI client configuration

## 🏃‍♂️ Run Locally

```bash
git clone https://github.com/Emmatshi/my-bc-st004.git
cd my-bc-st004
pyenv local 3.11.4
poetry install
poetry run python -m streamlit run main.py
```
