MLOps-Project
This repository contains the implementation of an MLOps pipeline integrating MLFlow for model versioning, Airflow for workflow automation, and a full-stack application with CI/CD pipelines for Docker and Kubernetes deployment. The project also demonstrates the integration of DVC for data and model versioning, along with a professional Medium blog showcasing the entire process.

Project Overview
This project is designed to help you gain hands-on experience with essential MLOps concepts, including versioning models, automating workflows, and deploying models in production. We use MLFlow for model versioning and logging, Airflow for orchestrating tasks, and Docker and Kubernetes for application deployment.

Tools and Technologies Used:
MLFlow: For model versioning, logging, and managing model registry.
Airflow: For workflow automation and scheduling.
Flask: For building the backend REST API.
React: For building the frontend interface.
DVC (Data Version Control): For managing datasets and models.
Git: For version control with a branch-based workflow.
Docker: For containerizing the application.
Kubernetes: For deploying the application in a Kubernetes cluster (Minikube for local development).
CI/CD: GitHub Actions for continuous integration and deployment.

Installation
Prerequisites:
Docker: Install Docker for containerization.
Minikube: Install Minikube for local Kubernetes cluster.
Python 3.x: Install Python 3.x to run backend APIs and MLFlow.
Node.js: Install Node.js for running the React frontend (if using React).
Git: For managing version control and branches.
DVC: Install DVC for data versioning.
Airflow: Install Apache Airflow for workflow automation.

Step-by-Step Installation:

Clone the repository:
git clone https://github.com/ahmadnaeem10/MLOps-Project.git
cd MLOps-Project

Set up a virtual environment:
python3 -m venv venv
source venv/bin/activate  # For Linux/macOS
.\venv\Scripts\activate  # For Windows

Install the required Python dependencies:
pip install -r requirements.txt

Set up DVC for data versioning:
dvc init

Set up MLFlow:
Install and configure MLFlow.
Use mlflow.start_run() to log metrics, hyperparameters, and models during training.

Run Airflow:
Install Apache Airflow and configure the workflow using the provided DAG files.
Set up your tasks such as data preprocessing, training, and model evaluation.

Run the Backend API:
Use Flask or FastAPI to serve the model and handle prediction requests.

Run the Frontend:
npm start

Run Complete App:
python run.py

Dockerize the Application:
Build and run Docker containers for the backend and frontend using the provided Dockerfile.

Deploy on Kubernetes:
Use Kubernetes manifests to deploy the Dockerized application on a Minikube cluster.

Branch Workflow

This project follows a branch-based workflow to ensure efficient collaboration and testing:
Dev: For active development. Push features and fixes here.
Testing: For automated testing. CI pipelines trigger on commits here.
Prod: For production deployment. CD pipelines trigger on merging to prod.

Git Workflow:
Create a new feature branch:
git checkout -b feature/your-feature-name

Commit and push changes:
git commit -m "Your commit message"
git push origin feature/your-feature-name
Open a pull request (PR) to merge changes into the dev branch.

CI/CD Pipelines:
When pushing to testing, GitHub Actions triggers CI pipelines.
Merging testing into prod triggers CD pipelines that deploy the app on Kubernetes.
CI/CD Pipeline
Continuous Integration (CI)
CI pipelines run on commits to the Testing branch.

These pipelines include:
Running unit tests (e.g., with pytest).
Building and pushing Docker images to DockerHub.
Continuous Deployment (CD)
The CD pipeline is triggered when merging into the Prod branch.
It pulls the Docker image from DockerHub and deploys it to a Minikube Kubernetes cluster using deployment manifests.
Model Versioning with MLFlow
MLFlow is used for tracking models, metrics, and parameters throughout training.
Models are registered in the MLFlow Model Registry with stages (e.g., staging, production).
Use mlflow.log_metric() and mlflow.log_param() to log metrics and hyperparameters during training.
Models are saved and versioned using mlflow.pyfunc.save_model() and loaded with mlflow.pyfunc.load_model().
Full-Stack Application
Frontend
A simple React app allows users to input weather features and get temperature predictions.
Backend
A Flask API is built to serve model predictions. The API takes user input, processes it, and returns the model's prediction.
Database
User authentication is handled through a SQLAlchemy-based database (SQLite).
Users can sign up, log in, and manage sessions.
Airflow Automation

Airflow orchestrates the workflow, automating tasks like:
Data collection and preprocessing.
Model training and evaluation.
Monitoring for new data and triggering retraining.

Airflow Workflow:
Tasks are defined in DAGs (Directed Acyclic Graphs).

The workflow includes tasks like:
Data preprocessing.
Model training and evaluation.
Model registration in MLFlow.

Blog Post

A professional blog will be written to showcase the implementation and learnings throughout the project. It will cover:
The purpose of the project.
Tools used (MLFlow, DVC, Airflow).
Data versioning with DVC and model versioning with MLFlow.
Workflow automation using Airflow.
Integration of CI/CD pipelines and deployment on Kubernetes.
The blog will be published on Medium and will include code snippets, diagrams, and visuals to explain the process.

Key Learnings

This project will help you understand:
How to manage data and model versioning with DVC.
How to integrate MLFlow for model versioning.
How to automate workflows using Airflow.
How to deploy applications using Docker and Kubernetes.
How to implement CI/CD pipelines with GitHub Actions.

License
This project is licensed under the MIT License - see the LICENSE file for details.

