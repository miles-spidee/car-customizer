import streamlit as st

st.set_page_config(
    page_title="Akilan CK - Portfolio",
    page_icon=":rocket:",
)

st.markdown("""
    <style>
    .title {
        font-size: 50px;
        font-weight: bold;
        color: #0A4D68;
        text-align: center;
        padding: 20px;
    }
    .card {
        background-color: #f4f4f9;
        border-radius: 12px;
        padding: 7px;
        margin-bottom: 30px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    .card h3 {
        color: #3E8A7E;
        font-size: 26px;
        margin-bottom: 10px;
    }
    .card p {
        color: #444;
        font-size: 18px;
        line-height: 1.6;
    }
    .footer {
        text-align: center;
        color: #888;
        font-size: 14px;
        padding-top: 20px;
    }
    .btn-link {
        color: #3E8A7E;
        font-weight: bold;
        text-decoration: none;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<p class="title">My Portfolio</p>', unsafe_allow_html=True)

with st.container():
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.header("About Me")
    st.write("""
    Hello! I'm Akilan CK, a passionate programmer and mathematics enthusiast. 
    I have experience in front-end development and UI design. 
    I love to explore new technologies and work on creative projects.
    """)
    st.markdown('</div>', unsafe_allow_html=True)

with st.container():
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.header("Projects")
    st.subheader("Project 1: SPACETOUR")
    st.write("""
    - **Description**: An interactive website where you explore the wonders of space and enjoy a space-themed quiz.
    - **Tech**: HTML, CSS, JavaScript
    - [View Project](https://webcrafters-spacetour.netlify.app/)
    """)
    
    st.subheader("Project 2: Retro Cycling Club Site")
    st.write("""
    - **Description**: A responsive website for a cycling club, featuring modern designs and smooth UI.
    - **Tech**: HTML, CSS, JavaScript
    - [View Project](https://miles-spidee.github.io/club-site/)
    """)
    
    st.subheader("Project 3: XIONA")
    st.write("""
    - **Description**: A website for an AI company showcasing innovative solutions.
    - **Tech**: HTML, CSS, JavaScript
    - [View Project](https://miles-spidee.github.io/xiona/)
    """)
    st.markdown('</div>', unsafe_allow_html=True)

with st.container():
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.header("Skills")
    st.write("""
    - **Frontend Development**: HTML, CSS, JavaScript (Advanced)
    - **UI Design**: Responsive Design, Prototyping, User-Centered Design
    - **Tools**: Git, Figma, Visual Studio Code
    """)
    st.markdown('</div>', unsafe_allow_html=True)

with st.container():
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.header("Contact")
    st.write("""
    Feel free to reach out to me through any of the following platforms:
    - [GitHub](https://github.com/miles-spidee)
    - [Discord Server](https://discord.gg/6QEMZ5nxdB)
    """)
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<p class="footer">Thank you for visiting my portfolio!</p>', unsafe_allow_html=True)
