import streamlit as st
import pandas as pd
import os
import pickle
import numpy as np
import time
from database import COLLEGE_DB

# ========================= 1. PAGE CONFIGURATION =========================
st.set_page_config(
    page_title="NexGen Admission AI", 
    page_icon="", 
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ========================= 2. VIBRANT COLORFUL CSS =========================
st.markdown("""
    <style>
    /* IMPORT FONTS */
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;500;700;900&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Outfit', sans-serif;
    }

    /* ANIMATED GRADIENT BACKGROUND */
    [data-testid="stAppViewContainer"] {
        background: linear-gradient(-45deg, #ee7752, #e73c7e, #23a6d5, #23d5ab);
        background-size: 400% 400%;
        animation: gradient 15s ease infinite;
        color: white;
    }

    @keyframes gradient {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    /* NEON GLASS CARDS */
    .glass-card {
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(10px);
        -webkit-backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.2);
        border-radius: 20px;
        padding: 25px;
        margin-bottom: 20px;
        box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    
    .glass-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 15px 45px rgba(0, 0, 0, 0.2);
        border: 1px solid rgba(255, 255, 255, 0.5);
    }

    /* COLORFUL HEADINGS */
    .hero-title {
        font-size: 4rem;
        font-weight: 900;
        background: linear-gradient(to right, #ffffff, #ffe259);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin-bottom: 10px;
        text-shadow: 0 4px 15px rgba(0,0,0,0.2);
    }
    
    .section-title {
        font-size: 1.8rem;
        font-weight: 700;
        color: white;
        margin-bottom: 15px;
        border-left: 5px solid #ffe259;
        padding-left: 15px;
    }

    /* VISIT WEBSITE BUTTON */
    .visit-btn {
        display: block;
        width: 100%;
        text-align: center;
        background: linear-gradient(45deg, #FF512F 0%, #DD2476 100%);
        color: white !important;
        text-decoration: none;
        padding: 10px 0;
        border-radius: 12px;
        font-weight: bold;
        margin-top: 15px;
        box-shadow: 0 4px 15px rgba(221, 36, 118, 0.4);
        transition: all 0.3s ease;
    }
    .visit-btn:hover {
        transform: scale(1.02);
        box-shadow: 0 6px 20px rgba(221, 36, 118, 0.6);
    }

    /* INPUT FIELDS STYLING */
    .stTextInput>div>div>input, .stNumberInput>div>div>input, .stSelectbox>div>div>div {
        background-color: rgba(0, 0, 0, 0.3) !important;
        color: white !important;
        border-radius: 12px;
        border: 1px solid rgba(255,255,255,0.1);
    }

    /* MAIN BUTTONS */
    div.stButton > button {
        background: linear-gradient(45deg, #1FA2FF 0%, #12D8FA 50%, #A6FFCB 100%);
        color: #0f2027;
        font-weight: 900;
        border: none;
        border-radius: 30px;
        height: 55px;
        font-size: 18px;
        transition: all 0.3s ease;
        box-shadow: 0 5px 15px rgba(18, 216, 250, 0.4);
    }
    div.stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(18, 216, 250, 0.6);
    }

    /* GOLD CARD (NK ORCHID) */
    .gold-card {
        background: radial-gradient(circle, rgba(255,215,0,0.2) 0%, rgba(0,0,0,0.4) 100%);
        border: 2px solid #FFD700;
        border-radius: 20px;
        padding: 30px;
        text-align: center;
        box-shadow: 0 0 30px rgba(255, 215, 0, 0.3);
        animation: glow 2s infinite alternate;
    }
    
    @keyframes glow {
        from { box-shadow: 0 0 20px rgba(255, 215, 0, 0.2); }
        to { box-shadow: 0 0 40px rgba(255, 215, 0, 0.6); }
    }
    </style>
""", unsafe_allow_html=True)

# ========================= 3. SETUP =========================
DATA_PATH = "data"
MODEL_FILE = "regional_model.pkl"
STUDENT_FILE = os.path.join(DATA_PATH, "students.csv")
MENTOR_FILE = os.path.join(DATA_PATH, "mentors.csv")
os.makedirs(DATA_PATH, exist_ok=True)

if not os.path.exists(STUDENT_FILE):
    pd.DataFrame(columns=["Name","Email","Password","MHT_CET","JEE_Main","Category","Gender"]).to_csv(STUDENT_FILE, index=False)

@st.cache_resource
def load_model():
    try:
        with open(MODEL_FILE, "rb") as f: return pickle.load(f)
    except: return None

def save_data(file_path, data):
    df = pd.read_csv(file_path)
    df = pd.concat([df, pd.DataFrame([data])], ignore_index=True)
    df.to_csv(file_path, index=False)

def get_effective_score(cet, jee, category, gender):
    score = (cet * 0.7) + (jee * 0.3)
    if category in ['SC', 'ST']: score += 7
    elif category == 'OBC': score += 3
    if gender == 'Female': score += 2
    return score

# ========================= 4. APP LOGIC =========================
if "user" not in st.session_state: st.session_state.user = None

# --- HEADER ---
st.markdown("<h1 class='hero-title'>🚀 NexGen Admission AI</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 1.2rem; margin-bottom: 40px;'>Discover Your Dream College with AI Precision</p>", unsafe_allow_html=True)

# --- DASHBOARD (LOGGED IN) ---
if st.session_state.user:
    user = st.session_state.user
    
    with st.sidebar:
        st.write("")
        st.markdown(f"<h2 style='text-align:center'>👤 {user['Name']}</h2>", unsafe_allow_html=True)
        if st.button("🚪 Logout"):
            st.session_state.user = None
            st.rerun()

    # INPUT CARD
    st.markdown("<div class='glass-card'><h3 class='section-title'>📊 Your Academic Profile</h3>", unsafe_allow_html=True)
    
    c1, c2 = st.columns(2)
    with c1: cet = st.number_input("MHT-CET Score", 0.0, 100.0, float(user.get("MHT_CET", 80.0)))
    with c2: jee = st.number_input("JEE Main Score", 0.0, 100.0, float(user.get("JEE_Main", 70.0)))
    
    c3, c4, c5 = st.columns(3)
    with c3: cat = st.selectbox("Category", ["OPEN", "OBC", "SC", "ST", "EWS"], index=["OPEN", "OBC", "SC", "ST", "EWS"].index(user.get("Category", "OPEN")))
    with c4: gen = st.selectbox("Gender", ["Male", "Female"], index=["Male", "Female"].index(user.get("Gender", "Male")))
    with c5: loc_pref = st.selectbox("📍 Location Preference", ["All Regions", "Pune", "Mumbai", "Solapur", "Nagpur", "Sangli"])
    
    st.markdown("</div>", unsafe_allow_html=True)

    # PREDICT BUTTON
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("✨ FIND MY COLLEGES ✨", use_container_width=True):
            with st.spinner("🔮 Consultng AI Oracle..."):
                time.sleep(1.2)
                
                effective_score = get_effective_score(cet, jee, cat, gen)
                engineering_db = COLLEGE_DB.get("Engineering", {})
                safe_colleges = []

                # LOGIC
                for name, info in engineering_db.items():
                    if "Women" in name and gen == "Male": continue
                    if loc_pref != "All Regions" and info['City'] != loc_pref: continue
                    if "Orchid" in name: continue # Handle fallback separately

                    branches = []
                    for br, cut in info['Cutoffs'].items():
                        if effective_score >= (cut - 2):
                            status = "High Chance" if effective_score >= cut else "Possible"
                            branches.append((br, status))
                    
                    if branches:
                        safe_colleges.append((name, branches, info['Website'], info['City']))

                # RESULTS
                if safe_colleges:
                    st.markdown(f"<h3 class='section-title'>🎉 Top Matches in {loc_pref}</h3>", unsafe_allow_html=True)
                    
                    # Create a Grid
                    cols = st.columns(2)
                    for i, (name, branches, url, city) in enumerate(safe_colleges):
                        branch_txt = " | ".join([b[0] for b in branches[:3]])
                        if len(branches) > 3: branch_txt += "..."
                        
                        with cols[i % 2]:
                            st.markdown(f"""
                            <div class='glass-card' style='min-height: 200px; display:flex; flex-direction:column; justify-content:space-between;'>
                                <div>
                                    <div style='display:flex; justify-content:space-between;'>
                                        <h3 style='margin:0; color: #fff;'>{name}</h3>
                                        <span style='background:rgba(255,255,255,0.2); padding:2px 8px; border-radius:5px; font-size:12px;'>{city}</span>
                                    </div>
                                    <p style='color:#ddd; margin-top:10px;'><b>Qualifying Branches:</b><br>{branch_txt}</p>
                                </div>
                                <a href='{url}' target='_blank' class='visit-btn'>Visit Official Website ↗</a>
                            </div>
                            """, unsafe_allow_html=True)
                
                else:
                    # FALLBACK (NK ORCHID)
                    st.markdown("<br>", unsafe_allow_html=True)
                    orchid = engineering_db.get('N.K. Orchid College Solapur', {})
                    url = orchid.get('Website', '#')
                    
                    st.markdown(f"""
                    <div class='gold-card'>
                        <h1 style='color:#FFD700; margin-bottom:5px;'>🌟 GEM RECOMMENDATION 🌟</h1>
                        <h2 style='color:white; margin-top:0;'>N.K. Orchid College of Engineering, Solapur</h2>
                        <p style='font-size: 1.1rem; color: #eee;'>
                            We found no matches in your filtered list, but your profile is a 
                            <b>PERFECT MATCH</b> for this premier institute.
                        </p>
                        <hr style='border-color:#FFD700; opacity:0.5;'>
                        <div style='display:flex; justify-content:center; gap: 20px; flex-wrap:wrap;'>
                            <span style='background:#FFD700; color:black; padding:5px 15px; border-radius:20px; font-weight:bold;'>Computer Science</span>
                            <span style='background:#FFD700; color:black; padding:5px 15px; border-radius:20px; font-weight:bold;'>Civil Engg</span>
                            <span style='background:#FFD700; color:black; padding:5px 15px; border-radius:20px; font-weight:bold;'>E & TC</span>
                        </div>
                        <br>
                        <a href='{url}' target='_blank' 
                           style='background:white; color:black; padding:12px 30px; border-radius:30px; text-decoration:none; font-weight:900; display:inline-block; margin-top:10px; box-shadow: 0 0 20px rgba(255,255,255,0.5);'>
                           APPLY NOW 🚀
                        </a>
                    </div>
                    """, unsafe_allow_html=True)

# --- LOGIN SCREEN (LOGGED OUT) ---
else:
    c1, c2, c3 = st.columns([1, 1.5, 1])
    with c2:
        st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
        
        tab1, tab2 = st.tabs(["🔐 LOGIN", "📝 REGISTER"])
        
        with tab1:
            email = st.text_input("Email", key="l_email")
            password = st.text_input("Password", type="password", key="l_pass")
            if st.button("Enter Dashboard"):
                df = pd.read_csv(STUDENT_FILE)
                if not df.empty:
                    df["Email"] = df["Email"].astype(str).str.strip()
                    df["Password"] = df["Password"].astype(str).str.strip()
                    user = df[(df["Email"]==email) & (df["Password"]==password)]
                    if not user.empty:
                        st.session_state.user = user.iloc[0].to_dict()
                        st.rerun()
                    else: st.error("❌ Invalid Credentials")
                else: st.error("❌ No users found")

        with tab2:
            n_name = st.text_input("Full Name")
            n_email = st.text_input("Email", key="r_email")
            n_pass = st.text_input("Password", type="password", key="r_pass")
            col_a, col_b = st.columns(2)
            n_cet = col_a.number_input("MHT-CET", 0.0, 100.0)
            n_jee = col_b.number_input("JEE Main", 0.0, 100.0)
            
            if st.button("Create Profile"):
                save_data(STUDENT_FILE, {"Name":n_name, "Email":n_email, "Password":n_pass, "MHT_CET":n_cet, "JEE_Main":n_jee, "Category":"OPEN", "Gender":"Male"})
                st.success("✅ Registered! Please Login.")

        st.markdown("</div>", unsafe_allow_html=True)