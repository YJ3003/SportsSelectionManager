import streamlit as st
import os
import subprocess
import json
# subprocess.check_call(["pip", "install", "-r", os.path.join(os.path.abspath("."), "requirements.txt")])
# result_str = subprocess.run(["python", "tempCodeRunnerFile.py"], capture_output=True, text=True)
# result_dict = json.loads(result_str.stdout)
# df = result_dict['df']
# sports_group = result_dict['sports_group']
# send_emails = result_dict['send_emails']
# from tempCodeRunnerFile import df, sports_group, send_emails

def run_script(script_path):
    with open(script_path, 'r') as file:
        script_code = file.read()
    result_dict = {}
    exec(script_code, result_dict)
    return result_dict

result_dict = run_script("tempCodeRunnerFile.py")
df = result_dict['df']
sports_group = result_dict['sports_group']
send_emails = result_dict['send_emails']

# Install required libraries


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
