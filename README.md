# Myfiles

Flight 06 file is a Power BI file and it is built for user to understand the price, layover of flights moving from one location to another in the country of USA.
It has Gauge, Slicer, Table, Flow Map, Card as a Visualization tool. I have made this dashboard keeping in mind the users of USA Airways. I have made this dashboard
by connecting Amazon Athena as the file size of data was greater than 4 GB after cleaning the data and it was part of the bigger big data project. Direct Query 
option was chosen by me so that that Power bi works efficiently and at optimum speed. This connection also required one ODBC connection which again 
requires the AWS session id, password and Session Token. One S3 Bucket location is required where the Athena Query results are stored. 




Another project is about Passbook Management System. It is a software application which is developed using Python programming language. 
Python is a versatile and widely used programming language that is suitable for developing complex web applications and systems. 
I have used different modules like mysql.connector and execute method of cursor class. I have handled exceptions too in this project so that 
if user input wrong data then the program should not end abruptly. Passbook Management System keeps the record of every entry and also keeps 
user data like created account ,checks balance , deposited amount and the withdrawal amount.



KNN is a classifier used as Machine Learning Algorithm. It is particularly useful when the labelled output is in a Categorical form. Classification
comes under the Supervised Learning of Machine Learning. Full form is K- Nearest Neigbour. KNN classifier operates by finding the k nearest neighbors to a given data point, and it takes the majority vote to classify the data point.
The value of k is crucial, and one needs to choose it wisely to prevent overfitting or underfitting the model.
One can use cross-validation to select the optimal value of k for the k-NN algorithm, which helps improve its performance and prevent overfitting or underfitting. Cross-validation is also used to identify the outliers before applying the KNN algorithm.
The above article provides implementations of KNN in Python and R, and it compares the result with scikit-learn and the “Class” library in R.


# MyFiles - My Data Science Portfolio

Welcome to my personal repository for data science projects! This repository showcases various analyses, machine learning models, and data handling techniques I've worked on.

## Table of Contents
- [Project Overview](#project-overview)
- [Projects](#projects)
    - [Lung Cancer Prediction Project](#lung-cancer-prediction-project)
    - [ANOVA and Chi-square test](#anova-and-chi-square-test)
    - [Flight Data Analysis](#flight-data-analysis)
    - [K-Nearest Neighbors (KNN) Implementation](#k-nearest-neighbors-knn-implementation)
    - [Support Vector Machine (SVM) Implementation](#support-vector-machine-svm-implementation)
    - [Final PMS Project](#final-pms-project)
- [How to Navigate This Repository](#how-to-navigate-this-repository)
- [Connect with Me](#connect-with-me)

## Project Overview
This repository serves as a collection of my data analysis and machine learning projects. Each project demonstrates my skills in data cleaning, exploratory data analysis, model building, and deriving actionable insights.

## Projects

### Lung Cancer Prediction Project

**File:** [`Lung_Cancer_Data_Analyse.ipynb`](./Lung_Cancer_Data_Analyse.ipynb)

This project focuses on analyzing a dataset related to factors influencing lung cancer and building a predictive model.

- **Objective:** To identify key risk factors for lung cancer through EDA and develop a classification model to predict the likelihood of diagnosis.
- **Dataset Source:** [Lung Cancer Dataset on Kaggle](https://www.kaggle.com/datasets/aagambshah/lung-cancer-dataset)
- **Key Techniques Used:**
    - Data Cleaning & Preprocessing (handling numerical encodings, stripping whitespace)
    - Exploratory Data Analysis (EDA) including distributions, cross-tabulations, and correlation analysis (heatmap).
    - Logistic Regression for binary classification.
    - Model Evaluation (Accuracy, Confusion Matrix, Classification Report).
    - Prediction on new, unseen data.
- **Key Insights:**
    - Initial analysis revealed no missing values, allowing for straightforward preprocessing.
    - Strong correlations were found between Lung Cancer diagnosis and symptoms like **Chest Pain, Shortness of Breath, and Coughing**.
    - The trained Logistic Regression model demonstrated high confidence in predicting lung cancer for a new data point based on these key indicators.
 
  How We Found the Model's Prediction for New Data:
The process of finding the prediction for a new data point involves several crucial steps, primarily data preprocessing and then applying the trained machine learning model.

Defining the New Patient's Data:

What we did: We started by creating a Python dictionary called new_patient_data. This dictionary holds the specific values for each feature (like 'GENDER', 'AGE', 'SMOKING', etc.) for the hypothetical new patient we want to test.
Why it's important: This is our raw input. It mimics how you might receive new patient information in a real-world scenario.
Converting to a Pandas DataFrame:

What we did: The new_patient_data dictionary was then converted into a Pandas DataFrame named new_patient_df.
Why it's important: Pandas DataFrames are the standard structure that scikit-learn models (like our Logistic Regression) expect as input for features.
Preprocessing the New Data to Match Training Format:

What we did: This is the most critical step shown in your image_7df8bb.png.
Binary Feature Mapping: We used the binary_features_str list (containing names like 'SMOKING', 'YELLOW_FINGERS', etc.) to iterate through these columns in new_patient_df. For each, we applied a .map({'No': 0, 'Yes': 1}) operation. This converts the human-readable 'Yes'/'No' strings into the numerical 0s and 1s that our model was trained on.
Gender Mapping: Similarly, the 'GENDER' column was mapped from 'Male'/'Female' to 0/1 using .map({'Male': 0, 'Female': 1}).
Why it's important: The machine learning model was trained on data where 'Yes' symptoms were 1 and 'No' symptoms were 0, and 'Female' was 1 and 'Male' was 0 (or vice-versa, depending on your mapping). If the new data isn't transformed to this exact numerical format, the model won't understand it, or it will make incorrect predictions. This step ensures consistency.
Ensuring Column Order Consistency (expected_column_order):

What we did: We defined an expected_column_order list, which contains all the feature names in the exact sequence that the model expects them. This order was derived from the X_train.columns (or X.columns) during the model training phase. Then, we used new_patient_df[expected_column_order] to rearrange the columns of new_patient_df into this specific order.
Why it's important: Machine learning models are sensitive to the order of features. If you train a model expecting 'AGE' in the second column and 'SMOKING' in the third, and then feed it new data with 'SMOKING' in the second and 'AGE' in the third, it will interpret the values incorrectly, leading to nonsensical predictions. This step ensures that the new data's features are presented to the model in the same sequence it learned from.
Making the Prediction (model.predict and model.predict_proba):

What we did: After new_patient_df_processed was ready, we passed it directly to our trained model.
prediction = model.predict(new_patient_df_processed): This command asks the model to classify the patient based on the preprocessed features. It outputs 0 (No Lung Cancer) or 1 (Lung Cancer).
prediction_proba = model.predict_proba(new_patient_df_processed): This command asks the model for the probability of the patient belonging to each class (0 and 1). [:, 1] extracts the probability for class 1 (Lung Cancer 'Yes').
Why it's important: This is the core "prediction" step. The model applies the mathematical relationships it learned during training to the new input data to determine the most likely outcome. The probabilities give us a measure of the model's confidence in its classification.
In essence, we took the raw, human-readable patient data, transformed it into the precise numerical and structural format the model understood, and then asked the trained model to give us its best estimate of whether that patient has lung cancer, along with its confidence in that estimate.


