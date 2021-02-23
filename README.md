# MLOps Lifecycle Demo

## Developing Machine Learning Models for Practical Web Applications

**Notes:** Given the relatively large scope of the project please consider the following:
1. This project is under active development. **The App/API are NOT yet live at the links below. They are being redeployed, and updated asap**
2. Projects assets will be split over multiple repos, platforms, services, etc. Please see links below.

## Assets:

### Model Serving API:
* **Heroku Deployment:** [The public API is hosted here](https://min-flask-api.herokuapp.com/)
* **AWS Deployment:** Docker deployment via the AWS Elastic Container Registry is in development.

### Web Application
* **Client:** [Go here to view it live, and for the latest updates](https://github.com/workbench-a/mern_client_demo)
* **Server:** [Go here to view it live, and for the latest updates](https://github.com/workbench-a/mern_server_demo)

### Business Case-Studies:
* **Fashion Trends:** Real-Time Monitoring and Forecasting
 * Problem and Opportunity (Under Contruction)

### MLOps: A Guide to the Machine Learning Development LifeCycle
 * Presented as a case-study for real-time Monitoring of fashion trends
 * **Ancillary (Project / Workflow Related) Documentation:** [here](https://colab.research.google.com/drive/1fuVfAoYDDcNSTcczp8EQPE7cG_AA_H9t?usp=sharing)

### Data Science:
 * **Real-time monitoring of fashion trends:** [View the notebook](https://colab.research.google.com/drive/1k0ulpOzYYIxmu2NHuUAzJAP_8jheuDS5?usp=sharing)


# Running the project:
---

## Dev Environment:

* You need to have pyenv installed locally to build the dev environment.
  * Ubuntu Linux (or similar):
    * ```sudo bash setup_env.sh```
* You can then execute ```pipenv shell``` from the root directory to run the global development environment.
* To Do: 
  * Pipfiles need to be updated to specify the range of appropriate versions for each package.
* Misc Commands:
  * To remove uninstall environment: ```pipenv --rm```
  * To exit virtual environment: ```exit```

## Citations

**Special Notes:**

* This project was insipired by a few really excellent resources that deserve special note below.
* A complete set of sitations will be provided as the project develops (here, and in the notebooks linked above).

**MOOCS**
[Machine Learning Model Deployment](https://www.udemy.com/course/deployment-of-machine-learning-models/)
[Testing and Monitoring Machine Learning Model Deployments](https://www.udemy.com/course/testing-and-monitoring-machine-learning-model-deployments/)
[Feature Engineering for Machine Learning](https://www.udemy.com/course/feature-engineering-for-machine-learning/learn/lecture/24098280#overview)
[Docker Mastery: with Kubernetes +Swarm from a Docker Captain](https://www.udemy.com/course/docker-mastery)

**Tutorials**
[Full-Stack MERN Application - Javascript Mastery](https://www.youtube.com/playlist?list=PL6QREj8te1P7VSwhrMf3D3Xt4V6_SRkhu)

**Other Web Content**
[ML-Ops.org - A Introduction to MLOps](https://ml-ops.org/)
[Continuous Development for Machine Learing Systems](https://martinfowler.com/articles/cd4ml.html)
[Hidden Technical Debt in Machine Learning Systems - NeurIPS2015](https://papers.nips.cc/paper/2015/file/86df7dcfd896fcaf2674f757a2463eba-Paper.pdf)
