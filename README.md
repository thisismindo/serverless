# Overview
A simple demonstration of aws lambda using python with api gateway and lambda layers resources.

# Requirements
- serverless >= 3.27.0
- aws-cli >= 1.22.87
- python >= 3.9.x
- botocore >= 1.24.32
- npm >= 9.4.0
- node >= v19.6.0
- pip >= 22.3.1

# Setup
- install [aws-cli](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)
- configure [aws-cli](https://docs.aws.amazon.com/cli/latest/reference/configure/)
- update [vpc security group ids](https://github.com/thisismindo/serverless/blob/main/resources.yml#L13)
- update [subnet ids](https://github.com/thisismindo/serverless/blob/main/resources.yml#L21-L23)
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
```

# Technical Specifications
- Language(s)
    - [python](https://www.python.org/)
- Framework(s)
    - [serverless](https://www.serverless.com/)
    - [npm](https://www.npmjs.com/)
- Platform
    - [aws](https://aws.amazon.com/)
