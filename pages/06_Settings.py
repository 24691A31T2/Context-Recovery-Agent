import streamlit as st
from pathlib import Path

st.set_page_config(
    page_title="Settings",
    page_icon="⚙️",
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

st.title("⚙️ Settings")
st.caption("Application Information")

st.divider()

# ==========================================
# APPLICATION
# ==========================================

st.subheader("📌 Application")

st.info("""
**Context Recovery Agent**

**Version:** 1.0

**Built With:**

- 🐍 Python
- 🎈 Streamlit
- 🤖 Google Gemini AI
- ☁️ Google AI Studio
""")

st.divider()

# ==========================================
# DEVELOPERS
# ==========================================

st.subheader("👨‍💻 Developers")

st.success("""
👩 **Addanki Thanvitha**

👩 **Peddapolu Suma**
""")

st.divider()

# ==========================================
# TECHNOLOGIES
# ==========================================

st.subheader("🛠️ Technologies Used")

st.write("• Python")
st.write("• Streamlit")
st.write("• Google Gemini API")
st.write("• JSON Storage")
st.write("• CSS")

st.divider()

# ==========================================
# FUTURE IMPROVEMENTS
# ==========================================

st.subheader("🚀 Future Improvements")

st.write("• User Authentication")
st.write("• Cloud Database")
st.write("• Team Collaboration")
st.write("• Project Analytics")
st.write("• Email Notifications")
st.write("• Mobile Responsive UI")