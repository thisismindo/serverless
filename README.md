# Overview
A simple demonstration of aws lambda using python with api gateway and lambda layers resources.

# Requirements
- serverless >= 3.28.1
- aws-cli >= 1.22.87
- python >= 3.9.x
- botocore >= 1.24.32
- npm >= 9.6.0
- node >= v19.6.1
- pip >= 22.3.1

# Setup
- install [aws-cli](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)
- configure [aws-cli](https://docs.aws.amazon.com/cli/latest/reference/configure/)
- update [vpc security group ids](https://github.com/thisismindo/serverless/blob/main/resources.yml#L15)
- update [subnet ids](https://github.com/thisismindo/serverless/blob/main/resources.yml#L23-L25)
- create s3 bucket
```sh
aws s3 mb s3://sls-dev-demo-582305 \
  --region <REGION> \
  --endpoint-url https://s3.<REGION>.amazonaws.com
```
- install serverless framework
```sh
> npm install -g serverless
```
- setup local environment
```sh
> pipenv shell
```
- install python package(s) for local development
```sh
> pip install -r src/requirements.txt
```
- install python packages(s) for aws lambda layers
```sh
> mkdir packages/python/lib/python3.9/site-packages/
> pip install -r src/requirements.txt --target=packages/python/lib/python3.9/site-packages/
```

# Deployment
```sh
> sls deploy --stage dev
```

# Tear Down
```sh
> sls remove --stage dev
> aws s3api delete-bucket --bucket <BUCKET_NAME>
```

# Technical Specifications
- Language(s)
  - [python](https://www.python.org/)
- Framework(s)
  - [serverless](https://www.serverless.com/)
  - [npm](https://www.npmjs.com/)
- Platform
  - [aws](https://aws.amazon.com/)
