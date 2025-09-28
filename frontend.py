#pip install streamlit requests
import streamlit as st
import requests

st.title("LLM Chat Frontend")

# Input box for user prompt
user_prompt = st.text_area("Enter your message:")

# Button to send prompt
if st.button("Send"):
    if user_prompt.strip() != "":
        try:
            # Replace 5000 with your backend port if different
            url = "http://127.0.0.1:5000/chat"
            response = requests.post(url, json={"prompt": user_prompt})
            
            if response.status_code == 200:
                data = response.json()
                if "response" in data:
                    st.success(data["response"])
                else:
                    st.error("Error from backend: " + str(data.get("error", "Unknown error")))
            else:
                st.error(f"Request failed with status {response.status_code}")
        except Exception as e:
            st.error(f"Exception: {e}")

