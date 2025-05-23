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
    - *(You can elaborate on 2-3 most impactful insights here, keeping it concise for the README)*


