import streamlit as st


def introduction():
    # Title
    st.title("About Me")
    st.header("",divider="rainbow")

    # Profile Image and About Me Section
    col1, col2 = st.columns([1, 2])

    with col1:
          st.image("Assets/Profile.png", width=200)

    with col2:
        st.write("""
            My name is Jugil P. Cabuenas, and I was born on August 17, 2002, in Cebu City. I am currently a student at Cebu Institute of Technology - University. Who I am today has been shaped by my experiences, the people I've met, and my education.

            Personal Life
                 
            I grew up in a close-knit family. As a young child, I was always curious about everything. I am surrounded by people who instill good values in me, shaping me into the person I am today. I enjoy cycling, playing table tennis, video games, and traveling. I also have a passion for photography.
            photography.   

            Achievements 
                 
            I won three consecutive table tennis championships during intramurals. I also achieved recognition as part of a high-performing group in the science diagnostic test in high school.

            Education 
                 
            My academic journey began at Colegio de la Inmaculada Concepción Cebu, where I stayed from nursery to high school. It became my second home, shaping me through the years I spent in that institution. After high school, I pursued higher education at Cebu Institute of Technology - University, majoring in Information Technology. My time at university has been transformative, providing me with the knowledge and skills to pursue my career aspirations.              
        """)