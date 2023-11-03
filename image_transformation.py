import streamlit as st
import cv2
import numpy as np

def contrast_stretching(image):
    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Apply contrast stretching
    min_val = np.min(gray)
    max_val = np.max(gray)
    stretched = ((gray - min_val) / (max_val - min_val) * 255).astype(np.uint8)
    
    return stretched

# Streamlit UI
st.title("Image Enhancement using Contrast Stretching")

# Upload image
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    # Read image
    image = cv2.imdecode(np.fromstring(uploaded_file.read(), np.uint8), 1)
    
    # Display original image
    st.subheader("Original Image")
    st.image(image, channels="BGR")
    
    # Apply contrast stretching
    enhanced_image = contrast_stretching(image)
    
    # Display enhanced image
    st.subheader("Enhanced Image")
    st.image(enhanced_image, channels="BGR")
