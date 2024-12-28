import streamlit as st
import openai

openai.api_key = "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"

def generate_chat_response(prompt):
    try:
        response = openai.completions.create(model="gpt-4", prompt=prompt)
        return response['choices'][0]['text'].strip()
    except Exception as e:
        return f"Error: {e}"

def generate_dalle_image(prompt):
    try:
        response = openai.Image.create(
            prompt=prompt,
            n=1,
            size="1024x1024"
        )
        image_url = response['data'][0]['url']
        if image_url:
            st.image(image_url, caption="Generated by DALL-E", use_container_width=True)
        else:
            st.error("No image URL returned.")
    except Exception as e:
        return f"Error: {e}"

st.title("AI Chatbot & DALL-E Image Generator")
st.sidebar.header("Choose an option")
option = st.sidebar.selectbox("Select functionality:", ["Chatbot", "Image Generator"])

if option == "Chatbot":
    st.header("Chat with AI")
    user_input = st.text_input("Enter your message:", "Hello, AI!")
    if st.button("Send"):
        response = generate_chat_response(user_input)
        st.text_area("AI Response:", response, height=200)

elif option == "Image Generator":
    st.header("Generate an Image with AI")
    image_prompt = st.text_input("Describe the image you want to create:")
    if st.button("Generate Image"):
        image_url = generate_dalle_image(image_prompt)
        if "http" in image_url:
            st.image(image_url, caption="Generated by DALL-E", use_container_width=True)
        else:
            st.error(image_url)
