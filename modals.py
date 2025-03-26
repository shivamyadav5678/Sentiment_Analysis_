from deepface import DeepFace
import streamlit as st

def imageEmotion(content):
    try:
        # Perform emotion analysis with face detection (face detection happens automatically)
        result = DeepFace.analyze(content, actions=['emotion'], enforce_detection=False)

        # Check if the result contains any data
        if not result or not isinstance(result, list) or len(result) == 0:
            st.write("No faces detected.")
            return None, None, content

        # Ensure that the first result contains emotions
        if 'emotion' not in result[0]:
            st.write("No emotions detected.")
            st.write(f"Result: {result}")
            return None, None, content

        emotions = result[0]["emotion"]
        topEmotion = max(emotions.items(), key=lambda kv: kv[1])

        # Handle multiple faces (if more than one face is detected)
        if len(result) > 1:
            # Collect top emotions for all detected faces
            topEmotions = [(max(face["emotion"].items(), key=lambda kv: kv[1])) for face in result]
            return result, topEmotions, content

        return result, topEmotion, content
    except Exception as e:
        st.write(f"Error during emotion analysis: {e}")
        return None, None, content
