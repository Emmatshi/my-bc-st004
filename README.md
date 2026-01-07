# my-bc-st004 — Text Summarizer

[![Open in Streamlit](https://2rpz6ewxyfuzzlernsbzjj.streamlit.app/)](https://my-bc-st004.streamlit.app)

# 📝 Text Summarizer

A Streamlit application that summarizes long-form text into concise,
readable summaries using a large language model.

This app was refactored to align with a reusable Streamlit AI template,
ensuring clean architecture, CI validation, and consistent deployment.

## ✨ Features

-   Summarizes long text into concise outputs
-   Adjustable summary length
-   Clean separation of UI and LLM logic
-   Secure OpenAI API key handling
-   CI-validated project structure

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

## 🏃 Run Locally

### Prerequisites

-   Python 3.11
-   Poetry

### Setup

```bash
git clone https://github.com/Emmatshi/my-bc-st004.git
cd my-bc-st004
poetry install

## 🧩 Built From a Reusable Template

This application was refactored to align with a reusable Streamlit AI
template that standardizes project structure, secrets management, and CI.

🔗 Template repository:
https://github.com/Emmatshi/streamlit-ai-template
```
