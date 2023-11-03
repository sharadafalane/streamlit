import streamlit as st
from PIL import Image, ImageEnhance

def contrast_stretching(image):
    enhancer = ImageEnhance.Contrast(image)
    enhanced_image = enhancer.enhance(2.0)  # Adjust the enhancement factor as needed
    return enhanced_image

# Streamlit UI
st.title("Image Enhancement using Contrast Stretching")

# Upload image
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    # Read image
    image = Image.open(uploaded_file)
    
    # Display original image
    st.subheader("Original Image")
    st.image(image, caption='Original Image', use_column_width=True)
    
    # Apply contrast stretching
    enhanced_image = contrast_stretching(image)
    
    # Display enhanced image
    st.subheader("Enhanced Image")
    st.image(enhanced_image, caption='Enhanced Image', use_column_width=True)
