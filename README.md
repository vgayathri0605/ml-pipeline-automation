# AI/ML Production Pipeline Project

This project demonstrates an automated machine learning pipeline for customer churn prediction.

## Features

- Data ingestion and preprocessing
- Machine learning model training using Scikit-learn
- Prediction API using FastAPI
- Cloud storage using AWS S3
- Event-driven automation using AWS Lambda
- Monitoring and logs using CloudWatch

## Architecture

New Dataset → Amazon S3 → Lambda Trigger → ML Pipeline → Model → FastAPI API

## Technologies Used

Python  
Scikit-learn  
FastAPI  
AWS S3  
AWS Lambda  
CloudWatch  

## Project Structure

src/
- ingest.py
- preprocess.py
- train_model.py
- predict.py
- upload_to_s3.py

api/
- app.py

## Workflow

1. Dataset uploaded to S3
2. S3 triggers Lambda
3. Lambda runs ML pipeline
4. Model is trained and saved
5. FastAPI serves predictions