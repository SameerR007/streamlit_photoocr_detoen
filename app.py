import easyocr
import streamlit as st
import numpy as np
from PIL import Image
from googletrans import Translator
import cv2

def ocr_translation(image, language):
    reader = easyocr.Reader([language])
    result = reader.readtext(image)
    font = cv2.FONT_HERSHEY_SIMPLEX
    for detection in result: 
        try:
            top_left = tuple(detection[0][0])
            bottom_right = tuple(detection[0][2])
            text = detection[1]
            translator = Translator()
            translation = translator.translate(text, dest="en")
            image = cv2.putText(image, translation.text, top_left, font, 0.5, (255, 0, 0), 1, cv2.LINE_AA)
        except:
            pass    
    return image


st.title("OCR Translation App")

# Upload image
image_file = st.file_uploader("Upload an image", type=['jpg', 'jpeg', 'png'])
if image_file is not None:
    image = Image.open(image_file)
    image=image.convert("RGB")
    image = np.array(image)
    image = ocr_translation(image, 'de')
    st.image(image, caption='Translated image')
