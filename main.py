Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import streamlit as st
... import openai
... import os
... 
... # Set your OpenAI API key
... openai.api_key = "api"  # 
... 
... # Streamlit UI
... st.title("AI-Powered Fashion Design Generator")
... st.write("Enter a description of your fashion design, and the AI will generate an image.")
... 
... # User input
... prompt = st.text_input("Describe your fashion design:", "Minimalist streetwear with geometric patterns")
... 
... if st.button("Generate Design"):
...     if prompt:
...         with st.spinner("Generating design..."):
...             response = openai.Image.create(
...                 prompt=prompt,
...                 n=1,
...                 size="1024x1024"
...             )
...             image_url = response["data"][0]["url"]
...             st.image(image_url, caption="Generated Fashion Design")
...     else:
...         st.warning("Please enter a description!")
