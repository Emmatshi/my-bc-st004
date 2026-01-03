import streamlit as st
from my_bc_st004.generator import summarize_text

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

col1, col2 = st.columns(2)

with col1:
    if st.button("Summarize ✨"):
        if not input_text.strip():
            st.warning("Please paste some text to summarize.")
        else:
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
    st.markdown(st.session_state.summary)

