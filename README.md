# 🤖 ML_ST: End-to-End MLOps Workflow with GitHub Actions + DVC + W&B

![GitHub Workflow Status](https://github.com/Hasee10/ML_ST/actions/workflows/run-model.yml/badge.svg)
![DVC Versioning](https://img.shields.io/badge/DVC-enabled-blue)
![W&B Logging](https://img.shields.io/badge/W%26B-logging-green)

A complete machine learning pipeline powered by modern MLOps tools:
- ✅ **Automated training** using GitHub Actions
- 📦 **Data versioning** via DVC + Google Drive
- 📊 **Metrics logging** with Weights & Biases (W&B)
- 📤 **Model artifact storage** on each run

---

## 📁 Project Structure

ML_ST/
├── data.csv # DVC-tracked dataset
├── data.csv.dvc # Dataset version pointer
├── model.py # Model training script
├── model.pkl # Saved model (artifact)
├── dvc-sa-key.json # (Ignored) GDrive auth key
├── .dvc/ # DVC metadata
└── .github/workflows/
└── run-model.yml # GitHub Actions workflow


---

## 🚀 How It Works

### 🔄 1. GitHub Actions
Every push to `main`:
- Pulls dataset from GDrive using DVC
- Trains the model in `model.py`
- Logs metrics to W&B
- Uploads `model.pkl` as an artifact

### 📦 2. Dataset Versioning with DVC
- The dataset `data.csv` is stored remotely on **Google Drive**
- A lightweight `.dvc` file tracks its version
- Data is pulled automatically by CI/CD

### 📊 3. Experiment Tracking with W&B
- Every model run logs `accuracy` to Weights & Biases
- Easily compare performance across versions

---

## 🧪 Metrics Example (via W&B)

[🔗 Click to view on Weights & Biases](https://wandb.ai/YOUR_USERNAME/mlops-demo)  
(Make sure to replace `YOUR_USERNAME` with your actual W&B username)

---

## 📦 Setup Instructions (for local development)

### 1. Clone the repo

bash
git clone https://github.com/Hasee10/ML_ST.git
cd ML_ST
---


2. Install Python packages
bash
Copy
Edit
pip install -r requirements.txt
# Or manually:
pip install scikit-learn wandb dvc[gdrive]
3. Pull the dataset from Google Drive
bash
Copy
Edit
dvc pull
Make sure you've configured the correct service account key for DVC if not using GitHub.

4. Run model locally
bash
Copy
Edit
python model.py

