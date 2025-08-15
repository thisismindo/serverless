# AWS Lambda Python Demo

This repository provides a simple demonstration of an **AWS Lambda function** built with Python, using **API Gateway** as the trigger and **Lambda Layers** to manage dependencies. This project uses the Serverless Framework to define and deploy the infrastructure as code.

## Key Features

* **Serverless Architecture**: Deploys a Python Lambda function without managing servers.
* **API Gateway Integration**: Exposes the Lambda function via a REST API endpoint.
* **Lambda Layers**: Efficiently bundles and manages Python dependencies, keeping the deployment package small and improving cold start times.

---

## Prerequisites

To deploy this project, ensure you have the following tools installed and configured:

* **AWS CLI**: Version `2.27.x` or higher.
* **Python**: Version `3.12.x` or higher.
* **Node.js**: Version `v23.1.x` or higher.
* **npm**: Version `11.5.x` or higher.
* **Serverless Framework**: Version `4.18.x` or higher.
* **pip**: Version `25.1.x` or higher.

---

## Getting Started

Follow these steps to set up the project locally and deploy it to your AWS account.

### 1. AWS Setup

First, you need to configure your AWS environment.

1.  **Install the AWS CLI**: If you haven't already, install the AWS CLI by following the official [installation guide](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html).
2.  **Configure AWS Credentials**: Set up your credentials using `aws configure`. This will allow the Serverless Framework to deploy resources to your account.
    ```bash
    aws configure
    ```
3.  **Update Configuration**: Open `resources.yml` and update the VPC security group and subnet IDs to match your AWS environment.
    * **VPC Security Group IDs**: Modify the values on [line 94](https://github.com/thisismindo/serverless/blob/main/resources.yml#L94).
    * **Subnet IDs**: Modify the values on [lines 104-106](https://github.com/thisismindo/serverless/blob/main/resources.yml#L104-L106).

4.  **Create an S3 Bucket**: The Serverless Framework uses an S3 bucket to store deployment artifacts. Create one using the AWS CLI. Be sure to replace `<REGION>` and `sls-dev-demo-582305` with your desired region and a unique bucket name.
    ```bash
    aws s3 mb s3://sls-dev-demo-582305 --region <REGION>
    ```

### 2. Local Environment Setup

1.  **Install Serverless Framework**: Install the Serverless Framework globally via npm.
    ```bash
    npm install -g serverless
    ```
2.  **Set Up Python Environment**: Create and activate a virtual environment to manage project dependencies. This project uses `pipenv`.
    ```bash
    pipenv shell --python 3.12
    ```
3.  **Install Development Dependencies**: Install the Python packages needed for local development.
    ```bash
    pip install -r src/requirements.txt
    ```

### 3. Build Lambda Layers

To keep the Lambda deployment package small, dependencies are packaged into a Lambda Layer.

* **Package Dependencies**: Install the required Python packages into the specific directory structure needed for AWS Lambda Layers.
    ```bash
    mkdir -p packages/python/lib/python3.12/site-packages/
    pip install -r src/requirements.txt --target=packages/python/lib/python3.12/site-packages/
    ```

---

## Deployment

### Deploying to AWS

Use the Serverless Framework to deploy the entire stack.

* **Package and Verify**: Run a dry-run to ensure the deployment package is correctly configured before deploying.
    ```bash
    serverless package --stage dev --debug
    ```
* **Deploy**: Deploy the Lambda function, API Gateway, and Lambda Layer to your AWS account.
    ```bash
    sls deploy --stage dev
    ```

### Tearing Down the Project

To remove all resources and clean up your AWS account, run the following commands.

1.  **Remove Serverless Stack**:
    ```bash
    sls remove --stage dev
    ```
2.  **Delete S3 Bucket**:
    ```bash
    aws s3 rb s3://<BUCKET_NAME> --force
    ```

---

## Technical Stack

* **Language**: [Python](https://www.python.org/)
* **Framework**: [Serverless Framework](https://www.serverless.com/)
* **Cloud Provider**: [Amazon Web Services (AWS)](https://aws.amazon.com/)
