import traceback

import streamlit as st

from pipeline import run_research_pipeline


st.set_page_config(page_title="AI Research Studio Powered by Bonami Solutions", page_icon="🔎", layout="wide")
st.title("AI Research Studio Powered by Bonami Solutions")
st.caption("Research topic → Search → Read → Write → Critique")


with st.form("research_form"):
    topic = st.text_input(
        "Research topic",
        placeholder="Enter any topic, for example: India economy 2025",
        help="The pipeline will search the web, select a relevant result, scrape it, write a report, and critique it.",
    )
    submitted = st.form_submit_button("Run research")


if submitted and topic.strip():
    try:
        with st.spinner("Running pipeline... This may take a few moments."):
            state = run_research_pipeline(topic.strip())

        st.success("Research completed successfully.")

        tabs = st.tabs(["Search result", "Scraped content", "Final report", "Critic feedback", "Raw state"])

        with tabs[0]:
            st.subheader("Search result")
            search_result = state.get("search_result", "")
            st.text_area("Search result", search_result, height=260)

        with tabs[1]:
            st.subheader("Scraped content")
            scraped_content = state.get("scraped_content", "")
            st.text_area("Scraped content", scraped_content, height=320)

        with tabs[2]:
            st.subheader("Final report")
            report = state.get("report", "")
            st.markdown(report)

        with tabs[3]:
            st.subheader("Critic feedback")
            feedback = state.get("feedback", "")
            st.text_area("Critic feedback", feedback, height=280)

        with tabs[4]:
            st.subheader("Pipeline raw state")
            st.json(state)

    except Exception as exc:
        st.error("The pipeline failed while running.")
        st.code(traceback.format_exc())
        st.warning("If Groq is rate-limited or unavailable, the app will still show the error here instead of crashing the UI.")
else:
    st.info("Enter a topic and press Run research to begin.")
