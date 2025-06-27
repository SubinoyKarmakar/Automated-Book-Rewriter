try:        # This will safely import the configured URL from the settings file
    from config_settings import URL
except ModuleNotFoundError:
    raise ModuleNotFoundError("'config_settings.py' not found. Please ensure it is in the same directory as 'main.py'.")

from scraper import fetch_chapter_text
from ai_writer import ai_writer
from storage import save_version
from retriever import store_in_memory

def run_pipeline():     # This function runs the full automated pipeline
    original = fetch_chapter_text(URL)
    ai_version = ai_writer(original)
    human_version = ai_version

    # It will save all versions to disk
    save_version({
        "original": original,
        "ai": ai_version,
        "human": human_version
    }, "chapter1")

    # It will store the final version in memory for quick access
    store_in_memory("chapter1", human_version, {
        "status": "final",
        "source": URL
    })

if __name__ == "__main__":
    run_pipeline()      # It will run the pipeline when the script is executed directly