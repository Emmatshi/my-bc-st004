from my_bc_st004.llm import get_llm
from my_bc_st004.prompts import SUMMARY_PROMPT

def summarize_text(text: str, length: str) -> str:
    llm = get_llm()
    query = SUMMARY_PROMPT.format(
        text=text,
        length=length,
    )

    try:
        response = llm.invoke(query)
        return response.content.strip()
    except Exception as exc:
        return(
            "⚠️ Unable to generate summary at this time.\n\n"
            f"Details: {exc}"
        )
        