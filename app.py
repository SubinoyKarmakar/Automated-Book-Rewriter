import streamlit as st
import os
from scraper import fetch_chapter_text
from ai_writer import ai_writer
from storage import save_version, load_version
from retriever import store_in_memory
from config_settings import URL

# Setting Streamlit app title and page title
st.set_page_config(page_title="Automated Book Publication")
st.title("Automated Book Chapter Rewriter")

# Initialize session state
if "original" not in st.session_state:
    st.session_state.original = ""
if "ai_version" not in st.session_state:
    st.session_state.ai_version = ""

# Fetch chapter
if st.button("Fetch Chapter"):
    with st.spinner("Fetching original text..."):
        st.session_state.original = fetch_chapter_text(URL)
    st.success("Chapter fetched Successfully!")

# Show original text
if st.session_state.original:
    st.text_area("Original Chapter Text Extracted From Given URL", st.session_state.original, height=200)

    # Prompt input
    prompt = st.text_input("Enter AI rewrite instruction", key="prompt_input")

    # AI Rewrite
    if st.button("AI Rewrite"):
        with st.spinner("AI rewriting..."):
            st.session_state.ai_version = ai_writer(st.session_state.original, prompt)
        st.success("AI version generated!")

# Show AI and Human Edit Areas
if st.session_state.ai_version:
    st.text_area("AI Rewritten Text", st.session_state.ai_version, height=200)
    human_input = st.text_area("Your Edits", st.session_state.ai_version, height=200)

    # Save Final Version
    if st.button("Save Final Version"):
        save_version({
            "original": st.session_state.original,
            "ai": st.session_state.ai_version,
            "human": human_input
        }, "chapter1")

        store_in_memory("chapter1", human_input, {
            "status": "final",
            "source": URL
        })

        st.success("Final version saved!")

st.markdown("---")
st.subheader("View Saved Versions")

# List JSON files in /data
saved_files = [f.replace(".json", "") for f in os.listdir("data") if f.endswith(".json")]
if saved_files:
    selected_version = st.selectbox("Choose a version to view", saved_files)

    if st.button("Load Selected Version"):
        version = load_version(selected_version)
        if version:
            st.text_area("Original", version["original"], height=200)
            st.text_area("AI Rewritten", version["ai"], height=200)
            st.text_area("Human Edited", version["human"], height=200)
        else:
            st.error("Version not found.")
else:
    st.info("No saved versions found yet.")
