import streamlit as st 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
import tempfile
from tempfile import NamedTemporaryFile
import os, shutil
import cv2
from PIL import Image
from deepface import DeepFace

st.title("Performance analysis of 'Face Recognition Models' in cloud platform")

choice = st.selectbox("Select Option",[
    "Analysis with Facenet",
    "Analysis with VGG-Face"
])

if not os.path.isdir('tempDir'):
    os.mkdir('tempDir')
    
@st.cache   
def recognisefacenet(img1, img2):
    backends = ['opencv', 'ssd', 'dlib', 'mtcnn', 'retinaface', 'mediapipe']
    models = ["VGG-Face", "Facenet", "Facenet512", "OpenFace", "DeepFace"]
    result = DeepFace.verify(img1_path = img1, img2_path = img2,detector_backend = backends[3],model_name =models[2])
    return result

@st.cache
def recognise(img1, img2):
    backends = ['opencv', 'ssd', 'dlib', 'mtcnn', 'retinaface', 'mediapipe']
    models = ["VGG-Face", "Facenet", "Facenet512"]
    result = DeepFace.verify(img1_path = img1, img2_path = img2,detector_backend = backends[3],model_name =models[0])
    return result
# def uploadFile():
#     st.header("Upload Image ")
#     column1, column2 = st.columns(2)
#     with column1:
#         image1 = st.file_uploader('Choose 1st Image(Normal)', type = ['jpg','jpeg','png'])
#     with column2:
#         image2 = st.file_uploader('Choose 2nd Image(with Specs/ Mask/ Beard if Male)', type = ['jpg','jpeg','png'])
            
#     if(image1 is not None) & (image2 is not None):
#         # col1 , col2 = st.columns(2)
#         # image_1 = Image.open(image1)
#         # image_2 = Image.open(image2)
#         # with col1: 
#         #     st.image(image_1)
#         with open(os.path.join("tempDir",image1.name), "wb") as f:
#             f.write(image1.getbuffer())
#             st.success('Saved imag1')
#         # with col2:
#         #     st.image(image_2)
#         with open(os.path.join("tempDir",image2.name), "wb") as g:
#             g.write(image2.getbuffer())
#             st.success('Saved imag2')
#         return (image1,image2)
#     else:
#         st.error("Please select Valid file")
        
        
def main():
    if choice == "Analysis with Facenet":
        st.header("Analysis with Facenet")    
        column1, column2 = st.columns(2)
        
        with column1:
            image1 = st.file_uploader('Choose 1st Image(Normal)', type = ['jpg','jpeg','png'])
        with column2:
            image2 = st.file_uploader('Choose 2nd Image(with Specs/ Mask/ Beard if Male)', type = ['jpg','jpeg','png'])
            
        if(image1 is not None) & (image2 is not None):
            col1 , col2 = st.columns(2)
            image_1 = Image.open(image1)
            image_2 = Image.open(image2)
            with col1: 
                st.image(image_1)
            with open(os.path.join("tempDir",image1.name), "wb") as f:
                f.write(image1.getbuffer())
            st.success('Save imag1')
            with col2:
                st.image(image_2)
            with open(os.path.join("tempDir",image2.name), "wb") as g:
                g.write(image2.getbuffer())
            st.success('Save imag2')
            p1 = 'tempDir/{}'.format(image1.name)
            p2 = 'tempDir/{}'.format(image2.name)
            print(p1,p2)
            st.write(recognisefacenet(p1,p2))
            with NamedTemporaryFile(dir='.', suffix='.jpg') as f:
                f.write(image1.getbuffer())
            with NamedTemporaryFile(dir='.', suffix='.jpg') as g:
                g.write(image2.getbuffer())
                
            
    elif choice == "Analysis with VGG-Face":
        st.header("Analysis with VGG-Face")    
        column1, column2 = st.columns(2)
        
        with column1:
            image1 = st.file_uploader('Choose 1st Image(Normal)', type = ['jpg','jpeg','png'])
        with column2:
            image2 = st.file_uploader('Choose 2nd Image(with Specs/ Mask/ Beard if Male)', type = ['jpg','jpeg','png'])
            
        if(image1 is not None) & (image2 is not None):
            col1 , col2 = st.columns(2)
            image_1 = Image.open(image1)
            image_2 = Image.open(image2)
            with col1: 
                st.image(image_1)
            with open(os.path.join("tempDir",image1.name), "wb") as f:
                f.write(image1.getbuffer())
            st.success('Save imag1')
            with col2:
                st.image(image_2)
            with open(os.path.join("tempDir",image2.name), "wb") as g:
                g.write(image2.getbuffer())
            st.success('Save imag2')
            p1 = 'tempDir/{}'.format(image1.name)
            p2 = 'tempDir/{}'.format(image2.name)
            print(p1,p2)
            st.write(recognise(p1,p2))

    else:
        st.write("Plaese Select Proper Model") 
    if st.button('Free memory'):
        fpath = Path('tempDir')
        if len(os.listdir(fpath))>0:
            shutil.rmtree(fpath)
            st.success('Memory Freed')
        else:
            st.error('Nothing to free')
if __name__ == "__main__":
    main()
     