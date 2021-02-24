# MLOps Lifecycle Demo

## Developing Machine Learning Models for Practical Web Applications

**Notes:** The MLOps demo is a collection of case-studies, web applications, models, pipelines, apis, and more illustrating the deployment, testing, and monitoring of machine learning models. The goal is to demonstrate the entire machine learning lifecycle in a variety of contexts both practical and theoretical. 

1. This project is under active development. **The App/API are NOT yet live at the links below. They are being redeployed, and updated asap.**
2. Projects assets are split over multiple repos.

## Projects:

### **Real-Time Monitoring of Fashion Trends** 

### Business / MLOps Case-Study:
* A guide to the machine learning development lifecycle presented in the context of a business case-study. [notebook!](https://colab.research.google.com/drive/1Tq7Wf_JGjs_LDlg41U3sppRzLBQ0MKlD?usp=sharing) 

### Model Serving API:
* **Heroku Deployment:** [The public API is hosted here!](https://min-flask-api.herokuapp.com/)
* **AWS Deployment:** Docker deployment via the AWS Elastic Container Registry is in development.

### Web Application
* **Client:** [Go here to view it live, and for the latest updates](https://github.com/workbench-a/mern_client_demo)
* **Server:** [Go here to view it live, and for the latest updates](https://github.com/workbench-a/mern_server_demo)


### Data Science:
 * Analysis for the project: [View the notebook!](https://colab.research.google.com/drive/1k0ulpOzYYIxmu2NHuUAzJAP_8jheuDS5?usp=sharing)

## Documentation:
* To generate documentation for the desired package simple execute:  
  * ```pdoc --html --output-dir doc_build_dir package_name```

### Package Docs:
* demo-model: [Live here!](https://app.netlify.com/sites/distracted-kare-e72e69/overview)
* api: In development
* text classifier: In development

# Running the project:

## Complete Workflow Documentation:
  * Notes to help navigate the project: [here!](https://colab.research.google.com/drive/1fuVfAoYDDcNSTcczp8EQPE7cG_AA_H9t?usp=sharing)

## Dev Environment Quickstart Guide:

* You need to have pyenv installed locally to build the dev environment.
  * Ubuntu Linux (or similar):
    * ```sudo bash setup_env.sh```
* You can then execute ```pipenv shell``` from the root directory to run the global development environment.

## Citations

**Special Notes:**

* This project was insipired by a few really excellent resources that deserve special note below.
* A complete set of sitations will be provided as the project develops (here, and in the notebooks linked above).

**MOOCS**
* [Machine Learning Model Deployment](https://www.udemy.com/course/deployment-of-machine-learning-models/) - The original inspiration and template for this project!
* [Testing and Monitoring Machine Learning Model Deployments](https://www.udemy.com/course/testing-and-monitoring-machine-learning-model-deployments/)
* [Feature Engineering for Machine Learning](https://www.udemy.com/course/feature-engineering-for-machine-learning/learn/lecture/24098280#overview) \
* [Feature Selection for Machine Learning](https://www.udemy.com/course/feature-selection-for-machine-learning/learn/lecture/9341694#overview)
* [Docker Mastery: with Kubernetes +Swarm from a Docker Captain](https://www.udemy.com/course/docker-mastery)

**Tutorials**
* [Full-Stack MERN Application - Javascript Mastery](https://www.youtube.com/playlist?list=PL6QREj8te1P7VSwhrMf3D3Xt4V6_SRkhu)

**Other Web Content**
* [ML-Ops.org - A Introduction to MLOps](https://ml-ops.org/)
* [Continuous Development for Machine Learing Systems](https://martinfowler.com/articles/cd4ml.html)
* [Hidden Technical Debt in Machine Learning Systems - NeurIPS2015](https://papers.nips.cc/paper/2015/file/86df7dcfd896fcaf2674f757a2463eba-Paper.pdf)
