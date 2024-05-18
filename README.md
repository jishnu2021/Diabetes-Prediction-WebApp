# Diabetes Prediction Web App

This repository contains a web application for predicting diabetes using a machine learning model. The model is built with a Support Vector Machine (SVM) and the web application is developed using Streamlit.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Model Training](#model-training)
- [Contributing](#contributing)
- [License](#license)

## Introduction

Diabetes is a chronic condition that affects millions of people worldwide. Early detection is crucial for managing and preventing the adverse effects of diabetes. This project provides a simple, user-friendly web application that predicts the likelihood of diabetes based on user-provided health metrics.

## Features

- Predicts the likelihood of diabetes using user input
- Uses a Support Vector Machine (SVM) for classification
- Standardizes input data using StandardScaler for better model performance
- User-friendly interface built with Streamlit

## Installation

To run this project locally, follow these steps:

1. Clone the repository:

   ```bash
   gh repo clone jishnu2021/Diabetes-Prediction-WebApp


2. Install the required dependencies:
   pip install -r requirements.txt

3.Ensure you have the saved model file (trained_model.sav) in the project directory.


## Usage
To start the Streamlit web application, run the following command:
streamlit run app.py


## Model Training
The machine learning model is trained using the Pima Indians Diabetes Dataset. The following steps outline the training process:

Preprocessing: Standardize the input features using StandardScaler.
Model Training: Train a Support Vector Machine (SVM) on the standardized data.
Saving the Model: Save the trained model using pickle for later use in the web application.


## Contributing
Contributions are welcome! Please open an issue or submit a pull request if you have any suggestions or improvements.

## License
This project is licensed under the MIT License. See the LICENSE file for details.



