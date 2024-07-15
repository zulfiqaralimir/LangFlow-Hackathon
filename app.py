# cd /c/Users/STONE/Documents/LangFlow2/langflow_chatbot_env/Scripts
# pip install streamlit
# activate langflow_chatbot_env
# streamlit run app.py

# 
# 
# cmd //c streamlit.cmd run app.py


import streamlit as st
import requests
import json

st.markdown(
    """
    <style>
    /* Title color */
    h1 {
        color: green;
    }
    </style>
    """,
    unsafe_allow_html=True
)
st.title('Codemate - Your Coding Tutor')
st.header('LangFlow Chatbot using Llama3 80b')

# Sidebar menu for user profile
menu = ["Profile", "Settings", "Help"]
choice = st.sidebar.selectbox("Menu", menu)

# Function to display different sections based on user choice
if choice == "Profile":
    st.subheader("User Profile")
    # Add user profile details here
elif choice == "Settings":
    st.subheader("Settings")
    # Add settings options here
elif choice == "Help":
    st.subheader("Help")
    # Add help information here

# Define a list of programming languages
programming_languages = ['Python', 'Java', 'JavaScript', 'C++', 'Ruby', 'PHP']

# Display a dropdown select box
selected_language = st.selectbox('Select a programming language', programming_languages)

# Show the selected language
st.write('You selected:', selected_language)


# Function to query the LangFlow API
def query_langflow(message):
    url = "https://astra.datastax.com/langflow/8a63160f-cba9-41aa-8b94-6f0636885a2a/flow/c194ac23-cf6b-4d8b-b9bf-51505cc18d96"
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer sk-lvKo9qL4F6U4dduiKpB7QJX2IBgUBDeiq4yFWeKmbZM"  # Ensure correct format
    }
    data = {"message": message}
    
    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()  # Raise an exception for HTTP errors (e.g., 401 Unauthorized)
        
        # Check for content type to verify if it's a valid JSON response.
        content_type = response.headers.get('content-type')
        if content_type and 'application/json' not in content_type:
            raise json.JSONDecodeError("Invalid content type received, expecting JSON", "", 0)

        return response.json()
    except requests.exceptions.RequestException as e:
        st.error(f"Request Error: {e}")  # Display error to user in Streamlit
        return {"response": "Error: Unable to get a response from the chatbot."}
    except json.JSONDecodeError as e:
        st.error(f"JSON Decoding Error: {e}")  # Display error to user in Streamlit
        return {"response": "Error: Invalid response format from the chatbot."}

# Streamlit app interface
user_input = st.text_input("You: ", "Hello, how can I help you?")
if st.button("Send"):
    response = query_langflow(user_input)
    st.text_area("Chatbot:", value=response.get('response', 'No response received.'), height=200)


# Title
st.header('Our Team CodeCrafters')

# List of team members
st.markdown("""
- Sajjid Ali - Team Leader
- Zulfiqar Ali Mir
- Stavin Fernandes
- Victoria Ude
- Nguyen Chi
- Muhammad Abubakar Alameen
""")



# import streamlit as st
# import requests

# st.title('LangFlow Chatbot with LLaMA-3')

# # Function to query the LangFlow API
# def query_langflow(message):
#     url = "https://astra.datastax.com/langflow/8a63160f-cba9-41aa-8b94-6f0636885a2a/flow/c194ac23-cf6b-4d8b-b9bf-51505cc18d96"
#     headers = {
#         "Content-Type": "application/json",
#         "Authorization": "sk-lvKo9qL4F6U4dduiKpB7QJX2IBgUBDeiq4yFWeKmbZM"
#     }
#     data = {
#         "message": message
#     }
#     response = requests.post(url, headers=headers, json=data)
#     if response.status_code == 200:
#         return response.json()
#     else:
#         return {"response": "Error: Unable to get a response from the chatbot."}

# # Streamlit app interface
# user_input = st.text_input("You: ", "Hello, how can I help you?")
# if st.button("Send"):
#     response = query_langflow(user_input)
#     st.text_area("Chatbot:", value=response.get('response', 'No response received.'), height=200)
