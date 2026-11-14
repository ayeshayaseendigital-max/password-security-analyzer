
import streamlit as st
from password_checker import analyze_password
import secrets
import string
from st_copy_to_clipboard import st_copy_to_clipboard


def generate_password(length=16):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password


st.set_page_config(
    page_title="Password Security Analyzer",
    page_icon="🔐",
    layout="centered"
)

st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #101827, #243b55);
}

h1 {
    color: #ffffff !important;
    text-align: center;
    font-size: 38px !important;
}

p {
    color: #dbeafe;
}

.stButton > button {
    background-color: #2563eb;
    color: white;
    border-radius: 10px;
    border: none;
    padding: 10px 25px;
    font-weight: bold;
}

.stButton > button:hover {
    background-color: #1d4ed8;
    color: white;
}

.stTextInput input {
    border-radius: 10px;
}

h2, h3 {
    color: #ffffff !important;
}

.stAlert p {
    color: #1f2937 !important;
    font-weight: 600;
}

.stMarkdown p {
    color: #e2e8f0;
}
</style>
""", unsafe_allow_html=True)


st.title("🔐 Password Security Analyzer")
st.write("Check the strength of your password.")


# PASSWORD GENERATOR
st.subheader("🔐 Generate a Strong Password")

password_length = st.slider(
    "Choose Password Length",
    min_value=8,
    max_value=32,
    value=16,
    step=1
)

if "generated_password" not in st.session_state:
    st.session_state.generated_password = ""

if st.button("Generate Password"):
    st.session_state.generated_password = generate_password(password_length)
    st.success("Strong password generated successfully!")

if st.session_state.generated_password:
    st.code(st.session_state.generated_password)

    st.caption("📋 Click the icon to copy")

    st_copy_to_clipboard(st.session_state.generated_password)


st.markdown("---")


# PASSWORD CHECKER
password = st.text_input(
    "Enter your password:",
    type="password",
    placeholder="Type your password here"
)

if st.button("Check Password"):

    if password:
        result = analyze_password(password)

        st.write(f"Score: {result['score']}/7")

        if result["strength"] == "Weak":
            st.error("Your password is weak! Improve it.")

        elif result["strength"] == "Moderate":
            st.warning("Your password is moderately strong.")

        else:
            st.success("Excellent! Your password is strong.")

        score = result["score"]

        st.write(f"Password Strength Meter: {score}/7")
        st.progress(score / 7)

        st.write("### 🔍 Security Checklist")

        for check, passed in result["checks"].items():
            if passed:
                st.write("✅", check)
            else:
                st.write("❌", check)

        if result["feedback"]:
            st.write("### Recommendations")

            for suggestion in result["feedback"]:
                st.write("⚠️", suggestion)

        else:
            st.success("Your password meets all the listed checks!")

    else:
        st.warning("Please enter a password first.")


st.caption(
    "Educational password checker. Do not enter real account passwords."
)

st.markdown("---")


# PASSWORD SECURITY TIPS
st.subheader("🔐 Password Security Tips")

tips = [
    "Use at least 12 characters for better security.",
    "Use a unique password for every account.",
    "Avoid names, birthdays, and common words.",
    "Never share your passwords with anyone.",
    "Use a trusted password manager.",
    "Enable Two-Factor Authentication (2FA).",
    "Never enter your real password into untrusted websites."
]

for tip in tips:
    st.info("🔒 " + tip)
