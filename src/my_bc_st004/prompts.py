from langchain_core.prompts import PromptTemplate

SUMMARY_PROMPT = PromptTemplate.from_template(
    """
Summarize the following text in a {length} way.

Text:
{text}

Guidelines:
- Be clear and concise
- Preserve key points
- Use bullet points if helpful
"""
)
