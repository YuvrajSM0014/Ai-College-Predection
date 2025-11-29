import streamlit as st
import pandas as pd
import os
import pickle
import numpy as np
import time

# ========================= PAGE CONFIG =========================
st.set_page_config(page_title="AI College Recommender", page_icon="🎓", layout="wide")

# ========================= CSS STYLING =========================
st.markdown("""
    <style>
    /* Main Background */
    [data-testid="stAppViewContainer"] {
        background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
        color: white;
    }
    
    /* Title Styling */
    .title {
        text-align: center;
        color: #00d2ff;
        font-size: 48px;
        font-weight: 800;
        margin-top: 10px;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
    }
    
    .subtitle {
        text-align: center;
        color: #e0e0e0;
        font-size: 18px;
        margin-bottom: 30px;
    }

    /* Card Container */
    .card {
        background-color: rgba(255,255,255,0.1);
        border-radius: 15px;
        padding: 25px;
        margin: 15px 0;
        box-shadow: 0 4px 15px rgba(0,0,0,0.3);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255,255,255,0.1);
    }

    /* College Result Card */
    .college-card {
        background: linear-gradient(to right, #ffffff, #f8f9fa);
        border-radius: 15px;
        padding: 25px;
        margin-top: 20px;
        box-shadow: 0 10px 25px rgba(0,0,0,0.2);
        color: #333;
        border-left: 8px solid #00d2ff;
        animation: fadeIn 1s;
    }
    
    @keyframes fadeIn {
        0% { opacity: 0; transform: translateY(20px); }
        100% { opacity: 1; transform: translateY(0); }
    }

    /* Buttons */
    div.stButton > button {
        background: linear-gradient(to right, #00d2ff, #3a7bd5);
        color: white;
        font-weight: bold;
        border-radius: 30px;
        height: 50px;
        width: 100%;
        border: none;
        transition: all 0.3s ease;
    }
    div.stButton > button:hover {
        transform: scale(1.02);
        box-shadow: 0 5px 15px rgba(0, 210, 255, 0.4);
    }
    </style>
""", unsafe_allow_html=True)

# ========================= FILE SETUP =========================
DATA_PATH = "data"
STUDENT_FILE = os.path.join(DATA_PATH, "students.csv")
MENTOR_FILE = os.path.join(DATA_PATH, "mentors.csv")
MODEL_FILE = "regional_model.pkl"

os.makedirs(DATA_PATH, exist_ok=True)

def ensure_csv(file_path, columns):
    if not os.path.exists(file_path):
        pd.DataFrame(columns=columns).to_csv(file_path, index=False)

ensure_csv(STUDENT_FILE, ["Name","Email","Password","MHT_CET","JEE_Main","Branch","Category","Gender"])
ensure_csv(MENTOR_FILE, ["Name","Email","Password","Current","Experience"])

# ========================= LOAD ML MODEL =========================
@st.cache_resource
def load_model():
    try:
        with open(MODEL_FILE, "rb") as f:
            data = pickle.load(f)
        return data
    except FileNotFoundError:
        return None
    except Exception as e:
        st.error(f"Error loading model: {e}")
        return None

model_data = load_model()

# ========================= UTIL FUNCTIONS =========================
def load_data(file_path):
    return pd.read_csv(file_path) if os.path.exists(file_path) else pd.DataFrame()

def save_data(file_path, new_entry):
    df = load_data(file_path)
    df = pd.concat([df, pd.DataFrame([new_entry])], ignore_index=True)
    df.to_csv(file_path, index=False)

def login_user(email, password, role):
    df = load_data(STUDENT_FILE if role == "Student" else MENTOR_FILE)
    if "Email" not in df.columns or "Password" not in df.columns:
        return None
    user = df[(df["Email"] == email) & (df["Password"] == password)]
    return user.iloc[0].to_dict() if not user.empty else None

# ========================= HEADER =========================
st.markdown("<h1 class='title'>🎓 AI College Predictor</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>Predicting Engineering Colleges in Maharashtra using Machine Learning</p>", unsafe_allow_html=True)

# ========================= SESSION STATE =========================
if "user" not in st.session_state:
    st.session_state.user = None
if "role" not in st.session_state:
    st.session_state.role = None
if "choice" not in st.session_state:
    st.session_state.choice = "🏠 Home"

# ========================= NAVIGATION LOGIC =========================

# 1. LOGGED IN NAVIGATION (Sidebar Only)
if st.session_state.user:
    with st.sidebar:
        st.image("https://cdn-icons-png.flaticon.com/512/4762/4762311.png", width=100)
        st.markdown(f"### 👋 Welcome, {st.session_state.user['Name']}")
        st.info(f"Role: {st.session_state.role}")
        
        st.markdown("---")
        if st.button("🚪 Logout", key="logout_btn"):
            st.session_state.user = None
            st.session_state.role = None
            st.session_state.choice = "🏠 Home"
            st.rerun()

