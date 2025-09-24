# kidney-Diseases-Prediction-By-Using-ML
# Kidney Disease Prediction 🩺

This project predicts **Chronic Kidney Disease (CKD)** using **Machine Learning models**.  
CKD is a silent killer that affects millions worldwide, often undiagnosed until late stages.  
Our goal is to use patient health data and ML models for **early detection**, which can help doctors and patients with faster treatment decisions.

## ✨ Features
- Uses patient **clinical, demographic, and biochemical attributes**.  
- Predicts whether a person is likely to have CKD.  
- Multiple ML models tested: Logistic Regression, Decision Tree, Random Forest, SVM, KNN, ANN.  
- **Random Forest** achieved the best accuracy (~98%).  
- Easy-to-understand models like Logistic Regression & Decision Tree also included for practical use.  

## 🔄 Workflow
1. **Data Collection** – Patient health dataset (lab results, demographics).  
2. **Data Preprocessing** – Handle missing values, normalize features, remove outliers.  
3. **Feature Selection** – Identify the most important clinical parameters.  
4. **Model Training** – Train models (LR, DT, RF, SVM, KNN, ANN).  
5. **Evaluation** – Compare accuracy, precision, recall, and F1-score.  
6. **Deployment** – Simple application for end-users.  

## 📊 Results
- Logistic Regression → 94%  
- Decision Tree → 95%  
- Random Forest → 98% ✅ (Best)  
- SVM → 96%  
- ANN → 97%  
- KNN → 93%  

Random Forest performed best, but Decision Tree and Logistic Regression are more interpretable for doctors.  

## 🚀 Future Scope
- Use **Deep Learning models (CNN, RNN)** for better accuracy.  
- Deploy as a **web or mobile app**.  
- Integrate with **IoT health devices** for real-time monitoring.  

## 🛠️ Tech Stack
- **Python**  
- **Pandas, NumPy** – Data preprocessing  
- **Scikit-learn** – Model training & evaluation  
- **Matplotlib / Seaborn** – Visualization  
- (Future) TensorFlow / PyTorch for deep learning
- 
## 📂 Project Structure
kidney-disease-prediction/
│-- data/ # Dataset files
│-- models/ # Trained ML models
│-- notebooks/ # Jupyter notebooks for training & testing
│-- app.py # Deployment script (Streamlit/Flask)
│-- requirements.txt # Dependencies
│-- README.md # Project documentation
