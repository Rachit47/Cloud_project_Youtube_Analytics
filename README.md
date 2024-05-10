Aim:
This project seeks to securely manage, streamline, and conduct analysis on both structured and semi-structured YouTube video data. The analysis focuses on video categories and trending metrics.

Objectives:

1. Data Ingestion: Develop a mechanism to collect data from diverse sources.
2. ETL System: Transform raw data into the appropriate format.
3. Data Lake: Establish a centralized repository for data from various sources.
4. Scalability: Ensure the system scales effectively as the data volume grows.
5. Cloud Integration: Utilize cloud services, particularly AWS, for processing large datasets.
6. Reporting: Construct a dashboard to address key questions derived from the analysis.

AWS services utilized:

1. Amazon S3: A scalable object storage service offering robust data management features.
2. AWS IAM: Identity and Access Management for secure management of AWS services.
3. Amazon QuickSight: A cloud-based, machine learning-driven business intelligence service.
4. AWS Glue: Serverless data integration service for data discovery, preparation, and consolidation.
5. AWS Lambda: Serverless computing service for executing code without managing servers.
6. AWS Athena: Interactive query service for analyzing data stored in S3 without the need for data loading.

Dataset Description:
The project employs a Kaggle dataset comprising CSV files containing statistics on daily popular YouTube videos spanning several months.
Each day, up to 200 trending videos are published across various locations, with data for each region stored in separate files. 
The dataset includes information such as video title, channel title, publication time, tags, views, likes, dislikes, description, and comment count. 
Additionally, a category_id field specific to each region is included in the associated JSON file.

Link: https://www.kaggle.com/datasets/datasnaek/youtube-new
