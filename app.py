import streamlit as st
import cnn as prd
import retina_classifier as rc
#import logistic as lg
import direct_data as dd
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import pandas as pd
import plotly.express as px
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array


# Set the page config for better layout
st.set_page_config(page_title="Glaucoma Detection", layout="wide", page_icon="🧿")
st.title("Glaucoma Diagnosis through Supervised Machine Learning on Retinal Fundus Images")

rad = st.sidebar.radio("Navigation", ["Predict", "Comparison"])

if rad == "Predict":
    st.subheader("Please input an image :sunglasses:")

    # Using columns to arrange file uploader and image side by side
    col1, col2 = st.columns(2)
    with col1:
        img_files = st.file_uploader("Upload an image", accept_multiple_files=True, type=["jpg", "jpeg"])

    for img_file in img_files:
        st.write(img_file.name)
        if img_file is not None:
            img = Image.open(img_file)
            img.save("img.jpg")
            img = np.array(img)
            img = cv.cvtColor(img, cv.COLOR_RGB2BGR)

            if rc.is_retinal(img):
                img=cv.imread("img.jpg")
                gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
                resized=cv.resize(gray,(290,290))
                x_var=np.array(resized)
                x_var=x_var.reshape(-1,290*290)/255
                plt.imshow(img)
                plt.title(prd.predict_and_plot("img.jpg"))
                st.pyplot(plt.gcf())
                
            else:
                st.error('The uploaded image is not a valid retinal fundus image. Please upload a valid image.')

if rad == "Comparison":
    st.subheader("Comparison of Glaucoma Detection Methods")
    data = dd.getdata()

    # Adding a plotly chart
    df = pd.DataFrame({
        "Method": data["Model name"],
        "Accuracy": data['Accuracy']
    })
    fig = px.bar(df, x="Method", y="Accuracy", title="Model comparison by Accuracy", color="Method")
    st.plotly_chart(fig)

    # Adding a plotly chart
    df = pd.DataFrame({
        "Method": data["Model name"],
        "Precision": data['Precision']
    })
    fig1 = px.bar(df, x="Method", y="Precision", title="Model comparison by Precision", color="Method")
    st.plotly_chart(fig1)

    # Adding a plotly chart
    df = pd.DataFrame({
        "Method": data["Model name"],
        "Recall": data['Recall']
    })
    fig2 = px.bar(df, x="Method", y="Recall", title="Model comparison by Recall", color="Method")
    st.plotly_chart(fig2)

    # Adding a plotly chart
    df = pd.DataFrame({
        "Method": data["Model name"],
        "F1 score": data['F1 score']
    })
    fig3 = px.bar(df, x="Method", y="F1 score", title="Model comparison by F1 score", color="Method")
    st.plotly_chart(fig3)

# Sidebar customization
st.sidebar.markdown("## About")
st.sidebar.markdown("This application uses machine learning to detect glaucoma from retinal images. Upload an image to get started.")

# Optional: Adding a footer
st.markdown("""
    <style>.footer {position: fixed;left: 0;bottom: 0;width: 100%;color: white;background-color: #282932;text-align: center;padding: 10px;}
    </style><div class="footer"><p>Created with ❤ using Streamlit</p></div>
    """, unsafe_allow_html=True)