from dotenv import load_dotenv
import os
import google.generativeai as genai 
import streamlit as st  
from PIL import Image

# calling in-built library function
load_dotenv()   

api_key = os.getenv("google_api_key")
model = genai.configure(api_key=api_key)

# <<<<<<<<<<<< BACKEND >>>>>>>>>>>>

#  passing prompt and image (arguments) to LLM model
def get_gemini_response(prompt, uploaded_image):
    # gemini-pro 
    model = genai.GenerativeModel("gemini-1.5-flash") 
    # if prompt is given by user
    if prompt != "":  
        # upload both prompt and image  
        response = model.generate_content([prompt, uploaded_image])
    # if prompt is not given by user
    else:
        # upload only image  
        response = model.generate_content(uploaded_image)
    return response.text


# <<<<<<<<<<<<<< INTERFACE/FRONTEND >>>>>>>>>>>>>>>>
# title tag 
st.set_page_config("gemini chatbot")   
# heading tag 
st.header("Chatbot Application using Gemini")   
# taking text input (prompt) from user
input = st.text_input("Input here : ", key="input")  
# taking image as a input from user
uploaded_file = st.file_uploader("choose an image ...", type=["jpeg", "jpg", "png"])   

image = ""
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    # image rendering on screen 
    st.image(image, "uploaded image", use_column_width=True)  

# creating button
submit = st.button("SUBMIT") 


# <<<<<<<<<<<< WORKING OF SUBMIT BUTTON >>>>>>>>>>>>>>>

# if user clicks submit button than call the function and write the response
if submit:
    response = get_gemini_response(prompt=input, uploaded_image=image)  
    st.subheader("Your response is :")
    st.write(response)





