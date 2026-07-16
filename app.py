import streamlit as st

st.set_page_config(
    page_title="Context Recovery Agent",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ===========================
# SIDEBAR
# ===========================

with st.sidebar:

    st.title("🤖 Context Recovery Agent")

    st.markdown("---")

    st.success("AI Powered Project Manager")

    st.markdown("### Navigation")

    st.page_link("app.py", label="🏠 Home")
    st.page_link("pages/1_Create_Project.py", label="➕ Create Project")
    st.page_link("pages/2_Dashboard.py", label="📊 Dashboard")
    st.page_link("pages/3_Resume_Project.py", label="📂 Resume Project")
    st.page_link("pages/4_AI_Assistant.py", label="🤖 AI Assistant")

# ===========================
# HOME
# ===========================

st.title("🤖 Context Recovery Agent")

st.caption("Recover project context instantly with AI")

st.divider()

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Projects", "0")

with col2:
    st.metric("Completed Tasks", "0")

with col3:
    st.metric("Pending Tasks", "0")

st.divider()

st.subheader("🚀 Features")

c1, c2 = st.columns(2)

with c1:

    st.success("AI Project Planning")

    st.success("Context Recovery")

    st.success("Project Dashboard")

    st.success("Progress Tracking")

with c2:

    st.success("Resume Previous Work")

    st.success("AI Recommendations")

    st.success("Multi Project Support")

    st.success("Google Gemini Integration")

st.divider()

st.subheader("⚡ Quick Actions")

q1, q2, q3 = st.columns(3)

with q1:

    st.page_link(
        "pages/1_Create_Project.py",
        label="➕ Create Project",
        icon="🚀"
    )

with q2:

    st.page_link(
        "pages/2_Dashboard.py",
        label="📊 Dashboard",
        icon="📊"
    )

with q3:

    st.page_link(
        "pages/4_AI_Assistant.py",
        label="🤖 AI Assistant",
        icon="🤖"
    )

st.divider()

st.info("Built using Streamlit + Gemini AI + Google AI Studio")