import easyocr
import cv2
from matplotlib import pyplot as plt
import numpy as np
from googletrans import Translator
import streamlit as st
from PIL import Image
uploaded_image=st.file_uploader("Upload image",type=["jpg","png"])
if(uploaded_image!=None):
    display_image=Image.open(uploaded_image)
    display_image=display_image.convert("RGB")
    st.image(display_image)
    if st.button("Translate"):
        st.text("This may take a minute or two")
        reader = easyocr.Reader(['de'])
        result = reader.readtext(np.array(display_image))
        img = np.array(display_image)
        font = cv2.FONT_HERSHEY_SIMPLEX
        for detection in result: 
           try:
                top_left = tuple(detection[0][0])
                bottom_right = tuple(detection[0][2])
                text = detection[1]
                #translator=Translator()
                #translation=translator.translate(text,dest="en")
                #img = cv2.rectangle(img,top_left,bottom_right,(0,255,0),3)
                img = cv2.putText(img,text,top_left, font, 0.5,(255,0,0),1,cv2.LINE_AA)
            except:
                pass
        st.image(img)
        st.text("Thank you for your patience")
