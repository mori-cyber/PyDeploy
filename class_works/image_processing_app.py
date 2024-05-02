import cv2
import numpy as np
from PIL import Image
import streamlit as st

st.title("image blur app")
with st.sidebar:
     #process
    blur_amount = st.slider("چقدر می خوای تصویر مات بشه",
                            min_value=1, 
                            max_value=199,
                            value=21,
                            step=2)

uploaded_file =st.file_uploader("choose an image ...", type=["jpg","png","jpeg"])

if uploaded_file is not None:
    st.success("file loaded success")
    image = Image.open(uploaded_file)
    st.image(image, "input")
    image = np.array(image)
    #preperocessing
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

   
    
    result_image = cv2.blur(image, (blur_amount,blur_amount))# باید اغداد فرد باشه

    #postprocessing
    result_image = cv2.cvtColor(result_image, cv2.COLOR_BGR2RGB)
    result_image =Image.fromarray(result_image)
    st.image(result_image, "out put")

else:
    st.info("هیچ فایلی بارگذاری نشده است")