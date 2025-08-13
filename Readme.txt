Real-Life Industrial Dataset of Casting Products
================================================

This dataset contains grayscale images of casting products for binary classification:
    1. defective  - Products with visible manufacturing defects
    2. ok_front   - Products without defects

Directory Structure:
--------------------
casting_data/
    train/
        defective/      --> Training images with defects
        ok_front/       --> Training images without defects
    test/
        defective/      --> Testing images with defects
        ok_front/       --> Testing images without defects

Image Details:
--------------
- Format: PNG
- Color: Grayscale
- Resolution: 300x300 pixels
- Cropped and aligned for consistency

Usage:
------
- 'train' folder: Use for training machine learning models
- 'test' folder: Use for evaluating trained models

Source:
-------
Kaggle Dataset:
https://www.kaggle.com/datasets/ravirajsinh45/real-life-industrial-dataset-of-casting-product
