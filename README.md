---
title: Croppredict
emoji: 👀
colorFrom: blue
colorTo: pink
sdk: docker
pinned: false
---

# 🌱 CropSense — Crop Recommendation System

A Flask web application that predicts the most suitable crop to grow based on soil nutrient parameters. Built with Scikit-learn and deployed with a clean, responsive UI.

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-2.3%2B-black?logo=flask)](https://flask.palletsprojects.com)
[![Scikit-learn](https://img.shields.io/badge/Scikit--learn-1.3%2B-orange?logo=scikit-learn)](https://scikit-learn.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

---

**Live Demo:** https://crop-predict-wgrr.onrender.com/

**Alternate Link:** https://lovnishverma-croppredict.hf.space/

**HF Space:** https://huggingface.co/spaces/LovnishVerma/croppredict

## 📌 Overview

CropSense takes 11 soil parameters as input and recommends the most suitable crop using a **Logistic Regression** model trained on the [Crop dataset](https://raw.githubusercontent.com/lovnishverma/datasets/refs/heads/main/Crop.csv). It also returns the **top-3 predictions with confidence percentages**.

This project was developed as a teaching artifact for the **IndiaAI Foundations of Artificial Intelligence** programme at **NIELIT Ropar**, demonstrating the end-to-end ML workflow: data → model → deployment.

---

## 🗂️ Project Structure

```
crop-predict/
├── app.py                          # Flask application
├── classification.ipynb            # Model training notebook (Colab)
├── crop_recommendation_model.joblib  # Saved trained model
├── requirements.txt
├── README.md                          # This File (Documentation)
├── static/
│   └── css/                        # Stylesheets
└── templates/
    └── index.html                  # Frontend UI
```

---

## 🧪 Input Features

The model uses 11 soil parameters:

| Feature | Description          | Unit   |
|---------|----------------------|--------|
| N       | Nitrogen             | kg/ha  |
| P       | Phosphorus           | kg/ha  |
| K       | Potassium            | kg/ha  |
| ph      | pH Level             | —      |
| EC      | Electrical Conductivity | dS/m |
| S       | Sulfur               | mg/kg  |
| Cu      | Copper               | mg/kg  |
| Fe      | Iron                 | mg/kg  |
| Mn      | Manganese            | mg/kg  |
| Zn      | Zinc                 | mg/kg  |
| B       | Boron                | mg/kg  |

**Sample values** (pomegranate): `175, 36, 216, 5.9, 0.15, 0.28, 15.69, 114.20, 56.87, 31.28, 28.62`

---

## ⚙️ ML Pipeline

```
Dataset (Crop.csv)
    ↓
Feature/Target Split (X = 11 soil params, y = crop label)
    ↓
Train-Test Split (80/20, random_state=42)
    ↓
Logistic Regression (sklearn)
    ↓
Evaluation (accuracy_score, classification_report, confusion matrix)
    ↓
Model Serialization (joblib → .joblib file)
    ↓
Flask REST API (/predict)
```

See [`classification.ipynb`](classification.ipynb) for the full training walkthrough.

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/lovnishverma/crop-predict.git
cd crop-predict
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the app

```bash
python app.py
```

Open your browser at **http://127.0.0.1:5000**

> **Note:** The pre-trained `crop_recommendation_model.joblib` is already included. If you want to retrain, open `classification.ipynb` in Google Colab and run all cells — it will regenerate the `.joblib` file.

---

## 🌐 API Reference

### `POST /predict`

Accepts `multipart/form-data` with all 11 soil parameters.

**Request (curl example):**

```bash
curl -X POST http://127.0.0.1:5000/predict \
  -F "N=175" -F "P=36" -F "K=216" -F "ph=5.9" -F "EC=0.15" \
  -F "S=0.28" -F "Cu=15.69" -F "Fe=114.20" -F "Mn=56.87" \
  -F "Zn=31.28" -F "B=28.62"
```

**Response:**

```json
{
  "crop": "pomegranate",
  "top3": [
    { "crop": "pomegranate", "prob": 87.3 },
    { "crop": "mango",       "prob": 7.1  },
    { "crop": "grapes",      "prob": 3.2  }
  ]
}
```

---

## 📦 Requirements

```
flask>=2.3
scikit-learn>=1.3
pandas>=2.0
joblib>=1.3
numpy>=1.24
gunicorn>=20.1.0
```

---

## 📊 Dataset

- **Source:** [`lovnishverma/datasets`](https://github.com/lovnishverma/datasets) → `Crop.csv`
- **Features:** 11 soil nutrient columns
- **Target:** `label` — crop name (e.g. pomegranate, wheat, rice, maize, etc.)

---

## 🙋 Author

**Lovnish Verma**
Project Engineer, NIELIT Ropar (Deemed University), Punjab

[![GitHub](https://img.shields.io/badge/GitHub-lovnishverma-black?logo=github)](https://github.com/lovnishverma)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-lovnishverma-blue?logo=linkedin)](https://linkedin.com/in/lovnishverma)
[![HuggingFace](https://img.shields.io/badge/HuggingFace-lovnishverma-yellow?logo=huggingface)](https://huggingface.co/lovnishverma)
[![Portfolio](https://img.shields.io/badge/Portfolio-lovnishverma.in-green)](https://lovnishverma.in)

---

## 📄 License

This project is licensed under the MIT License.

---

Docs: Docs on specifying a Python version: https://render.com/docs/python-version

> Built for IndiaAI students at NIELIT Ropar · No brainrot. Just facts. 🌾

