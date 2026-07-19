import streamlit as st
from pathlib import Path
from project_manager import list_projects, remove_project

st.set_page_config(
    page_title="Delete Project",
    page_icon="🗑️",
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

st.title("🗑️ Delete Project")
st.caption("Permanently remove a project from the application")

st.divider()

projects = list_projects()

if not projects:
    st.warning("⚠️ No projects available.")
    st.stop()

project_names = [project["project"] for project in projects]

selected_project = st.selectbox(
    "📁 Select Project",
    project_names
)

st.warning("⚠️ This action is permanent and cannot be undone.")

if st.button(
    "🗑️ Delete Project",
    use_container_width=True
):

    remove_project(selected_project)

    st.success(
        f"✅ '{selected_project}' has been deleted successfully!"
    )

    st.balloons()

    st.rerun()