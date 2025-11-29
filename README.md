# 🎓 AI College Recommender System

An AI-powered system that predicts the most suitable engineering college for students based on real MHT-CET & JEE admission data.  
Built for students in Maharashtra, especially around the **Amravati & Shegaon region**.

---

## 💡 About the Project

The **AI College Recommender** uses Machine Learning to help students find the best-fit college without checking hundreds of cutoff lists.

Students simply enter:
- 🎯 Their Percentile (JEE/MHT-CET)
- 🏫 Preferred Branch (CS/IT/Mechanical/etc.)
- 📍 Preferred City

The system predicts:
- Best matching college  
- Match confidence (%)  
- Alternative college options  

---

## 🚀 Key Features

### 👨‍🎓 For Students
- ⚡ **Instant predictions** using a trained ML model  
- 🧠 **Accurate recommendations** with confidence score  
- 🎛️ **Smart filtering**: Branch & City  
- 🏫 **Alternative suggestions** if top college is tough to get  

### 👨‍🏫 For Mentors
- 👥 Access to student data (Sign-up details)
- 📈 Insights & trends (coming soon)

### 🖥️ UI & Security
- 🔑 Role-based login (Student / Mentor)
- 🌙 Clean & modern dark-themed UI using Streamlit

---

## 🧠 How It Works

### 1️⃣ Data Understanding  
The system uses real admission merit list data (CSV files) and learns:
- Percentile → college mapping  
- Branch demand  
- City-wise seat patterns  

### 2️⃣ Machine Learning Model  
- Algorithm: **Random Forest Classifier**  
- Input fields (City, Branch) are **Label Encoded**  
- Output fields:
  - Predicted College  
  - Probability/Confidence  

### 3️⃣ Prediction Flow  
1. User enters percentile, branch, and city  
2. Data is encoded  
3. Model predicts the most suitable college  
4. Alternative options are shown as backup choices  

---

## 🛠️ Tech Stack

| Category | Technology |
|----------|------------|
| Frontend | Streamlit |
| Backend | Python |
| Machine Learning | Scikit-Learn (Random Forest) |
| Data Processing | Pandas, NumPy |
| Storage | CSV, Pickle (.pkl model) |

---


