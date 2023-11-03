import streamlit as st
import cv2
import numpy as np

# Function to convert image to grayscale using OpenCV
def grayscale_conversion(image):
    grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return grayscale_image

# Function to rotate image using OpenCV
def rotate_image(image, angle):
    rows, cols, _ = image.shape
    M = cv2.getRotationMatrix2D((cols/2, rows/2), angle, 1)
    rotated_image = cv2.warpAffine(image, M, (cols, rows))
    return rotated_image

# Function to flip image using OpenCV
def flip_image(image, direction):
    if direction == 'Horizontal':
        flipped_image = cv2.flip(image, 1)
    elif direction == 'Vertical':
        flipped_image = cv2.flip(image, 0)
    return flipped_image

# Function to apply Gaussian blur using OpenCV
def gaussian_blur(image, radius):
    blurred_image = cv2.GaussianBlur(image, (radius*2+1, radius*2+1), 0)
    return blurred_image

# Streamlit UI
st.title("Image Transformation App")

# Upload image
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    # Read image
    image = cv2.imdecode(np.fromstring(uploaded_file.read(), np.uint8), 1)
    
    # Display original image
    st.subheader("Original Image")
    st.image(image, channels="BGR", caption='Original Image', use_column_width=True)
    
    # Transformation options
    transformation = st.selectbox("Select Transformation", ["Grayscale", "Rotate", "Flip", "Gaussian Blur"])
    
    if transformation == "Grayscale":
        # Apply grayscale conversion
        transformed_image = grayscale_conversion(image)
        st.subheader("Grayscale Image")
        st.image(transformed_image, channels="BGR", caption='Grayscale Image', use_column_width=True)
    
    elif transformation == "Rotate":
        angle = st.slider("Enter Angle (degrees)", -180, 180, 0)
        # Apply rotation
        transformed_image = rotate_image(image, angle)
        st.subheader("Rotated Image")
        st.image(transformed_image, channels="BGR", caption='Rotated Image', use_column_width=True)
    
    elif transformation == "Flip":
        direction = st.radio("Select Direction", ["Horizontal", "Vertical"])
        # Apply flipping
        transformed_image = flip_image(image, direction)
        st.subheader("Flipped Image")
        st.image(transformed_image, channels="BGR", caption='Flipped Image', use_column_width=True)
    
    elif transformation == "Gaussian Blur":
        radius = st.slider("Enter Blur Radius", 0, 10, 2)
        # Apply Gaussian blur
        transformed_image = gaussian_blur(image, radius)
        st.subheader("Blurred Image")
        st.image(transformed_image, channels="BGR", caption='Blurred Image', use_column_width=True)
