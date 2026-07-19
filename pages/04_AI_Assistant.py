import streamlit as st
from pathlib import Path
from project_manager import list_projects
from memory import find_project
from agent import ask_ai

st.set_page_config(
    page_title="AI Assistant",
    page_icon="🤖",
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

st.title("🤖 AI Project Assistant")
st.caption("Ask Gemini anything about your project")

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

question = st.text_area(
    "💬 Ask your question",
    placeholder="""Example:

• What should I do next?
• Summarize my project.
• Which tasks are pending?
• What has been completed?
""",
    height=150
)

# ==========================================
# ASK AI
# ==========================================

if st.button("🤖 Ask Gemini", use_container_width=True):

    if question.strip() == "":
        st.warning("⚠ Please enter a question.")

    else:

        project = find_project(selected_project)

        if project is None:
            st.error("Project not found.")
            st.stop()

        try:

            with st.spinner("🤖 Gemini is thinking..."):

                answer = ask_ai(
                    project["project"],
                    project["completed"],
                    project["pending"],
                    question
                )

            st.subheader("🤖 AI Response")
            st.success(answer)

        except Exception:

            st.error("⚠ Gemini API quota exceeded.")

            st.info("""
The application is working correctly, but the Gemini free-tier API limit has been reached.

Please try again later or use another Gemini API key.
""")