import streamlit as st
import random
import time

# ১. পেজ সেটিংস ও থিম (Modern Look)
st.set_page_config(page_title="Global Retail AI", layout="wide", initial_sidebar_state="collapsed")

# ২. প্রিমিয়াম ক্যানভা-স্টাইল সিএসএস
st.markdown("""
<style>
    /* মেইন ব্যাকগ্রাউন্ড */
    .stApp { background-color: #f9f9fb; }
    
    /* ক্যানভা স্টাইল ব্যানার */
    .hero-section {
        background: linear-gradient(135deg, #6e8efb, #a777e3);
        padding: 80px 40px;
        border-radius: 30px;
        color: white;
        text-align: center;
        margin-bottom: 40px;
        box-shadow: 0 10px 30px rgba(110, 142, 251, 0.3);
    }
    
    /* কার্ড ডিজাইন */
    .feature-card {
        background: white;
        padding: 30px;
        border-radius: 24px;
        border: none;
        box-shadow: 0 10px 20px rgba(0,0,0,0.05);
        text-align: center;
        transition: 0.3s;
    }
    .feature-card:hover { transform: translateY(-10px); box-shadow: 0 20px 40px rgba(0,0,0,0.1); }
    
    /* বাটন ডিজাইন */
    .stButton>button {
        background: #6e8efb;
        color: white;
        border-radius: 12px;
        padding: 10px 24px;
        border: none;
    }
</style>
""", unsafe_allow_html=True)

# ৩. টপ নেভিগেশন (লোগো)
col_l, col_r = st.columns([1, 4])
with col_l:
    st.markdown("### 💠 AI DEALS") # এখানে আপনার লোগোর নাম

# ৪. হিরো ব্যানার (ক্যানভা স্টাইল)
st.markdown("""
<div class="hero-section">
    <h1 style="font-size: 50px; font-weight: 800;">From Everyday to Extraordinary</h1>
    <p style="font-size: 20px; opacity: 0.9;">AI-Driven Premium Liquidation Engine for Professionals.</p>
</div>
""", unsafe_allow_html=True)

# ৫. সার্চ ইঞ্জিন
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    query = st.text_input("", placeholder="Search for iPhone, Rolex, or Laptops...", label_visibility="collapsed")

if query:
    with st.spinner('Accessing Global Databases...'):
        time.sleep(1)
    
    st.markdown(f"### Analysis Report: {query}")
    
    # ৩টি কন্ডিশন কার্ড
    c1, c2, c3 = st.columns(3)
    base = random.randint(600, 1500)
    
    with c1:
        st.markdown(f"""<div class="feature-card">
            <h4 style="color:#6e8efb;">GRADE 1</h4>
            <p style="color:#888;">Condition: Pristine</p>
            <h2 style="color:#333;">${base}</h2>
            <p style="color:green; font-weight:bold;">Risk: 0.5%</p>
        </div>""", unsafe_allow_html=True)
        st.button("Secure Deal", key="b1", use_container_width=True)

    with c2:
        st.markdown(f"""<div class="feature-card" style="border: 2px solid #6e8efb;">
            <h4 style="color:#6e8efb;">GRADE 2</h4>
            <p style="color:#888;">Condition: Verified Refurb</p>
            <h2 style="color:#333;">${int(base*0.7)}</h2>
            <p style="color:orange; font-weight:bold;">Risk: 12%</p>
        </div>""", unsafe_allow_html=True)
        st.button("Secure Deal", key="b2", use_container_width=True)

    with c3:
        st.markdown(f"""<div class="feature-card">
            <h4 style="color:#6e8efb;">GRADE 3</h4>
            <p style="color:#888;">Condition: Open Stock</p>
            <h2 style="color:#333;">${int(base*0.4)}</h2>
            <p style="color:red; font-weight:bold;">Risk: 38%</p>
        </div>""", unsafe_allow_html=True)
        st.button("Secure Deal", key="b3", use_container_width=True)

# ৬. সাইডবার চ্যাটবট (স্মার্ট ফিচার)
with st.sidebar:
    st.markdown("### 💬 AI Assistant")
    st.write("Hello! I can help you find the best liquidation risks.")
    st.text_input("Ask me something...")
    st.divider()
    st.markdown("### 📊 Market Status")
    st.success("Global servers online")

# ৭. ফুটার
st.markdown("<br><hr><center>© 2026 Global Retail AI | Powered by Gemini</center>", unsafe_allow_html=True)
