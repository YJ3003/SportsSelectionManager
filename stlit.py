import streamlit as st
import os
import subprocess
# subprocess.check_call(["pip", "install", "-r", os.path.join(os.path.abspath("."), "requirements.txt")])
import tempCodeRunnerFile

# Install required libraries


try:
    # Create a session state
    st.title("SPORTS SELECTION MANAGER")
    if 'selected_sport' not in st.session_state:
        st.session_state.selected_sport = None

    # Create a select box to choose the sports group
    st.session_state.selected_sport = st.selectbox("Enter sports", tempCodeRunnerFile.sports_group, index=0)


    # Add a text input box with an initial value
    sub = st.text_input("Enter your subject:", value="<subject_line>")
    msg = st.text_input("Enter your message:", value="<message_line>")
    sport = st.session_state['selected_sport']

    # Send emails when the button is clicked
    if st.button("Send Emails"):
        tempCodeRunnerFile.send_emails(sport,sub, msg)
        st.write(f"Emails to {sport} sent successfully!")
    
    st.write(tempCodeRunnerFile.df)


except Exception as e:
    st.error(f"An error occurred: {e}")
