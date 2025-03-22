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



## HOW TO USE THE APP LOCALLY:
streamlit run app.py
2️⃣ Enter patient details (Age, Glucose Level, BMI, etc.).
3️⃣ Click "Predict" to see stroke risk probability.


## KEY FINDINGS
* Higher age and high glucose levels significantly increase stroke risk.

* Hypertension and heart disease are critical risk factors.

* Random Forest model achieved 92% accuracy.

* Feature Engineering (One-Hot Encoding, Age Binning) improved model performance.

* People who never smoked had a lower risk of stroke.

* Men had a slightly higher stroke risk than women in this dataset.



## 📊 Model Performance & Comparison
Several machine learning models were tested, with the following results:

Model	Accuracy
Random Forest	- 92%
Gradient Boosting	- 89%
Logistic Regression -	85%
Support Vector Machine (SVM) - 82%
Decision Tree	- 78%



##  🤝 Contributing
If you’d like to contribute to this project, follow these steps:

* Fork the repository

1. Create a feature branch (git checkout -b feature-name)

2. Commit your changes (git commit -m "Added new feature")

3. Push to GitHub (git push origin feature-name)

4. Open a Pull Request




## 🎯 Future Improvements
✅ Improve UI/UX for the Streamlit app

✅ Add deep learning models (e.g., Neural Networks)

✅ Perform hyperparameter tuning for better accuracy

✅ Deploy the app on multiple cloud platforms


## LICENSE
This project is licensed under the MIT License.
