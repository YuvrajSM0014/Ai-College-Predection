# 🎓 AI College Recommender System

Empowering students with AI-driven engineering college predictions based on real admission data.

---

## 📖 Table of Contents
- [About the Project](#-about-the-project)
- [Key Features](#-key-features)
- [How It Works](#-how-it-works)
- [Tech Stack](#-tech-stack)
- [Installation & Setup](#-installation--setup)
- [Usage Guide](#-usage-guide)
- [Project Structure](#-project-structure)
- [Future Roadmap](#-future-roadmap)
- [Contributing](#-contributing)

---

## 💡 About the Project

The **AI College Recommender** is a machine learning–powered web application designed to help engineering aspirants in Maharashtra (especially the **Amravati/Shegaon region**) find their best-fit colleges.

Instead of checking hundreds of cutoff lists manually, students simply enter their:
- 🎯 JEE/MHT-CET Percentile  
- 🏫 Preferred Branch  
- 📍 City  

The system uses a **Random Forest Classifier** trained on real historical merit data to predict the most likely college admission.

---

## 🚀 Key Features

### 👨‍🎓 For Students
- ⚡ **Instant Predictions:** Get college suggestions based on your percentile.
- 🎛️ **Smart Filters:** Choose Branch (CS/IT/Mech/etc.) and City.
- 📊 **Confidence Score:** Shows AI "Match Confidence" for every prediction.
- 🔁 **Alternative Options:** Suggests the next best colleges automatically.

### 👨‍🏫 For Mentors
- 📈 **Dashboard Access:** Track trends (coming soon).
- 👥 **Student Insights:** View registered student preferences and data.

### 🔐 Security & UI
- 🔑 **Role-Based Login:** Separate logins for Students and Mentors.
- 🖥️ **Modern UI:** Clean, dark-themed interface built with Streamlit.

---

## 🧠 How It Works

### 1️⃣ Data Extraction
Real admission merit lists (CSV) are parsed to understand:
- Percentile → College mapping  
- City-wise trends  
- Branch popularity  

### 2️⃣ Model Training (`setup_model.py`)
- Algorithm: **Random Forest Classifier**
- Text fields (City, Course) → **Label Encoding**
- Model captures patterns like:  
  _“Students with 85+ percentile usually get IT in Shegaon.”_

### 3️⃣ Prediction (`app.py`)
- User enters percentile, branch, and city.
- Inputs are encoded and sent to the trained model (`regional_model.pkl`).
- Model predicts college + probability score.

---

## 🛠️ Tech Stack

| Component | Technology | Description |
|----------|------------|-------------|
| Frontend | Streamlit | Fast, interactive UI |
| Backend | Python | Core logic |
| Machine Learning | Scikit-Learn | Random Forest Classifier |
| Data Processing | Pandas, NumPy | CSV handling and arrays |
| Storage | Pickle, CSV | Model + user data storage |

---

## ⚙️ Installation & Setup

Follow these steps to run the project locally.

### 1️⃣ Clone the Repository
bash


2️⃣ Install Dependencies
pip install -r requirements.txt

3️⃣ Initialize the AI Model (Important)

This creates the trained model file (regional_model.pkl):

python setup_model.py


You should see:

🎉 SUCCESS! 'regional_model.pkl' created.

4️⃣ Run the Application
streamlit run app.py

📱 Usage Guide

Sign Up
Create a Student account from the Sign-Up tab.

Login
Use your credentials to access the dashboard.

Predict Your College

Enter your JEE/MHT-CET percentile (e.g., 85.5)

Choose branch (e.g., IT)

Choose city (e.g., Shegaon)

Click Analyze

View Results

Top predicted college

Match confidence

Alternative recommendations

📂 Project Structure
ai_college_recommender/
├── data/                   # Stores user CSVs (students.csv, mentors.csv)
├── app.py                  # Main Streamlit application
├── setup_model.py          # Script to train the ML model
├── regional_model.pkl      # Trained ML model (generated)
├── requirements.txt        # Dependencies
└── README.md               # Project documentation

🔮 Future Roadmap

 Add all colleges across Maharashtra (Pune/Mumbai/Nagpur).

 Include category-wise logic (OBC/SC/ST).

 Add cutoff trend visualizations (last 5 years).

 Deploy to Streamlit Cloud / AWS.

 Create advanced mentor dashboards.


