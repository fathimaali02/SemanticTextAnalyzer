import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title="PlagiarismAI", layout="wide")

st.title("PlagiarismAI — AI & Plagiarism Result Checker")

tab1, tab2 = st.tabs(["Index Documents", "Check Text"])

# -------- INDEX TAB --------
with tab1:
    st.subheader("Add Text To Database")

    index_text = st.text_area("Paste text to index", height=200)

    if st.button("Index Text"):
        if index_text.strip():
            try:
                res = requests.post(
                    f"{API_URL}/index",
                    json={"text": index_text}
                )
                if res.status_code == 200:
                    st.success("Text indexed successfully")
                else:
                    st.error(res.text)
            except Exception as e:
                st.error(str(e))


# -------- CHECK TAB --------
with tab2:
    st.subheader("Analyze Text")

    check_text = st.text_area("Paste text to analyze", height=200)

    if st.button("Run Analysis"):
        if check_text.strip():
            try:
                res = requests.post(
                    f"{API_URL}/check",
                    json={"text": check_text}
                )

                if res.status_code == 200:
                    data = res.json()

                    st.markdown("## Result")

                    summary = data.get("summary", {})
                    similarity_text = summary.get("similarity_result", "")
                    ai_text = summary.get("ai_interpretation", "")

                    st.write(
                        "Plagiarism signal:",
                        f"**{similarity_text.replace(' detected','')}**"
                    )

                    if "varied language pattern" in ai_text.lower():
                        st.write(
                            "AI-generation signal:",
                            "**No strong AI pattern detected**"
                        )
                    elif "high predictability" in ai_text.lower():
                        st.write(
                            "AI-generation signal:",
                            "**Strong AI-like predictability pattern**"
                        )
                    else:
                        st.write(
                            "AI-generation signal:",
                            "**Moderate AI-like pattern**"
                        )

                else:
                    st.error(res.text)

            except Exception as e:
                st.error(str(e))
