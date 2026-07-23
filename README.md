# Synthetic EHR–Lifestyle Dataset for Machine Learning-Based Biomedical Prediction

## Overview

This repository contains a synthetic biomedical dataset developed for machine learning and deep learning research.

The dataset was generated using a custom Python-based data generation pipeline that integrates selected attributes from two publicly available EHR and lifestyle datasets:

1. Personalized Medication Dataset (Kaggle)
2. National Health and Nutrition Examination Survey (NHANES)

## Source Datasets

1. Personalized Medication Dataset:

Source: Kaggle

Available at https://www.kaggle.com/datasets/ziya07/personalized-medication-dataset

2. Lifestyle Dataset

Source: National Health and Nutrition Examination Survey (NHANES), Centers
for Disease Control and Prevention (CDC)

Available at: https://wwwn.cdc.gov/nchs/nhanes

These original datasets remain subject to their respective licenses and terms of use.

## Derived Dataset
## Synthetic Data Generation
The synthetic dataset contains synthetic patient records and is intended solely for research, educational, and benchmarking purposes.
The synthetic dataset was produced using custom Python programs.

Python Programs:
merge_ehr_nhanes.py
generate_synthetic_data.py

The workflow for generating synthetic dataset:
1. Data cleaning
2. Feature selection
3. Data harmonization
4. Integration of EHR and lifestyle variables
5. Statistical analysis of feature distributions
6. Synthetic patient record generation
7. Validation of generated data

## Synthetic EHR-Lifestyle Dataset
File Name: ehr_n_lifestyle.csv

## Dataset Statistics

Records: 10,000

Features: 22

Format: CSV

Encoding: UTF-8

Missing values: None

License: CC BY 4.0

## Intended Applications

• Disease prediction

• Clinical decision support

• Machine learning

• Deep learning

• Biomedical engineering

• Explainable AI

• Feature selection

• Healthcare analytics
