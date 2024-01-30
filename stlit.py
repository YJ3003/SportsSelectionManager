import streamlit as st
import os
import subprocess
from tempCodeRunnerFile import df, sports_group, send_emails

# Install required libraries
subprocess.check_call(["pip", "install", "-r", os.path.join(os.path.abspath("."), "requirements.txt")])

try:
    # Create a session state
    st.title("SPORTS SELECTION MANAGER")
    if 'selected_sport' not in st.session_state:
        st.session_state.selected_sport = None

    # Create a select box to choose the sports group
    st.session_state.selected_sport = st.selectbox("Enter sports", sports_group, index=0)


    # Add a text input box with an initial value
    sub = st.text_input("Enter your subject:", value="<subject_line>")
    msg = st.text_input("Enter your message:", value="<message_line>")
    sport = st.session_state['selected_sport']

    # Send emails when the button is clicked
    if st.button("Send Emails"):
        send_emails(sport,sub, msg)
        st.write(f"Emails to {sport} sent successfully!")
    
    st.write(df)


except Exception as e:
    st.error(f"An error occurred: {e}")
