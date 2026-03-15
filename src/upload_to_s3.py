import boto3

s3 = boto3.client('s3')

bucket_name = "aiml-pipeline-gayathri"
file_name = "../data/raw/customer_churn.csv"

s3.upload_file(file_name, bucket_name, "customer_churn.csv")

print("File uploaded to S3 successfully")