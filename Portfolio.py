import streamlit as st

def portfolio():
    st.title("Portfolio")
    st.header("", divider="rainbow")

    # InfoHaven
    col1, col2 = st.columns([1, 3])
    with col1:
        st.image("Assets/InfoHaven.png", use_column_width=True)

    with col2:
        st.header("InfoHaven", divider="gray")
        st.write("""
            InfoHaven is a robust and efficient tool designed to optimize library operations. This system focuses on 
            automating and streamlining various functions, facilitating seamless interactions between library staff 
            and patrons. Key features include user account management, book search and retrieval, real-time updates 
            on book availability, and fine management. The aim is to elevate the library experience, boost operational 
            efficiency, and offer users a modern, user-friendly platform for accessing library services. 
            """)
        st.divider()

    # NurtureHub
    col1, col2 = st.columns([1, 3])
    with col1:
        st.image("Assets/nurturehub.png", use_column_width=True)

    with col2:
        st.header("NurtureHub", divider="gray")
        st.write("""
            NurtureHub is an innovative caregiving system designed to streamline and enhance the process of finding and
            booking caregivers for those in need of assistance. It serves as a comprehensive platform where individuals 
            requiring care—whether for themselves or a loved one—can easily browse through a diverse pool of qualified caregivers. 
            """)
        st.divider()

    # JapLearn
    col1, col2 = st.columns([1, 3])
    with col1:
        st.image("Assets/jplogo.png", use_column_width=True)

    with col2:
        st.header("JapLearn", divider="gray")
        st.write("""
            JapLearn is a mobile-based language learning application and reinforces the learning of the Japanese language. 
            JapLearn focuses on helping students learn characters, vocabulary, sentence construction and grammar. The 
            application allows teachers to manage classes, create and manage exercise content, and monitor student’s performance. 
            For students, they can learn with interactive exercises and monitor their performance. 
            """)
        st.divider()

    # FlightWay
    col1, col2 = st.columns([1, 3])
    with col1:
        st.image("Assets/flightlogo.png", use_column_width=True)

    with col2:
        st.header("FlightWay", divider="gray")
        st.write("""
            FlightWay a secure and user-friendly travel booking system that includes features for admin-side booking management, 
            user-side booking and history, diverse travel options, payment integration, notification systems, feedback mechanisms,
            scalable architecture, performance optimization, comprehensive documentation, and rigorous testing to ensure functionality, 
            security, and performance.
            """)
        st.divider()