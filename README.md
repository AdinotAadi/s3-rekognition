# AWS S3 and Rekognition Image Object Detection with Streamlit Frontend

This Python application utilizes AWS S3 for storing images and AWS Rekognition for object detection in those images. It provides a Streamlit frontend for easy interaction.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your_username/your_repository.git
    ```

2. Navigate to the project directory:

    ```bash
    cd your_repository
    ```

3. Install the required dependencies using pip:

    ```bash
    pip install -r requirements.txt
    ```

## Configuration

Before running the application, ensure you have configured your AWS credentials properly. You can do this by either setting environment variables or using AWS CLI.

```bash
export AWS_ACCESS_KEY_ID='your_access_key_id'
export AWS_SECRET_ACCESS_KEY='your_secret_access_key'
export AWS_DEFAULT_REGION='your_aws_region'
```

Alternatively, you can configure AWS CLI by running:
```bash
aws configure
```

## Usage

To run the application, execute the following command:

```bash
streamlit run app.py
```

This will start the Streamlit application, which you can access through your web browser.

## Features

- Upload images to AWS S3 bucket.
- Detect objects in uploaded images using AWS Rekognition.
- Display detected objects along with confidence scores.

## File Structure
```
./
├── app.py                  # Streamlit application script
├── requirements.txt        # List of Python dependencies
└── README.md               # Project README file
```

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue if you encounter any problems or have suggestions for improvements.