# 🛠 AI-Based Casting Product Defect Detection System

An end-to-end Machine Learning project for detecting **manufacturing defects in casting products** using the [Real-Life Industrial Dataset of Casting Products](https://www.kaggle.com/datasets/ravirajsinh45/real-life-industrial-dataset-of-casting-product).

The system consists of:

1. **Model Training** (Jupyter Notebook) — trains a CNN model to classify casting products as **Defective** or **OK**.
2. **Web App** (Streamlit) — allows users to upload product images and get defect detection results instantly.

---

## 📂 Project Structure

## 📦 defect-detection
``` 
├── 📄 defect_detection_training.ipynb # Jupyter Notebook for model training
├── 📄 app.py # Streamlit app for image inference
│ └── README.txt # Dataset info
├── 📁 models/ # Saved trained model(s)
│ └── defect_model.h5 # Example saved model (can't save now due to large data will update later)
├── 📄 requirements.txt # Dependencies
└── 📄 README.md # Project documentation
```
---

## ⚙️ Requirements

Install dependencies with:
```

pip install -r requirements.txt
```


## 📊 Dataset

We are using the Real-Life Industrial Dataset of Casting Products from Kaggle.

It contains grayscale images of casting products in two categories:

Defective — Products with visible manufacturing defects.

OK — Products without defects (labeled as ok_front in the dataset).

Dataset structure:
```
casting_data/
├── train/
│   ├── defective/
│   └── ok_front/
└── test/
    ├── defective/
    └── ok_front/
```
## 🧠 Model Training (Jupyter Notebook)

Open defect_detection_training.ipynb and run all cells to:

Load and preprocess dataset (resize, normalize)

Train CNN model for binary classification

Evaluate model performance on test data

Save trained model to models/

Replace in notebook:
``` 

model.save("models/defect_model.h5")
``` 

## 🌐 Running the Streamlit App

Run the app with:
``` 

streamlit run app.py
``` 


Key Features:

Upload product image for analysis

Model predicts Defective or OK

Displays prediction confidence score

## 📜 License

This project is for educational and research purposes only. Dataset belongs to the original author on Kaggle.

## ✍️ Author

**Divyansh Kashyap**  
_BTech AIML | Machine Learning Intern | Open to Collaborations_  
📧 [LinkedIn](https://www.linkedin.com/in/divyansh-kashyap-231270301/)
