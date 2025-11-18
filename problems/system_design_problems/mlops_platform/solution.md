# MLOps Platform Design

## Architecture Diagram

The MLOps platform architecture diagram is available in multiple formats:

### Local File

- ![MLOps Platform Architecture](Design%20a%20MLOps%20Platform.drawio.png)

### Interactive Online Diagram

- [View and Edit on diagrams.net](https://viewer.diagrams.net/?tags=%7B%7D&lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&dark=auto#G16UYhGXmdZ1Jm53mx9D39qRrbyoCm1Wji)

## Overview

This architecture demonstrates a comprehensive MLOps platform that includes:

- **Data Sources**: MySQL, DynamoDB, MongoDB, S3
- **Data Ingestion**: AWS DMS with CDC (Change Data Capture)
- **Data Lake**: S3 for raw and processed data storage
- **Data Processing**: Medallion Architecture (Bronze, Silver, Gold layers) with Apache Hudi
- **Real-time Processing**: DynamoDB for real-time production data capture
- **Feature Store**: Centralized feature storage in S3
- **Query Engine**: AWS Athena / Presto for data analysis
- **ML Training**: Model training pipeline with SageMaker
- **Model Storage**: S3 for storing model weights (2/3 models)
- **Testing**: A/B testing capabilities
- **Deployment**: Load Balancer, CDN for serving to customer-facing mobile apps
- **Orchestration**: CRON-based scheduling for data drift measurement and model retraining
- **MLOps**: ML Engineer workflows for manual triggers and monitoring
- **Visualization**: Data visualization tools for analysis

The platform supports the complete ML lifecycle from data ingestion to model deployment and monitoring.