# 2. PUBLIC NAVIGATION (Top Bar - Only visible if NOT logged in)
else:
    cols_nav = st.columns([1,1,1,1])
    with cols_nav[0]:
        if st.button("🏠 Home"): st.session_state.choice = "🏠 Home"
    with cols_nav[1]:
        if st.button("📝 Sign Up"): st.session_state.choice = "📝 Sign Up"
    with cols_nav[2]:
        if st.button("🔐 Login"): st.session_state.choice = "🔐 Login"
    with cols_nav[3]:
        if st.button("📊 Workflow"): st.session_state.choice = "📊 Workflow"

# ========================= MAIN CONTENT RENDERER =========================

# --- SCENARIO A: USER IS LOGGED IN ---
if st.session_state.user:
    user = st.session_state.user
    role = st.session_state.role

    # STUDENT DASHBOARD
    if role == "Student":
        st.markdown("<div class='card'><h3>🤖 Predict Your College</h3></div>", unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("#### 📊 Academic Scores")
            cet_score = st.number_input("MHT-CET Percentile", 0.0, 100.0, float(user.get("MHT_CET", 80.0)))
            jee_score = st.number_input("JEE Main Percentile", 0.0, 100.0, float(user.get("JEE_Main", 70.0)))
            
        with col2:
            st.markdown("#### 👤 Profile & Preferences")
            branch_ops = ["CS", "IT", "EnTC", "Mech", "Civil"]
            cat_ops = ["OPEN", "OBC", "SC", "ST", "EWS"]
            gender_ops = ["Male", "Female"]

            # Safe index lookup
            def get_idx(options, val):
                return options.index(val) if val in options else 0

            branch_input = st.selectbox("Preferred Branch", branch_ops, index=get_idx(branch_ops, user.get("Branch")))
            cat_input = st.selectbox("Category", cat_ops, index=get_idx(cat_ops, user.get("Category")))
            gender_input = st.selectbox("Gender", gender_ops, index=get_idx(gender_ops, user.get("Gender")))

        st.markdown("<br>", unsafe_allow_html=True)
        
        if st.button("🚀 Analyze & Predict"):
            with st.spinner("Thinking... Analysis in progress..."):
                time.sleep(1.5) # UX Delay

                # --- PREDICTION LOGIC START ---
                predicted_college = "Unknown"
                confidence = 0.0
                alternatives = []

                if model_data:
                    try:
                        # Real Model Prediction
                        model = model_data['model']
                        le_branch = model_data['le_branch']
                        le_cat = model_data['le_category']
                        le_gen = model_data['le_gender']
                        le_col = model_data['le_college']

                        b_enc = le_branch.transform([branch_input])[0]
                        c_enc = le_cat.transform([cat_input])[0]
                        g_enc = le_gen.transform([gender_input])[0]

                        features = np.array([[cet_score, jee_score, b_enc, c_enc, g_enc]])
                        
                        pred_idx = model.predict(features)[0]
                        predicted_college = le_col.inverse_transform([pred_idx])[0]
                        
                        probs = model.predict_proba(features)[0]
                        confidence = np.max(probs) * 100
                        
                        # Get Alternatives
                        sorted_indices = np.argsort(probs)[::-1]
                        for idx in sorted_indices[1:4]: # Top 3 alternatives
                            if probs[idx] > 0.0:
                                alternatives.append((le_col.inverse_transform([idx])[0], probs[idx] * 100))

                    except Exception as e:
                        st.error(f"Prediction Error: {e}")
                else:
                    # --- FALLBACK SIMULATION (If model is missing) ---
                    st.warning("⚠️ Model file not found. Using simulation mode.")
                    predicted_college = "COEP Technological University (Simulated)"
                    confidence = 88.5
                    alternatives = [("VJTI Mumbai", 10.2), ("PICT Pune", 1.3)]
                
                # --- DISPLAY RESULTS ---
                st.markdown(f"""
                    <div class='college-card'>
                        <h4 style='color:gray; margin:0;'>Top Recommendation</h4>
                        <h1 style='color: #00d2ff; margin:5px 0;'>🏛️ {predicted_college}</h1>
                        <p><b>Confidence Score:</b> {confidence:.2f}%</p>
                        <hr>
                        <div style='display:flex; justify-content:space-between;'>
                            <span>📚 Branch: <b>{branch_input}</b></span>
                            <span>🏷️ Category: <b>{cat_input}</b></span>
                        </div>
                    </div>
                """, unsafe_allow_html=True)

                if alternatives:
                    st.markdown("### 💡 Other Possible Options")
                    cols_alt = st.columns(3)
                    for i, (name, prob) in enumerate(alternatives):
                        with cols_alt[i % 3]:
                            st.info(f"**{name}**\n\nChance: {prob:.1f}%")

    # MENTOR DASHBOARD
    elif role == "Mentor":
        st.markdown("<div class='card'><h3>👨‍🏫 Mentor Dashboard</h3></div>", unsafe_allow_html=True)
        st.info("Analytics feature under development.")
        st.bar_chart({"CS": 40, "IT": 30, "EnTC": 20, "Mech": 10})

# --- SCENARIO B: USER IS NOT LOGGED IN (Public Pages) ---
else:
    choice = st.session_state.choice

    if choice == "🏠 Home":
        st.markdown("""
            <div class='card'>
            <h3>🚀 Welcome to the AI Admission Assistant</h3>
            <p>This system uses a <b>Random Forest Machine Learning Model</b> trained on Maharashtra Engineering Admission patterns.</p>
            <ul>
                <li>🎯 <b>Predicts</b> colleges based on MHT-CET & JEE Scores.</li>
                <li>🏢 <b>Covers</b> top colleges: COEP, VJTI, PICT, WIT Solapur, etc.</li>
                <li>🧠 <b>Learns</b> from category and gender-based cutoff trends.</li>
            </ul>
            </div>
        """, unsafe_allow_html=True)
        st.image("https://miro.medium.com/v2/resize:fit:1400/1*c_fiB-YgbnMl6nntYGBMHQ.jpeg", use_container_width=True)

    elif choice == "📝 Sign Up":
        st.markdown("<h3>📝 Create an Account</h3>", unsafe_allow_html=True)
        role_choice = st.radio("Select Role", ["Student", "Mentor"], horizontal=True)
        
        with st.form("signup_form"):
            name = st.text_input("Full Name")
            email = st.text_input("Email Address")
            password = st.text_input("Password", type="password")
            
            # Init vars to avoid scope errors
            cet, jee, branch, cat, gender = 0.0, 0.0, "CS", "OPEN", "Male"
            curr, exp = "", 0

            if role_choice == "Student":
                c1, c2 = st.columns(2)
                with c1:
                    cet = st.number_input("MHT-CET Score", 0.0, 100.0)
                    jee = st.number_input("JEE Main Score", 0.0, 100.0)
                with c2:
                    branch = st.selectbox("Preferred Branch", ["CS", "IT", "EnTC", "Mech", "Civil"])
                    cat = st.selectbox("Category", ["OPEN", "OBC", "SC", "ST", "EWS"])
                    gender = st.selectbox("Gender", ["Male", "Female"])
            else:
                curr = st.text_input("Current Organization")
                exp = st.number_input("Years of Experience", 0, 50)

            submit = st.form_submit_button("Register Now")
            
            if submit:
                if name and email and password:
                    if role_choice == "Student":
                        save_data(STUDENT_FILE, {
                            "Name": name, "Email": email, "Password": password,
                            "MHT_CET": cet, "JEE_Main": jee, "Branch": branch, 
                            "Category": cat, "Gender": gender
                        })
                    else:
                        save_data(MENTOR_FILE, {
                            "Name": name, "Email": email, "Password": password, 
                            "Current": curr, "Experience": exp
                        })
                    st.success("✅ Account created successfully! Please Login.")
                else:
                    st.warning("⚠️ Please fill all required fields.")

    elif choice == "🔐 Login":
        st.markdown("<h3>🔐 Access Your Dashboard</h3>", unsafe_allow_html=True)
        col_main, _ = st.columns([1,1])
        with col_main:
            role_login = st.selectbox("Login As", ["Student", "Mentor"])
            email_login = st.text_input("Email")
            pass_login = st.text_input("Password", type="password")
            
            if st.button("Secure Login"):
                user_data = login_user(email_login, pass_login, role_login)
                if user_data:
                    st.session_state.user = user_data
                    st.session_state.role = role_login
                    st.rerun()
                else:
                    st.error("❌ Invalid Credentials. Please try again.")
    
    elif choice == "📊 Workflow":
        st.markdown("### 🧠 How It Works")
        st.markdown("""
        1. **Data Collection**: We generated a synthetic dataset simulating student profiles.
        2. **Training**: A Random Forest Classifier learns the relationships.
        3. **Prediction**: The model suggests the best fit based on previous cutoff trends.
        """)
        st.code("""
        # Logic Flow
        User Input -> Encoders -> Random Forest Model -> Prediction -> Top College
        """, language="python")