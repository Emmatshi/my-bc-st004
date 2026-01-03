import streamlit as st
from my_bc_st004.generator import summarize_text

def word_count(text: str) -> int:
    return len(text.split())


st.set_page_config(page_title="Text Summarizer", layout="wide")
st.title("📝 Text Summarizer")

st.sidebar.header("Summary Settings")

length = st.sidebar.selectbox(
    "Summary length",
    ["Short", "Medium", "Detailed"],
)

if "summary" not in st.session_state:
    st.session_state.summary = ""

input_text = st.text_area(
    "Paste text to summarize",
    height=250,
    key="input_text",
)
if input_text:
    st.caption(f"🧮 Original word count: {word_count(input_text)}")

col1, col2 = st.columns(2)

with col1:
    if st.button(
        "Summarize ✨",
        disabled=not input_text.strip(),
    ):
        with st.spinner("Summarizing..."):
            st.session_state.summary = summarize_text(
                text=input_text,
                length=length.lower(),
            )

with col2:
    if st.button("Reset 🔄"):
        st.session_state.input_text = ""
        st.session_state.summary = ""

if st.session_state.summary:
    st.markdown("### Summary")

    st.caption(
        f"🧮 Summary word count: {word_count(st.session_state.summary)}"
    )

    st.markdown(st.session_state.summary)

st.code(st.session_state.summary, language="markdown")



