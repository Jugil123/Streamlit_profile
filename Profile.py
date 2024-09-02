import streamlit as st
import matplotlib.pyplot as plt

def profile():
    st.title("Profile")
    st.header("", divider="rainbow")

    # Skills Section
    st.write("## My Skills")
    st.write("""
        **🛠 Programming Languages:** Python, JavaScript, Java, C   
        **📚 Frameworks:** React Native, React, Django, Spring  
        **🛠 Tools:** Git, Github  
        **🗄️Database:** MySQL, SQLite, MongoDB
    """)

    st.write("## Choose an Option")
    choice = st.selectbox("Select a category:", ["Expertise", "Project Frameworks", "Programming Language Work Time"])
    
    if choice == "Expertise":
        languages = ["Python", "JavaScript", "Java", "C"]
        expertise_levels = [50, 20, 60, 10]  # Percentage of expertise
        
        # Create a chart
        fig, ax = plt.subplots()
        ax.bar(languages, expertise_levels, color='skyblue')
        ax.set_xlabel('Programming Languages')
        ax.set_ylabel('Expertise Level (%)')
        ax.set_title('Expertise in Programming Languages')
        
        st.pyplot(fig)

    elif choice == "Project Frameworks":
        st.header("InfoHaven", divider="gray")
        st.write("""
            **Tech Stack:**
            - **Framework:** Django
            - **Database:** SQLite
        """)

        st.header("FlightWay", divider="gray")
        st.write("""
            **Tech Stack:**
            - **Framework:** Django
            - **Database:** MySQL
        """)

        st.header("JapLearn", divider="gray")
        st.write("""
            **Tech Stack:**
            - **Frontend:** React Native
            - **Backend:** Spring Boot
            - **Database:** MongoDB
        """)

        st.header("Nurture Hub", divider="gray")
        st.write("""
            **Tech Stack:**
            - **Frontend:** React
            - **Backend:** Spring Boot
            - **Database:** MySQL
        """)

    elif choice == "Programming Language Work Time":
        st.header("Programming Language Work Time")

        labels = ["Python", "JavaScript", "Java", "C"]
        sizes = [25, 30, 30, 15]  # Percentage of time spent
        colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99']

        # Create a pie chart
        fig, ax = plt.subplots()
        ax.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', shadow=False, startangle=140)
        ax.axis('equal')

        st.pyplot(fig)