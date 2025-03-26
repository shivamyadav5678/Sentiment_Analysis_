import streamlit as st
import numpy as np
import cv2
import modals
from PIL import Image
import text2emotion as te
import json
import plotly.graph_objects as go
import streamlit.components.v1 as components



# Define a dictionary to map emotions to emojis (ensure you have the emojis for each emotion)
getEmoji = {
    "angry": "😡",
    "disgust": "🤢",
    "fear": "😨",
    "happy": "😊",
    "sad": "😞",
    "surprise": "😲",
    "neutral": "😐"
}

def showEmotionData(emotion, topEmotion, image, idx):
    try:
        # Safely check if 'box' key exists before accessing it
        if 'box' in emotion:
            x, y, w, h = tuple(emotion["box"])
            cropImage = image[y:y+h, x:x+w]
        else:
            # If 'box' is missing, return a message or handle it accordingly
            st.write(f"Face bounding box not found for person {idx}.")
            return

        # Get the emotion labels and values
        cols = st.columns(7)
        keys = list(emotion["emotions"].keys())
        values = list(emotion["emotions"].values())
        emotions = sorted(emotion["emotions"].items(), key=lambda kv: (kv[1], kv[0]))

        # Title for the person detected
        st.components.v1.html(f"""<h3 style="color: #ef4444; font-family: Source Sans Pro, sans-serif; font-size: 20px; margin-bottom: 0px; margin-top: 0px;">Person detected {idx}</h3>""", height=30)
        
        # Layout for displaying emotion metrics
        col1, col2, col3 = st.columns([3, 1, 2])
        
        with col1:
            st.image(cropImage, width=200)  # Display the cropped face image
        
        with col2:
            # Display the first 4 emotions in the list
            for i in range(4):
                st.metric(f"{keys[i].capitalize()} {getEmoji.get(keys[i], '')}", round(values[i], 2), None)
        
        with col3:
            # Display the next 3 emotions and the top emotion
            for i in range(4, 7):
                st.metric(f"{keys[i].capitalize()} {getEmoji.get(keys[i], '')}", round(values[i], 2), None)
            st.metric(f"Top Emotion {getEmoji.get(topEmotion[0], '')}", None)

        # Separator between different face detections
        st.components.v1.html("<hr>", height=5)

    except Exception as e:
        st.write(f"Error displaying emotion data: {e}")


def printResultHead():
    st.write("")
    st.write("")
    st.components.v1.html("""<h3 style="color: #0ea5e9; font-family: Source Sans Pro, sans-serif; font-size: 26px; margin-bottom: 10px; margin-top: 60px;">Result</h3><p style="color: #57534e; font-family: Source Sans Pro, sans-serif; font-size: 16px;">Find below the sentiments we found in your given image. What do you think about our results?</p>""", height=150)

def printImageInfoHead():
    st.write("")
    st.write("")
    st.components.v1.html("""<h3 style="color: #ef4444; font-family: Source Sans Pro, sans-serif; font-size: 22px; margin-bottom: 0px; margin-top: 40px;">Image information</h3><p style="color: #57534e; font-family: Source Sans Pro, sans-serif; font-size: 14px;">Expand below to see the information associated with the uploaded image</p>""", height=100)

'''def uploadFile():
    uploaded_file = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])
    if uploaded_file is not None:
        content = Image.open(uploaded_file)
        content = np.array(content)  # Convert PIL to numpy array
        shape = np.shape(content)
        if len(shape) < 3:
            st.error('Your image has a bit-depth less than 24. Please upload an image with a bit-depth of 24.')
            return
        
        emotions, topEmotion, image = modals.imageEmotion(content)
    
        if uploaded_file is not None:
            file_details = {"filename": uploaded_file.name, "filetype": uploaded_file.type, "filesize": uploaded_file.size}
            printImageInfoHead()
            with st.expander("See JSON Object"):
                st.json(json.dumps(file_details))
                st.subheader("Image")
                st.image(uploaded_file, caption=uploaded_file.name, width=250)

        if emotions is not None and len(emotions) == 0:
            st.text("No faces found!")
        if emotions is not None:
            printResultHead()
            with st.expander("Expand to see individual result"):
                for i in range(len(emotions)):
                    showEmotionData(emotions[i], topEmotion, content, i+1)
            st.write("")
            col1, col2 = st.columns([4, 2])
            with col1:
                st.image(image, width=300)
            with col2:
                st.metric("Top Emotion", topEmotion[0].capitalize() + " " + getEmoji[topEmotion[0]], None)
                st.metric("Emotion Percentage", str(round(topEmotion[1] * 100, 2)), None)'''
import streamlit as st
import numpy as np
from PIL import Image
import json

def uploadFile():
    # Upload the file
    uploaded_file = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])
    if uploaded_file is not None:
        # Load the image and convert it to a numpy array
        content = Image.open(uploaded_file)
        content = np.array(content)
        shape = np.shape(content)

        # Check image bit-depth
        if len(shape) < 3:
            st.error('Your image has a bit-depth less than 24. Please upload an image with a bit-depth of 24.')
            return

        # Call the modal function to get emotions
        emotions, topEmotion, image = modals.imageEmotion(content)

        # Display file details
        if uploaded_file is not None:
            file_details = {
                "filename": uploaded_file.name,
                "filetype": uploaded_file.type,
                "filesize": uploaded_file.size
            }
            printImageInfoHead()
            with st.expander("See JSON Object"):
                st.json(file_details)
                st.subheader("Image")
                st.image(uploaded_file, caption=uploaded_file.name, width=250)

        # Handle no faces found
        if emotions is not None and len(emotions) == 0:
            st.text("No faces found!")
            return

        # Display emotions
        if emotions is not None:
            printResultHead()
            with st.expander("Expand to see individual result"):
                for i, emotion in enumerate(emotions, start=1):
                    showEmotionData(emotion, topEmotion, content, i)
            st.write("")

            # Display the processed image and metrics
            col1, col2 = st.columns([4, 2])
            with col1:
                st.image(image, width=300)
            with col2:
                # Safely extract topEmotion
                if isinstance(topEmotion, tuple) and len(topEmotion) > 1:
                    emotion = topEmotion[0]
                    percentage = round(topEmotion[1] * 100, 2)
                else:
                    emotion = "Unknown"
                    percentage = 0.0

                # Emoji dictionary
                getEmoji = {
                    "happy": "😊",
                    "sad": "😢",
                    "angry": "😡",
                    "surprised": "😲",
                    "neutral": "😐"
                }

                # Display metrics
                st.metric("Top Emotion", emotion.capitalize() + " " + getEmoji.get(emotion, ""), None)
                st.metric("Emotion Percentage", f"{percentage}%", None)


def renderPage():
    st.title("Sentiment Analysis 😊😐😕😡")
    st.components.v1.html("""<hr style="height:3px;border:none;color:#333;background-color:#333; margin-bottom: 10px" /> """)
    st.subheader("Image Analysis")
    st.text("Input an image and let's find sentiments in there.")
    option = st.selectbox('How would you like to provide an image?', ('Upload One',))
    if option == "Upload One":
        uploadFile()
