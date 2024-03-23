import streamlit as st
import boto3
from PIL import Image
import boto3
from dotenv import load_dotenv
import os
import io

load_dotenv() 

ACCESS_KEY = os.getenv("AWS_ACCESS_KEY_ID")
SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
REGION = os.getenv("AWS_REGION")
AWS_BUCKET_NAME = os.getenv("AWS_BUCKET_NAME")

s3 = boto3.client(
    service_name = 's3',
    region_name = REGION,
    aws_access_key_id = ACCESS_KEY,
    aws_secret_access_key = SECRET_ACCESS_KEY
)

rekognize = boto3.client('rekognition',
                         region_name = REGION,
                         aws_access_key_id = ACCESS_KEY,
                         aws_secret_access_key = SECRET_ACCESS_KEY
)

st.title('Image Classification App')

uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image', use_column_width=True)

    # Convert uploaded file to bytes
    file_bytes = uploaded_file.getvalue()


    # Upload the bytes to S3
    object_key = uploaded_file.name
    s3.put_object(Bucket=AWS_BUCKET_NAME, Key=object_key, Body=file_bytes)
    st.success("Image uploaded to S3")

    response = rekognize.detect_labels(
        Image={'S3Object': {'Bucket': AWS_BUCKET_NAME, 'Name': uploaded_file.name}},
        MaxLabels=10
    )

    classification_results = []
    for label in response['Labels']:
        classification_results.append({'Label': label['Name'], 'Confidence': label['Confidence']})

    # Display classification results in a table
    st.subheader('Classification Results:')
    st.table(classification_results)