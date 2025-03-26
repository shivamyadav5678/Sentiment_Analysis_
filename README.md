# Sentiment Analysis Application

## Overview
This project provides a web-based sentiment analysis tool that can process both text and image inputs to detect emotions. It utilizes Streamlit for the frontend, DeepFace for facial emotion detection in images, and TextBlob and text2emotion for analyzing sentiments in text.

## Features
- **Text Analysis**: It analyzes user input to determine the sentiment of the text (Positive/Negative/Neutral) using TextBlob and categorizes the emotion (Happy, Sad, Angry, Fear, Surprise) using text2emotion.
- **Image Analysis**: Users can upload an image, and the app will detect faces and analyze their emotions (e.g., Happy, Angry, Sad, etc.) using DeepFace.

## Tools and Libraries

- **Streamlit**: An open-source app framework used to create the web interface for the project.
  - [Streamlit documentation](https://docs.streamlit.io/)

- **DeepFace**: A Python library for deep learning-based face recognition and emotion analysis.
  - [DeepFace documentation](https://github.com/serengil/deepface)

- **TextBlob**: A library for processing textual data. It provides a simple API for common natural language processing (NLP) tasks, including sentiment analysis.
  - [TextBlob documentation](https://textblob.readthedocs.io/en/dev/)

- **text2emotion**: A Python package to extract emotions from text (Happy, Sad, Angry, Fear, Surprise).
  - [text2emotion documentation](https://github.com/atulapraja/text2emotion)

- **Plotly**: A graphing library used to create interactive plots and charts. In this project, it is used to display pie charts representing emotion distribution.
  - [Plotly documentation](https://plotly.com/)

- **OpenCV**: A computer vision library used to handle image processing tasks such as reading and manipulating images.
  - [OpenCV documentation](https://opencv.org/)

- **Pillow (PIL)**: A Python Imaging Library for opening, manipulating, and saving image files.
  - [Pillow documentation](https://pillow.readthedocs.io/en/stable/)

- **streamlit-option-menu**: A Streamlit component used for adding side navigation menus to the app.
  - [streamlit-option-menu documentation](https://github.com/vikraft/streamlit-option-menu)

## Setup Instructions

1. **Install the required dependencies**:
   - Ensure that you have Python installed.
   - Run the following command to install the necessary libraries:
     ```bash
     pip install -r requirements.txt
     ```

2. **Run the Streamlit app**:
   - After installing the dependencies, run the following command to launch the app:
     ```bash
     streamlit run app.py
     ```

3. **Access the application**:
   - The app will open in your default web browser at `http://localhost:8501`.

## Usage

### Text Sentiment Analysis
1. Input text into the provided text box.
2. Choose the type of analysis:
   - **Positive/Negative/Neutral** using TextBlob: This analysis gives the sentiment polarity (positive, negative, neutral) and subjectivity of the text.
   - **Happy/Sad/Angry/Fear/Surprise** using text2emotion: This analysis provides the intensity of each emotion in the text.

### Image Emotion Analysis
1. Upload an image that contains faces.
2. The app will process the image, detect faces, and analyze emotions such as Happy, Sad, Angry, etc.
3. The results will be displayed with visual representations, such as images of the detected faces and pie charts for emotion distribution.

## Conclusion
This sentiment analysis application provides easy-to-use tools for analyzing both text and image data, allowing you to explore different sentiment analysis techniques.
