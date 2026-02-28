import streamlit as st
from agent_logic import (
    generate_summary,
    extract_decisions,
    extract_action_items,
    extract_risks,
    generate_next_steps
)

st.set_page_config(page_title="Internal Meeting Intelligence Agent", layout="wide")

st.title("🧠 Internal Meeting Intelligence Agent")
st.markdown("""
**Purpose:**  
Convert unstructured meeting transcripts into structured, decision-ready insights  
for internal teams and stakeholders.
""")
st.divider()

st.markdown("### 🔄 Workflow")
st.markdown("""
1. Input raw meeting transcript  
2. Extract executive summary  
3. Identify decisions & action items  
4. Highlight risks  
5. Generate structured next steps  
""")
st.divider()

text = st.text_area("Paste meeting transcript here:", height=250)

if st.button("Analyze Meeting"):
    if text.strip() == "":
        st.warning("Please paste meeting transcript.")
    else:
        col1, col2 = st.columns(2)

        with col1:
            st.subheader("📌 Executive Summary")
            st.write(generate_summary(text))

            st.subheader("🗳 Key Decisions")
            for d in extract_decisions(text):
                st.write(f"- {d}")

            st.subheader("⚠ Risks / Concerns")
            for r in extract_risks(text):
                st.write(f"- {r}")

        with col2:
            st.subheader("✅ Action Items")
            for a in extract_action_items(text):
                st.write(f"- {a}")

            st.subheader("➡ Next Steps")
            for n in generate_next_steps():
                st.write(f"- {n}")
st.divider()
st.markdown("### 🧩 Agent Design Logic")
st.markdown("""
This prototype simulates an internal AI workflow agent designed to:
- Reduce cognitive load from long meetings
- Convert discussions into structured decisions
- Improve team accountability
- Support internal documentation workflows

Future version would integrate LLM-based reasoning using Claude.
""")