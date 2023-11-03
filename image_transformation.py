import streamlit as st
from PIL import Image, ImageOps, ImageFilter

# Function to convert image to grayscale using Pillow
def grayscale_conversion(image):
    grayscale_image = ImageOps.grayscale(image)
    return grayscale_image

# Function to rotate image using Pillow
def rotate_image(image, angle):
    rotated_image = image.rotate(angle)
    return rotated_image

# Function to flip image using Pillow
def flip_image(image, direction):
    if direction == 'Horizontal':
        flipped_image = ImageOps.mirror(image)
    elif direction == 'Vertical':
        flipped_image = ImageOps.flip(image)
    return flipped_image

# Function to apply Gaussian blur using Pillow
def gaussian_blur(image, radius):
    blurred_image = image.filter(ImageFilter.GaussianBlur(radius=radius))
    return blurred_image

# Streamlit UI
st.title("Image Transformation App")

# Upload image
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    # Read image
    image = Image.open(uploaded_file)
    
    # Display original image
    st.subheader("Original Image")
    st.image(image, caption='Original Image', use_column_width=True)
    
    # Transformation options
    transformation = st.selectbox("Select Transformation", ["Grayscale", "Rotate", "Flip", "Gaussian Blur"])
    
    if transformation == "Grayscale":
        # Apply grayscale conversion
        transformed_image = grayscale_conversion(image)
        st.subheader("Grayscale Image")
        st.image(transformed_image, caption='Grayscale Image', use_column_width=True)
    
    elif transformation == "Rotate":
        angle = st.slider("Enter Angle (degrees)", -180, 180, 0)
        # Apply rotation
        transformed_image = rotate_image(image, angle)
        st.subheader("Rotated Image")
        st.image(transformed_image, caption='Rotated Image', use_column_width=True)
    
    elif transformation == "Flip":
        direction = st.radio("Select Direction", ["Horizontal", "Vertical"])
        # Apply flipping
        transformed_image = flip_image(image, direction)
        st.subheader("Flipped Image")
        st.image(transformed_image, caption='Flipped Image', use_column_width=True)
    
    elif transformation == "Gaussian Blur":
        radius = st.slider("Enter Blur Radius", 0, 10, 2)
        # Apply Gaussian blur
        transformed_image = gaussian_blur(image, radius)
        st.subheader("Blurred Image")
        st.image(transformed_image, caption='Blurred Image', use_column_width=True)
