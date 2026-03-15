# AI/ML Production Pipeline Project

Goal:
Build an end-to-end machine learning pipeline using Python and AWS that simulates a real production ML system.

The pipeline will include:
- Data ingestion
- Data preprocessing
- Feature engineering
- Model training
- Model storage
- API deployment
- Automation with AWS services

---

# Project Architecture (High Level)

Raw Data
   ↓
Python Ingestion Script
   ↓
Processed Dataset
   ↓
Feature Engineering
   ↓
Machine Learning Model
   ↓
Prediction API
   ↓
Automation & Monitoring

---

# Project Folder Structure

ai_ml_pipeline_project
│
├── data
│   ├── raw
│   └── processed
│
├── src
│
├── models
│
├── api
│
├── lambda
│
├── config
│
├── logs
│
└── NOTES.md


Folder Explanation

data/raw
Stores the original dataset.

data/processed
Stores cleaned or transformed datasets used for ML training.

src
Contains Python scripts for the ML pipeline.

models
Stores trained machine learning models.

api
Contains code for prediction API.

lambda
Contains AWS Lambda automation scripts.

logs
Stores pipeline logs.

---

# Step 1 – Project Setup

Created the project folder and standard ML project structure.

Purpose:
Organize data, models, and code similar to real industry ML repositories.

Key Concept:
ML projects separate raw data, processed data, models, and code to maintain reproducibility.

---

# Step 2 – Dataset Creation

Dataset Name:
Customer Churn Dataset

Goal:
Predict whether a customer will leave a service.

Dataset Location:
data/raw/customer_churn.csv

Columns in Dataset

customer_id
Unique identifier for each customer

age
Age of the customer

monthly_bill
Monthly subscription cost

contract_type
Type of contract (monthly or yearly)

support_calls
Number of customer support calls

churn
Target variable
0 = customer stays
1 = customer leaves

---

# Machine Learning Concepts

Features (Input Variables)

age
monthly_bill
contract_type
support_calls

Target (Prediction Variable)

churn

Machine Learning Model Goal

Features → Predict churn

Example

Input:
Age = 30
Monthly bill = 75
Support calls = 3

Output:
Churn prediction = 1 (customer may leave)

---

# Step 3 – Data Ingestion

Purpose:
Load raw dataset into the machine learning pipeline.

Script:
src/ingest.py

Tools Used

Python
Pandas

Key Function

pd.read_csv()

This loads the dataset into a Pandas DataFrame.

Process

1. Read dataset from data/raw
2. Load dataset into Python DataFrame
3. Save a copy of the dataset into data/processed

Important Industry Practice

Raw data should never be modified directly.

Instead:
Raw dataset → Processed dataset

This ensures reproducibility and data integrity.

Output File

data/processed/clean_data.csv

## Step 4 – Data Preprocessing

Purpose
Prepare the dataset for machine learning models.

Tasks Performed
1. Load processed dataset
2. Remove missing values
3. Convert categorical values into numeric values

Why This Is Needed
Machine learning models cannot understand text values.

Example

contract_type

monthly
yearly

Converted To

monthly → 0
yearly → 1

Output File

data/processed/ml_ready_data.csv

Libraries Used

pandas
Used for data manipulation and loading datasets.

scikit-learn
Used for machine learning algorithms and model training.

joblib
Used to save trained machine learning models.

## Step 6 – Model Inference (Predictions)

Purpose

Use the trained machine learning model to make predictions on new data.

Script

src/predict.py

Process

1. Load the trained model using joblib
2. Create input data for a new customer
3. Convert input to a DataFrame
4. Run model prediction
5. Output churn prediction

Concept

Inference is the stage where trained models are used to generate predictions in production systems.

Example

Input

Age = 30
Monthly bill = 75
Support calls = 3
Contract type = monthly

Output

Prediction → Customer will stay or churn

## Step 7 – API Deployment

Purpose:
Expose the trained ML model as a web API.

Framework:
FastAPI

Server:
Uvicorn

Endpoints:

GET /
Returns a message confirming that the API is running.

POST /predict
Accepts customer data and returns churn prediction.

Example Input

{
 "age": 30,
 "monthly_bill": 75,
 "contract_type": 0,
 "support_calls": 3
}

Example Output

{
 "prediction": "Customer will stay"
}

Concept

Machine learning models are deployed as APIs so applications,
web services, and dashboards can request predictions in real time.

IAM users allow secure programmatic access to AWS services.
Access keys are used by applications to authenticate with AWS APIs.

The command "aws s3 ls" lists all S3 buckets accessible by the configured IAM user.
This confirms that AWS CLI authentication is working correctly.

S3 triggers Lambda only for new events.
Files uploaded before the trigger configuration do not activate Lambda.

ML pipelines are designed to process new datasets without changing code.

The same pipeline scripts are reused for future data.

Only the dataset changes while the processing workflow remains constant.