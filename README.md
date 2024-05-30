
## 2ND END TO END PROJECT - TEXT SUMMERIZATION
This is going to be an NLP PROJECT.

    We will be using Huggiing face for transformer based API.
    we will be using github to commit our code. because code management is important.

## what will cover:
    Text summerization is 
    setup github
    set up template creation to have a flow
    requirement installation like transformer 
    we will talk about logging 
    project overflow
    notebook experiment : 
    writing our modular coding --- python
    training pipeline
    Prediction pipeline because we need to make our prediction. and also user App Creation
    Final is the ci/cd ON AWS and Github action.


## Prerequisite
    python
    NLP --BASIC HIGGING FACE
    AWS aCCOUNT
    Your dedication


## What is will learn at the end of the project:
    - able to create a Text Summarizer from scratch.-


## we will do these components:
    1. Data ingestion
    2. Data Validation
    3. Data Transformation
    4. model trainer
    5. model evaluation
    6. Prediction pipeline or user input


# End to end project work flow
    Update config.yaml in config
    Update params.yaml
    Update entity -------------------------------- in src - textsummerizer - enitiy - __init_py
    Update the configuration manager in src config -------------------------------- src - config - configurationmanager
    update the conponents in src---------------src-components - dataingestion.py
    update the pipeline in src
    update the main.py
    update the app.py



# AWS-CICD-Deployment-with-Github-Actions
## 1. Login to AWS console.
## 2. Create IAM user for deployment

    #with specific access

    1. EC2 access : It is virtual machine

    2. ECR: Elastic Container registry to save your docker image in aws


    #Description: About the deployment

    1. Build docker image of the source code

    2. Push your docker image to ECR

    3. Launch Your EC2 

    4. Pull Your image from ECR in EC2

    5. Lauch your docker image in EC2

    #Policy:

    1. AmazonEC2ContainerRegistryFullAccess

    2. AmazonEC2FullAccess

## 3. Create ECR repo to store/save docker image
    - Save the URI: 566373416292.dkr.ecr.us-east-1.amazonaws.com/text-s

## 4. Create EC2 machine (Ubuntu)
## 5. Open EC2 and Install docker in EC2 Machine:

    #optinal

    sudo apt-get update -y

    udo apt-get upgrade

    #required

    curl -fsSL https://get.docker.com -o get-docker.sh

    sudo sh get-docker.sh

    sudo usermod -aG docker ubuntu

    newgrp docker


## 6. Configure EC2 as self-hosted runner:
    setting>actions>runner>new self hosted runner> choose os> then run command one by one

## 7. Setup github secrets:
    AWS_ACCESS_KEY_ID=

    AWS_SECRET_ACCESS_KEY=

    AWS_REGION = us-east-1

    AWS_ECR_LOGIN_URI = demo>>  566373416292.dkr.ecr.ap-south-1.amazonaws.com

    ECR_REPOSITORY_NAME = simple-app