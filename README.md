# Automated Mound Recognition in the State of Indiana

## Overview
This project implements an advanced geospatial and machine learning pipeline to detect archaeological mounds from **Digital Terrain Model (DTM)** data. By integrating **YOLOv5** and **Generative Adversarial Networks (GANs)**, the system achieves precise mound identification with a **Precision score of 0.573** and delivers robust performance in complex terrain scenarios.

## Key Features
- **YOLOv5 for Object Detection**:
  - Fine-tuned **YOLOv5** using transfer learning to identify mounds from preprocessed **DTM data**.
  - Employed domain-specific annotations to enhance detection accuracy and performance.

- **Geospatial Preprocessing**:
  - Leveraged tools like **QGIS** for terrain preprocessing, contour generation, and feature extraction from geospatial datasets.

- **Synthetic Data Augmentation**:
  - Generated 480 high-quality synthetic samples using **Generative Adversarial Networks (GANs)** to address data scarcity and improve training efficacy.

- **Performance Optimization**:
  - Applied **Data Augmentation** techniques, including rotation, scaling, and noise addition, to improve model robustness.
  - Evaluated model performance using precision, recall, and F1-score metrics.

## Technologies Used
- **Machine Learning 
Frameworks**:
  - **YOLOv5**: For object detection and model training.
  - **PyTorch**: Backend framework for model customization and training.
- **Geospatial Tools**:
  - **QGIS**: For DTM preprocessing and geospatial feature extraction.
- **Synthetic Data Generation**:
  - **GANs**: For creating realistic synthetic samples to enhance dataset diversity.
- **Data Processing**:
  - **Pandas** and **NumPy**: For data manipulation and preprocessing.

## Workflow
1. **Data Preparation**:
   - Imported and preprocessed **Digital Terrain Models (DTMs)** using **QGIS**.
   - Annotated mounds in the dataset to create domain-specific labels.

2. **Synthetic Data Augmentation**:
   - Applied **GANs** to generate 480 synthetic images, addressing data imbalance.
   - Augmented training data using techniques like flipping, rotation, and scaling.

3. **Model Training**:
   - Fine-tuned **YOLOv5** using transfer learning on the augmented dataset.
   - Evaluated the model iteratively, refining hyperparameters for optimal performance.

4. **Validation and Testing**:
   - Assessed model performance using **Precision (0.573)** and other key metrics.
   - Validated results on independent DTM datasets to ensure generalization.

## Performance Metrics
- **Precision**: 0.573
- **Training Dataset Size**: Augmented to include 480 synthetic images.
- **Generalization**: Validated on diverse DTM datasets with promising results.
