import streamlit as st
from pathlib import Path
from project_manager import list_projects, resume_project

st.set_page_config(
    page_title="Resume Project",
    page_icon="📂",
    layout="wide"
)

# ==========================================
# LOAD CSS
# ==========================================

def load_css():
    css_path = Path(__file__).parent.parent / "styles.css"

    if css_path.exists():
        with open(css_path) as f:
            st.markdown(
                f"<style>{f.read()}</style>",
                unsafe_allow_html=True
            )

load_css()

# ==========================================
# PAGE
# ==========================================

st.title("📂 Resume Project")
st.caption("Recover your previous work using Gemini AI")

st.divider()

# ==========================================
# LOAD PROJECTS
# ==========================================

projects = list_projects()

if not projects:
    st.warning("⚠ No projects found. Please create a project first.")
    st.stop()

project_names = [project["project"] for project in projects]

selected_project = st.selectbox(
    "📁 Select Project",
    project_names
)

# ==========================================
# RESUME PROJECT
# ==========================================

if st.button("🤖 Resume Project", use_container_width=True):

    try:

        with st.spinner("🤖 Gemini is generating your project summary..."):

            summary = resume_project(selected_project)

        st.success("✅ Project Summary Generated")
        st.markdown(summary)

    except Exception:

        st.error("⚠ Gemini API quota exceeded.")

        st.info("""
The application is working correctly, but the Gemini free-tier API limit has been reached.

Please try again later or use another Gemini API key.
""")