import streamlit as st
from pathlib import Path
from datetime import datetime
from memory import get_statistics, get_all_projects

st.set_page_config(
    page_title="🏠 Home",
    page_icon="🏠",
    layout="wide"
)

# ==========================================
# LOAD CSS
# ==========================================

def load_css():
    css_path = Path(__file__).parent / "styles.css"

    if css_path.exists():
        with open(css_path) as f:
            st.markdown(
                f"<style>{f.read()}</style>",
                unsafe_allow_html=True
            )

load_css()

# ==========================================
# LOAD DATA
# ==========================================

stats = get_statistics()
projects = get_all_projects()

# ==========================================
# HEADER
# ==========================================

st.title("🤖 Context Recovery Agent")

st.caption("AI-Powered Project Memory & Context Recovery System")

st.success("🚀 Version 1.0")

st.caption(f"📅 Today: {datetime.now().strftime('%d %B %Y')}")

st.success("""
### 👋 Welcome!

Recover your work instantly using AI.

✔ AI Project Planning

✔ Context Recovery

✔ Smart Dashboard

✔ Gemini AI Assistant
""")

st.info(
    "💡 *Never lose your project context again. Let AI remember where you left off.*"
)

st.divider()

# ==========================================
# METRICS
# ==========================================

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("📁 Total Projects", stats["projects"])

with col2:
    st.metric("✅ Completed Tasks", stats["completed"])

with col3:
    st.metric("📌 Pending Tasks", stats["pending"])

with col4:
    st.metric(
        "📝 Total Tasks",
        stats["completed"] + stats["pending"]
    )

# ==========================================
# OVERALL PROGRESS
# ==========================================

total = stats["completed"] + stats["pending"]

overall_progress = (
    round((stats["completed"] / total) * 100)
    if total > 0 else 0
)

st.subheader("📈 Overall Progress")

st.progress(overall_progress)

st.write(f"### {overall_progress}% Completed")

st.divider()

# ==========================================
# KEY FEATURES
# ==========================================

st.subheader("🚀 Key Features")

left, right = st.columns(2)

with left:

    st.success("🤖 AI Project Planning")
    st.success("📂 Context Recovery")
    st.success("📊 Progress Tracking")
    st.success("📈 Interactive Dashboard")

with right:

    st.success("🧠 Gemini AI Assistant")
    st.success("📁 Multi Project Support")
    st.success("☁️ Google AI Studio")
    st.success("⚡ Smart Task Management")

st.divider()

# ==========================================
# RECENT PROJECTS
# ==========================================

st.subheader("📁 Recent Projects")

if projects:

    for project in projects[-5:][::-1]:

        completed = len(project["completed"])
        pending = len(project["pending"])
        total_tasks = completed + pending

        progress = (
            round((completed / total_tasks) * 100)
            if total_tasks > 0 else 0
        )

        with st.container(border=True):

            st.markdown(f"### 📂 {project['project']}")

            st.write(project["description"])

            st.caption(
                f"📅 Created : {project.get('created_date', 'Not Available')}"
            )

            st.caption(
                f"🕒 Last Updated : {project.get('last_updated', 'Not Available')}"
            )

            st.progress(progress)

            st.caption(
                f"📊 Progress : {progress}% | "
                f"✅ Completed : {completed} | "
                f"📌 Pending : {pending}"
            )

else:

    st.info("""
👋 No projects found.

Create your first project from the **Create Project** page.
""")

st.divider()

# ==========================================
# NAVIGATION
# ==========================================

st.info("👈 Use the left sidebar to navigate through the application.")

st.markdown("---")

# ==========================================
# FOOTER
# ==========================================

st.caption(
    "👩‍💻 Developed by **Addanki Thanvitha** & **Peddapolu Suma** | "
    "🤖 Agentic AI Internship • 2026"
)