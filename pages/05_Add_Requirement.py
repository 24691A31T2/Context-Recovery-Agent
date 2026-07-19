import streamlit as st
from pathlib import Path
from project_manager import list_projects, add_requirement

st.set_page_config(
    page_title="Add Requirement",
    page_icon="➕",
    layout="wide"
)
from pathlib import Path

def load_css():
    css_path = Path(__file__).parent.parent / "styles.css"

    if css_path.exists():
        with open(css_path) as f:
            st.markdown(
                f"<style>{f.read()}</style>",
                unsafe_allow_html=True
            )

load_css()
st.title("➕ Add New Requirement")
st.caption("Add a new pending task to an existing project")

# ==========================================
# LOAD PROJECTS
# ==========================================

projects = list_projects()

if not projects:
    st.warning("⚠ No projects available.")
    st.stop()

project_names = [project["project"] for project in projects]

selected_project = st.selectbox(
    "📁 Select Project",
    project_names
)

requirement = st.text_input(
    "📝 New Requirement",
    placeholder="Example: Email Notification Module"
)

# ==========================================
# ADD REQUIREMENT
# ==========================================

if st.button("➕ Add Requirement", use_container_width=True):

    if requirement.strip() == "":
        st.warning("⚠ Please enter a requirement.")

    else:

        success = add_requirement(
            selected_project,
            requirement
        )

        if success:

            st.success("✅ Requirement added successfully!")

            st.balloons()

            st.rerun()

        else:

            st.error("Unable to add requirement.")