# ai-powered-sme-cyber-threat-detection
AI-powered cyber threat detection system for Nigerian SMEs
# AI-Powered Cyber Threat Detection System for Nigerian SMEs

This project implements a lightweight AI-based anomaly detection system designed for small and medium enterprises in Nigeria.

## Features
- Machine learning-based threat detection
- Low-resource system design
- SME-friendly alerting mechanism
- Reproducible and transparent architecture

## Dataset
CICIDS2017 dataset from the Canadian Institute for Cybersecurity.

## How to Run
1. Install dependencies:
   pip install -r requirements.txt

2. Place dataset CSV files in:
   data/raw/

3. Run notebooks in order:
   notebooks/01_data_loading.ipynb
   notebooks/02_preprocessing.ipynb
   notebooks/03_model_training.ipynb
   notebooks/04_evaluation.ipynb

4. Launch dashboard:
   streamlit run dashboard/app.py

## Academic Use
This system was developed as part of a design-based postgraduate thesis.
