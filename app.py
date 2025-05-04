import streamlit as st
import pandas as pd
import os
import re
import random


# Set page configuration ONCE
st.set_page_config(page_title="My Portfolio", layout="centered")

# Inject CSS for sidebar background and button styling
st.markdown("""
    <style>
    /* Change sidebar background color */
    [data-testid="stSidebar"] {
        background-color: #1f2937; /* Dark gray */
    }

    /* Style all buttons in sidebar */
    [data-testid="stSidebar"] button {
        background-color: #2563eb;
        color: white;
        font-size: 18px;
        margin: 6px 0px;
        border-radius: 8px;
        height: 50px;
    }

    [data-testid="stSidebar"] button:hover {
        background-color: #1d4ed8;
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar Navigation
st.sidebar.markdown("## 🚀 Navigation")

# Initialize session state
if "page" not in st.session_state:
    st.session_state["page"] = "Home"

# Navigation buttons
if st.sidebar.button("🏠 Home"):
    st.session_state["page"] = "Home"
if st.sidebar.button("🙋 About Me"):
    st.session_state["page"] = "About Me"
if st.sidebar.button("💼 Projects"):
    st.session_state["page"] = "Projects"
if st.sidebar.button("📬 Contact"):
    st.session_state["page"] = "Contact"

page = st.session_state["page"]

# Content based on selected page
if page == "Home":
    st.title("👋 Welcome to My Portfolio")
    st.header("Home")
    st.markdown("""
    <div style='text-align: center; font-size: 22px;'>
        🚀 <strong>Hi, I'm Syed Muhammad Hyder Zaidi!</strong><br>
        Python Developer | Streamlit Enthusiast | Tech Explorer 🧠💡<br><br>
        <span style='font-size:18px;'>Welcome to my portfolio. Let's build something cool together! 🔧👨‍💻</span>
    </div>
""", unsafe_allow_html=True)
    

    st.image("HYDER.jpeg")
    
    with st.expander("🛤️ My Developer Journey"):
        st.markdown("""
    - 📍 **2024**: Started Python
    - 🧠 **2025**: Built my first app with Streamlit
    - 🚀 **2026**: Exploring AI & deploying full-stack projects
    """)
        
    projects = [
    ("BMI Calculator", "A tool for calculating health metrics."),
    ("Madlibs", "A fun fill-in-the-blanks story generator."),
    ("Data Sweeper", "Cleans messy datasets easily.")
    ]

    project = random.choice(projects)
    st.markdown(f"### 🎯 Project Spotlight: **{project[0]}**")
    st.write(project[1])
    


elif page == "About Me":
    st.title("👋 Welcome to My Portfolio")
    st.header("About Me")
    st.write("""
        I'm a Python Programme Developer with experience in Python Programming. 
        I love building tools that make life easier.

        **Skills**:
        - Python
        - Streamlit
        - Web Development
        - Data Analysis
    """)
    col1, col2, col3 = st.columns(3)
    col1.metric("Projects", "10+")
    col2.metric("Years of Experience", "1+")
    col3.metric("Clients", "0")


elif page == "Projects":
    st.title("👋 Welcome to My Portfolio")
    st.header("Projects")

    st.subheader("💪 Project 1: BMI Calculator")
    st.write("It is a simple project that calculates a user's Body Mass Index based on their height and weight to assess health status.")

    st.subheader("🤔 Project 2: Number Guessing Game")
    st.write("It challenges the user to guess a randomly generated number within a specified range using hints for guidance.")

    st.subheader("🧐 Project 3: Hangman Game")
    st.write("It is a word-guessing game where the player tries to guess a hidden word letter by letter before running out of attempts.")

    st.subheader("👊📄✂ Project 4: Rock Paper Scissor Game")
    st.write("It lets the user play the classic hand game against the computer using random choices and simple logic to determine the winner.")

    st.subheader("🔁 Project 5: Password Generator")
    st.write("It creates strong, random passwords using combinations of letters, numbers, symbols, and core password to enhance security.")

    st.subheader("💪 Project 6: Password Stength Meter")
    st.write("It evaluates the strength of a given password by analyzing its length, complexity, and character variety to suggest improvements.")

    st.subheader("♻ Project 7: Unit Converter")
    st.write("It allows users to convert between different units of measurement, such as length, weight, and temperature, with ease.")

    st.subheader("📚 Project 8: Libraray Manager")
    st.write("It helps manage a library's inventory by allowing users to add, remove, and search for books, along with tracking book availability.")

    st.subheader("🧹 Project 9: Data sweeper")
    st.write("It automates the process of cleaning and organizing datasets by removing duplicates, handling missing values, and standardizing data formats.")

    st.subheader("😜 Project 10: Madlibs")
    st.write("It generates a fun, fill-in-the-blank story by prompting the user to provide words for various categories like nouns, verbs, and adjectives.")


elif page == "Contact":
    st.title("👋 Welcome to My Portfolio")
    st.header("📬 Contact Me")

    # Function to save data
    def save_contact_info(name, email, message):
        df = pd.DataFrame([[name, email, message]], columns=["Name", "Email", "Message"])
        if os.path.exists("contacts.csv"):
            df.to_csv("contacts.csv", mode='a', header=False, index=False)
        else:
            df.to_csv("contacts.csv", index=False)

    with st.form("contact_form"):
        name = st.text_input("Your Name")
        email = st.text_input("Your Email")
        message = st.text_area("Your Message")
        submitted = st.form_submit_button("Send")

        if submitted:
            email_pattern = r"[^@]+@[^@]+\.[^@]+"  # Simple email regex

    if not name or not email or not message:
        st.error("Please fill in all fields.")
    elif not re.match(email_pattern, email):
        st.error("❌ Please enter a valid email address.")
    else:
        save_contact_info(name, email, message)
        st.success(f"✅ Thank you {name}, your message has been saved!")