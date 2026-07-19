import streamlit as st
import plotly.express as px
from pathlib import Path

from project_manager import (
    list_projects,
    get_dashboard,
    complete_task,
    remove_project
)

from agent import suggest_next_task

st.set_page_config(
    page_title="Dashboard",
    page_icon="📊",
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
# PAGE HEADER
# ==========================================

st.title("📊 Project Dashboard")
st.caption("Monitor your project progress and manage tasks.")

st.divider()

# ==========================================
# LOAD PROJECTS
# ==========================================

projects = list_projects()

if not projects:
    st.warning("⚠ No projects found.")
    st.info("Create a project first from the Home page.")
    st.stop()

project_names = [project["project"] for project in projects]

selected_project = st.selectbox(
    "📁 Select Project",
    project_names
)

dashboard = get_dashboard(selected_project)

if dashboard is None:
    st.error("Unable to load project.")
    st.stop()

progress = dashboard["progress"]

# ==========================================
# METRICS
# ==========================================

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("📈 Progress", f"{progress}%")

with col2:
    st.metric("✅ Completed", len(dashboard["completed"]))

with col3:
    st.metric("📌 Pending", len(dashboard["pending"]))

st.progress(progress)

st.divider()

# ==========================================
# PIE CHART
# ==========================================

chart_data = {
    "Status": ["Completed", "Pending"],
    "Tasks": [
        len(dashboard["completed"]),
        len(dashboard["pending"])
    ]
}

fig = px.pie(
    chart_data,
    names="Status",
    values="Tasks",
    hole=0.45,
    title="Task Distribution"
)

st.plotly_chart(fig, use_container_width=True)

st.divider()

# ==========================================
# TASKS
# ==========================================

left, right = st.columns(2)

# ------------------------------------------
# COMPLETED TASKS
# ------------------------------------------

with left:

    st.subheader("✅ Completed Tasks")

    if dashboard["completed"]:

        for task in dashboard["completed"]:
            st.success(task)

    else:
        st.info("No completed tasks yet.")

# ------------------------------------------
# PENDING TASKS
# ------------------------------------------

with right:

    st.subheader("📌 Pending Tasks")

    if dashboard["pending"]:

        selected_task = st.selectbox(
            "Choose a task",
            dashboard["pending"]
        )

        if st.button(
            "✅ Mark as Completed",
            use_container_width=True
        ):

            success = complete_task(
                dashboard["project"],
                selected_task
            )

            if success:
                st.success("Task completed successfully!")
                st.rerun()
            else:
                st.error("Unable to update task.")

        st.markdown("---")

        st.subheader("Remaining Tasks")

        for task in dashboard["pending"]:
            st.warning(task)

    else:

        st.balloons()

        st.success("🏆 Project Completed Successfully!")

        st.info(f"""
### 📁 {dashboard["project"]}

**Progress:** 100%

**Completed Tasks:** {len(dashboard["completed"])}

**Created:** {dashboard.get("created_date", "Not Available")}

**Last Updated:** {dashboard.get("last_updated", "Not Available")}

Your project has been completed successfully.
""")

        keep_col, delete_col = st.columns(2)

        with keep_col:

            if st.button(
                "📂 Keep Project",
                use_container_width=True
            ):
                st.success("Project retained successfully.")

        with delete_col:

            if st.button(
                "🗑 Delete Project",
                use_container_width=True
            ):
                remove_project(dashboard["project"])
                st.success("Project deleted successfully!")
                st.rerun()

st.divider()

# ==========================================
# AI RECOMMENDATION
# ==========================================

st.subheader("🤖 AI Recommendation")

if dashboard["pending"]:

    try:

        recommendation = suggest_next_task(
            dashboard["project"],
            dashboard["pending"]
        )

        st.info(recommendation)

    except Exception:

        st.warning(
            "⚠ AI recommendation is currently unavailable."
        )

else:

    st.success("🎉 All tasks have been completed.")

st.divider()

# ==========================================
# PROJECT DETAILS
# ==========================================

with st.expander("📄 Project Details"):

    st.write("### 📁 Project Name")
    st.write(dashboard["project"])

    st.write("### 📝 Description")
    st.write(dashboard["description"])

    st.write("### 📅 Created On")
    st.write(dashboard.get("created_date", "Not Available"))

    st.write("### 🕒 Last Updated")
    st.write(dashboard.get("last_updated", "Not Available"))

    st.write("### 📊 Progress")
    st.write(f"{dashboard['progress']}%")

    st.write("### 📋 Total Tasks")
    st.write(
        len(dashboard["completed"]) +
        len(dashboard["pending"])
    )

    st.write("### ✅ Completed Tasks")
    st.write(len(dashboard["completed"]))

    st.write("### 📌 Pending Tasks")
    st.write(len(dashboard["pending"]))