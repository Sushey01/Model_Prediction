# Stroke Prediction Analysis 🚑  

## 📌 Overview  
This project analyzes stroke risk factors using **machine learning** on the [Stroke Prediction Dataset](https://www.kaggle.com/fedesoriano/stroke-prediction-dataset).  
The model predicts whether a patient is at risk of **stroke** based on key health indicators.  

## 📊 Dataset  
The dataset contains **11 features**, including:  
- `age`, `hypertension`, `heart_disease`, `avg_glucose_level`  
- `bmi`, `smoking_status`, `gender`, `work_type`, etc.  

### 📌 **Data Preprocessing**  
- **Missing Values**: Handled using mean/mode imputation.  
- **Feature Engineering**: Categorical variables encoded.  
- **Outlier Detection**: Extreme values handled using the IQR method.  

📄 **[Full Report](https://github.com/Sushey01/Model_Prediction/blob/main/StrokePredictionAnalysis_Report.pdf)**  
_For a detailed understanding of the analysis process, please refer to the report._  

---

## 🌍 **Live Demo**  
The app is deployed using **Streamlit**. Try it here:  
👉 [Stroke Prediction Web App](https://nqminbjjvmu5weffkztdak.streamlit.app/)  

---

## 🚀 **Installation & Setup**  
Clone the repository and install dependencies:  
```bash
git clone https://github.com/Sushey01/Model_Prediction.git  
cd Model_Prediction  
pip install -r requirements.txt  
