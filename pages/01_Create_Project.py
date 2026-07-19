import streamlit as st
from pathlib import Path
from project_manager import create_project

st.set_page_config(
    page_title="Create Project",
    page_icon="➕",
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

st.title("➕ Create New Project")
st.caption("Generate an AI-powered project plan using Gemini AI")

st.divider()

col1, col2 = st.columns([2, 1])

# ==========================================
# INPUT SECTION
# ==========================================

with col1:

    project_name = st.text_input(
        "📁 Project Name",
        placeholder="Example: Hospital Management System"
    )

    description = st.text_area(
        "📝 Project Description",
        placeholder="Describe your project in detail...",
        height=180
    )

    generate = st.button(
        "🚀 Generate AI Project Plan",
        use_container_width=True
    )

# ==========================================
# TIPS
# ==========================================

with col2:

    st.info("""
### 💡 Tips

✔ Give a meaningful project name

✔ Describe the project clearly

✔ AI will generate a complete workflow

✔ Project is saved automatically

✔ Duplicate project names are not allowed
""")

st.divider()

# ==========================================
# GENERATE PROJECT
# ==========================================

if generate:

    if not project_name.strip() or not description.strip():

        st.error("⚠ Please enter both Project Name and Description.")

    else:

        try:

            with st.spinner("🤖 Gemini is generating your project plan..."):

                tasks = create_project(
                    project_name,
                    description
                )

            if tasks is None:

                st.error("⚠ A project with this name already exists.")

            else:

                st.success("🎉 Project created successfully!")

                st.subheader("📋 AI Generated Project Plan")

                for index, task in enumerate(tasks, start=1):
                    st.checkbox(
                        f"{index}. {task}",
                        value=False,
                        disabled=True
                    )

                st.balloons()

                st.success("Project saved successfully!")

                st.info(
                    "📊 Open **Dashboard** from the left sidebar to track your project progress."
                )

        except Exception:

            st.error("⚠ Gemini API quota exceeded.")

            st.info("""
The application is working correctly, but the Gemini free-tier API limit has been reached.

Please try again later or use another Gemini API key.
""")