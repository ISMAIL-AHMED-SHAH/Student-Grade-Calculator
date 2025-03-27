import streamlit as st

# 🎨 Set Page Configuration
st.set_page_config(page_title="Student Grades Calculator", page_icon="🎓", layout="wide")

# 🎨 Custom CSS for Styling
st.markdown(
    """
    <style>
        .stApp {
            background-color: #222222;
        }
        .stButton>button {
            background-color: #6A0DAD !important;
            color: white;
            font-weight: bold;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# 🎯 Initialize Session State
if "scores" not in st.session_state:
    st.session_state.scores = []
    st.session_state.average = None
    st.session_state.grade = None
    st.session_state.calculated = False

# 📌 Function to Calculate Grade
def calculate_grade(scores):
    if not scores:
        return None, None

    avg_score = sum(scores) / len(scores)

    if avg_score >= 90:
        grade = "A 🎉 Excellent!"
    elif avg_score >= 80:
        grade = "B 😊 Good Job!"
    elif avg_score >= 70:
        grade = "C 🙂 Keep Improving!"
    elif avg_score >= 60:
        grade = "D 😐 Needs More Effort!"
    else:
        grade = "F ❌ Try Again!"

    return avg_score, grade

# 🎯 UI Layout
st.title("🎓 Student Grades Calculator")
st.subheader("Easily calculate grades with an intuitive UI! 📊")

# 📌 Get User Input for Scores
st.write("Enter student scores (0 - 100):")

num_subjects = st.number_input("Number of Subjects:", min_value=1, max_value=10, step=1, value=5)

st.session_state.scores = []
for i in range(num_subjects):
    score = st.number_input(f"Score for Subject {i+1}:", min_value=0, max_value=100, step=1)
    st.session_state.scores.append(score)

# 📌 Calculate Button
if st.button("📊 Calculate Grade"):
    st.session_state.average, st.session_state.grade = calculate_grade(st.session_state.scores)
    st.session_state.calculated = True

# 📊 Display Results
if st.session_state.calculated:
    st.write("---")
    st.write(f"📌 **Average Score:** `{st.session_state.average:.2f}`")
    st.write(f"🎯 **Grade:** `{st.session_state.grade}`")

# 🔄 Restart Button
if st.button("🔄 Reset Calculator"):
    st.session_state.scores = []
    st.session_state.average = None
    st.session_state.grade = None
    st.session_state.calculated = False
    st.experimental_rerun()

# 📌 SIDEBAR WITH TIPS & CONTACT INFO
st.sidebar.title("📌 Study Tips")
st.sidebar.info("""
- ✅ **Practice makes perfect!** Solve problems daily.
- 📝 **Understand concepts** instead of memorizing.
- ⏳ **Manage your time** effectively during exams.
- 🔄 **Revise regularly** to reinforce learning.
""")

# 📬 Contact Section
st.sidebar.markdown("---")
st.sidebar.markdown("### 📬 Contact")
st.sidebar.write("📧 [Email Us](mailto:ismailahmedshahpk@gmail.com)")
st.sidebar.write("🔗 [LinkedIn](https://www.linkedin.com/in/ismail-ahmed-shah-2455b01ba/)")
st.sidebar.write("💬 [WhatsApp](https://wa.me/923322241405)")
