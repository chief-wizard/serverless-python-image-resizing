# Dynamic image resizing with Python and Serverless framework

In this example, we set up a dynamic image resizing solution with AWS S3 and a Serverless framework function written in Python. We use [Pillow](https://pillow.readthedocs.io/en/stable/) for image resizing.

## Pre-requisites

In order to deploy the function, you will need the following:

- API credentials for AWS with persmissions to manage S3, IAM and API Gateway
- Docker installed locally

## Deploying the Serverless project

1. Add your AWS credentials into `deploy.sh`
2. Deploy the Serverless project using docker:

```
docker build .
docker images
docker run <container-id>
```

## Example usage

```
https://XXX.execute-api.eu-west-1.amazonaws.com/dev/100x100/test.jpg
```
