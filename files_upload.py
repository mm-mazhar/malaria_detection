import streamlit as st
import numpy as np
#import pandas as pd
from io import BytesIO
from tensorflow.keras.preprocessing import image

class FilesUpload(object):

    def __init__(self):
        self.fileTypes = ["png", "jpg"]

    def run(self):
        image_shape = (130, 130, 3)
        st.set_option('deprecation.showfileUploaderEncoding', False)
        img_file = st.file_uploader("Upload file", type=self.fileTypes)
        show_img_file = st.empty()
        if not img_file:
            show_img_file.info("Please upload a file of type: " + ", ".join(["png", "jpg"]))
            return
        content = img_file.getvalue()
        if isinstance(img_file, BytesIO):
            st.image(img_file, width = 130) #use_column_width=True
            img_file = image.load_img(img_file, target_size=image_shape)
            img_file = image.img_to_array(img_file)
            img_file = np.expand_dims(img_file, axis=0)
            img_file = img_file/255 #Normalizing the Image
            #st.text(img_file)
            st.text(img_file.shape)
            st.text("image = {}, Width = {}, Height = {}, color = {}".format(img_file.shape[0],
                    img_file.shape[1], img_file.shape[2], img_file.shape[3]))
            return img_file
        else:
            st.write("Incorrect file or file extension")

