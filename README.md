# 🤖 ML_ST: End-to-End MLOps Workflow with GitHub Actions + DVC + W&B

This repository showcases a complete machine learning pipeline powered by modern MLOps tools, demonstrating **automated training, data versioning, experiment tracking, and model artifact management**.

---

## ✨ Features

* ✅ **Automated Training**: Seamless model training triggered by **GitHub Actions** on every push to the `main` branch.
* 📦 **Data Versioning**: Robust dataset management using **DVC (Data Version Control)**, with remote storage on Google Drive.
* 📊 **Experiment Tracking**: Comprehensive metrics logging (e.g., accuracy) and experiment comparison facilitated by **Weights & Biases (W&B)**.
* 📤 **Model Artifact Storage**: Automatic saving of trained models (`model.pkl`) as artifacts with each successful run.

---

## 🚀 How It Works

### 🔄 1. Continuous Integration with GitHub Actions

Our `run-model.yml` workflow orchestrates the entire ML pipeline:

* **Data Pull**: Fetches the latest `data.csv` from Google Drive using DVC.
* **Model Training**: Executes `model.py` to train the machine learning model.
* **Metrics Logging**: Pushes training metrics (like accuracy) to Weights & Biases for real-time monitoring and comparison.
* **Artifact Upload**: Saves the trained `model.pkl` as a GitHub Action artifact, making it easily accessible for deployment or further analysis.

### 📦 2. Data Versioning with DVC

The `data.csv` dataset is version-controlled using DVC, with its remote storage residing on **Google Drive**. Instead of committing large data files directly to Git, a small `.dvc` file (`data.csv.dvc`) acts as a pointer to the actual data. This ensures:

* Lightweight Git repository.
* Reproducible data environments for every experiment.
* Automatic data fetching by our CI/CD pipeline.

### 📊 3. Experiment Tracking with Weights & Biases (W&B)

Every model training run automatically logs key metrics, such as `accuracy`, to your W&B project. This provides:

* A centralized dashboard to visualize and compare experiment results.
* The ability to track hyperparameter changes and their impact on model performance.
* Enhanced collaboration when working in teams.

---

## 📁 Project Structure

ML_ST/
├── data.csv                # DVC-tracked dataset
├── data.csv.dvc            # DVC pointer file for the dataset
├── model.py                # Python script for model training
├── model.pkl               # Saved trained model (artifact)
├── dvc-sa-key.json         # (Ignored) Google Drive service account key for DVC authentication
├── .dvc/                   # DVC metadata directory
└── .github/workflows/
└── run-model.yml       # GitHub Actions workflow definition


---

## 🧪 Metrics Example (via W&B)

[![GitHub Workflow Status](https://github.com/Hasee10/ML_ST/actions/workflows/run-model.yml/badge.svg)](https://github.com/Hasee10/ML_ST/actions/workflows/run-model.yml)
[![DVC Versioning](https://img.shields.io/badge/DVC-enabled-blue)](https://dvc.org/)
[![W&B Logging](https://img.shields.io/badge/W%26B-logging-green)](https://wandb.ai/)

Explore the experiment results and compare different model runs directly on the Weights & Biases platform:

[🔗 Click to view on Weights & Biases](https://wandb.ai/YOUR_USERNAME/mlops-demo)
*(Remember to replace `YOUR_USERNAME` with your actual W&B username to view your project.)*

---

## 📦 Setup Instructions (for local development)

To get this project running on your local machine, follow these simple steps:

### 1. Clone the Repository

### bash
git clone [https://github.com/Hasee10/ML_ST.git](https://github.com/Hasee10/ML_ST.git)
cd ML_ST
2. Install Python Dependencies
Install all necessary packages using pip:

Bash

pip install -r requirements.txt
# Alternatively, install them individually:
# pip install scikit-learn wandb dvc[gdrive]
3. Pull the Dataset
To get the data.csv file, you'll need to pull it using DVC. Ensure you have configured your Google Drive service account key (dvc-sa-key.json) if you're not using GitHub Actions.

Bash

dvc pull
4. Run the Model Locally
You can run the model training script independently:

Bash

python model.py
