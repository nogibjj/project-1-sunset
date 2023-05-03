<!-- [![CI](https://github.com/nogibjj/aws-template/actions/workflows/cicd.yml/badge.svg?branch=main)](https://github.com/nogibjj/aws-template/actions/workflows/cicd.yml)
[![Codespaces Prebuilds](https://github.com/nogibjj/aws-template/actions/workflows/codespaces/create_codespaces_prebuilds/badge.svg?branch=main)](https://github.com/nogibjj/aws-template/actions/workflows/codespaces/create_codespaces_prebuilds) -->

[![Python application test with GitHub Actions](https://github.com/nogibjj/project-1-sunset/actions/workflows/main.yml/badge.svg)](https://github.com/nogibjj/project-1-sunset/actions/workflows/main.yml)

## IDS 721 Project 1: Cloud Continuous Delivery of Microservice - Sunrise/Sunset Info

This is a microservice that provides information about sunrise/sunset time in a given location. Additionally, it can combine local weather information to suggest whether it is a good day to observe sunrise or sunset.

The microservice is built using Flask, and it is deployed on AWS. The microservice can be accessed through a simple UI that allows users to input a place and date, and it displays the corresponding sunrise and sunset times.


### Usage

To use the microservice, follow these steps:

Input a place and a date that you want to search for sunrise/sunset information.
The server will get the local sunrise/sunset info via APIs.
It gets the local weather info via APIs and builds a simple algorithm to show whether it is a good day to observe suggested sunrise and sunset.
Finally, it allows users to customize the timestamp (past or future).

### Project Tasks
* Create a microservice in Flask or Fast API
* Push source code to Github
* Configure build system to deploy changes
* Use Infrastructure as Code (IaC) to deploy code
* Use either AWS, Azure, or GCP (recommended services include Google App Engine, AWS App Runner, or Azure App Services)
* Containerization is optional but recommended

### Project Set Up
1. Create and source the virtual environment
```
python3 -m venv env
source env/bin/activate
```
2. Install Requirement
```
make install
```
3. Run flask
```
python3 app.py
```

### Containerized with Docker and Deployed with AWS ECR and Apprunner
1. Clone and open the repo in AWS Cloud9, source the virtual environment
```
source env/bin/activate
```
2. Create a Repository in AWS ECR.
3. Write the corresponding Dockerfile.
4. View the push commands in ECR, follow the steps in Cloud9 terminal. 
  - `aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 962268758789.dkr.ecr.us-east-1.amazonaws.com`
  - `docker build -t sunset .`
  - `docker tag sunset:latest 962268758789.dkr.ecr.us-east-1.amazonaws.com/sunset:latest`
  - `docker push 962268758789.dkr.ecr.us-east-1.amazonaws.com/sunset:latest`

5. Go to AWS Apprunner, click `create services` fill with default, and `create and deploy`.

*Note: To pass the health attack, you need to make sure the host address in app.py is "0.0.0.0", and the port number should match the one you expose in Dockerfile.* 

6. Your program is successfully deployed with AWS Apprunner and you will get the default domain - https://p6jsa3zbp3.us-east-1.awsapprunner.com.



#### Homepage
![Home](https://user-images.githubusercontent.com/68854273/215937259-87aa0834-f556-4336-8bb9-97afaa06730f.png) 

#### Homepage
![Duke University, 2023-02-01](https://user-images.githubusercontent.com/68854273/215937898-404b07b7-5e47-40fe-bc8b-83a61d226579.png) 

### Reference Video(s):

* Data Engineering with Python and AWS Lambda: https://learning.oreilly.com/videos/data-engineering-with/9780135964330
* Building AI & ML Applications on Google Cloud Platform: https://learning.oreilly.com/videos/building-ai-applications/9780135973462
* Reference Source Code: https://github.com/noahgift/gcp-hello-ml

### Template for AWS Projects

1. First thing to do on launch is to open a new shell and verify virtualenv is sourced.

Things included are:

* `Makefile`

* `Pytest`

* `pandas`

* `Pylint`

* `Dockerfile`

* `GitHub copilot`

* `jupyter` and `ipython` 

* Most common Python libraries for ML/DL and Hugging Face

* `githubactions` 

### Used in Following Projects

* [coursera-mlops-aws-c3-step-functions](https://github.com/nogibjj/coursera-mlops-aws-c3-step-functions)
* [coursera-mlops-aws-c3-eda](https://github.com/nogibjj/coursera-mlops-aws-c3-eda)
* [coursera-mlops-aws-c3-linear-regression](https://github.com/nogibjj/coursera-mlops-aws-c3-linear-regression)
* [coursera-mlops-aws-c30fine-tune-sagemaker-studio-lab](https://github.com/nogibjj/coursera-mlops-aws-c30fine-tune-sagemaker-studio-lab)

### References

* [Watch GitHub Universe Talk:  Teaching MLOps at scale with Github](https://watch.githubuniverse.com/on-demand/ec17cbb3-0a89-4764-90a5-9debb58515f8)
* [Building Cloud Computing Solutions at Scale Specialization](https://www.coursera.org/specializations/building-cloud-computing-solutions-at-scale)
* [Python, Bash and SQL Essentials for Data Engineering Specialization](https://www.coursera.org/learn/web-app-command-line-tools-for-data-engineering-duke)
* [Implementing MLOps in the Enterprise](https://learning.oreilly.com/library/view/implementing-mlops-in/9781098136574/)
* [Practical MLOps: Operationalizing Machine Learning Models](https://www.amazon.com/Practical-MLOps-Operationalizing-Machine-Learning/dp/1098103017)
* [Coursera-Dockerfile](https://gist.github.com/noahgift/82a34d56f0a8f347865baaa685d5e98d)

![Sunrise in Miami Beach](https://user-images.githubusercontent.com/68854273/211383609-a64c45a9-d359-4edf-9b2f-3733a3bf2e40.png)
