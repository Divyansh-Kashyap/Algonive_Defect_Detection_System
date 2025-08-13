
import streamlit as st
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
import cv2
import tempfile

st.title("Manufacturing Defect Detection")
st.write("Upload a product image to check for defects.")

model = load_model(r"C:\Users\Divyansh Kashyap\Downloads\AI_Defect_Detection_Project\defect_detection_project\app\defect_detection_model.h5")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    img = cv2.imdecode(file_bytes, 1)
    img_resized = cv2.resize(img, (300, 300))
    img_array = image.img_to_array(img_resized)
    img_array = np.expand_dims(img_array, axis=0) / 255.0

    prediction = model.predict(img_array)
    label = "Defective" if prediction[0][0] > 0.5 else "Non-Defective"

    st.image(img, caption=f"Prediction: {label}", use_column_width=True)
