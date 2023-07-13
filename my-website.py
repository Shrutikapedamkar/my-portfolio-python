import streamlit as st
import requests
from streamlit_lottie import st_lottie

import time,os,sys



st.set_page_config(page_title="My webpage", page_icon=":woman:", layout="wide")

#function to load lottie json file
def load_lottieURL(url) :
    req = requests.get(url)
    #Status_code=200 means connection successful
    if req.status_code !=200 :
        return None
    return req.json()

#call the function and pass the lottie json url
lottie_animation = load_lottieURL("https://lottie.host/820240dd-6ec5-4059-b743-37faa33f4821/39LYRISCPL.json")

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style.css")

def typingPrint(text):
    st.title(text)
    sys.stdout.flush()
    time.sleep(0.60)

#HEADER
with st.container():
    typingPrint('Hello! I am Shrutika')
    time.sleep(0.60)
    st.subheader("An experienced Software Engineer with a Master's degree in \
             Artificial Intelligence.")
    time.sleep(0.60)
    st.write("connect with me on [LinkedIn] (https://www.linkedin.com/in/shrutika-pedamkar-473758170/)")

#What I DO

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        time.sleep(0.60)
        st.write("I've spent years delving into the depths of programming languages, \
                  working on huge databases, and bending algorithms to my will. \
                  Basically a typical tech geek.")
        time.sleep(0.60)
        st.write("What sets me apart is my keen interest in exploring the frontiers of technology. \
                 I have honed my skills in various machine learning algorithms, natural language processing, and data analysis techniques. \
                 I have even undertaken projects in sentiment analysis and supervised/unsupervised learning, where I processed and analyzed large volumes \
                 of data to derive meaningful insights.")
        time.sleep(0.60)
        st.write("As a technology enthusiast, I am always eager to learn and adapt to new technologies \
                 and programming languages. With a strong foundation in software engineering principles and an ability to think critically and problem-solve, \
                 I strive to create innovative and user-friendly applications. If you are seeking a passionate and dedicated professional \
                 who can contribute their skills and experience to your organization, look no further. I am excited about challenging assignments and \
                 opportunities for professional growth. I currently reside in Manchester and I am open to relocation.")

    with right_column:
        time.sleep(0.60)
        st_lottie(lottie_animation, key = "coding")

# CONTACT SECTION
    time.sleep(0.60)
    st.write("---")
    time.sleep(0.60)
    st.header("Get in Touch ")
    time.sleep(0.60)

    contact_form = """
    <form action="https://formsubmit.co/shrutikapedamkar97@gmail.com" method="POST">
        <input type = "hidden" name= "_captcha" value = "false">
        <input type="text" name="name" placeholder = "Your name" required>
        <input type="email" name="email" placeholder = "Your email" required>
        <textarea name = "message" placeholder = "Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>"""

    left_column, right_column = st.columns(2)
    with left_column :
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()
