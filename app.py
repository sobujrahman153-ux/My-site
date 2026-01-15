    import streamlit as st
import random
import time
import re
import requests
from bs4 import BeautifulSoup
import google.generativeai as genai

# --- ১. API কী লোড করা এবং হ্যাকিং প্রতিরোধ ---
# Streamlit Secrets থেকে API Key লোড করা (আপনার Secrets বক্সে এটি সেট করতে হবে)
try:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
    model = genai.GenerativeModel('gemini-pro')
except Exception as e:
    st.error("AI API Key not found. Please set `GEMINI_API_KEY` in Streamlit Secrets.")
    st.stop()

# ইনপুট স্যানিটাইজেশন (হ্যাকিং প্রতিরোধ)
def clean_input(text):
    if text:
        return re.sub(r'[<>/{}[\]\\^`|]', '', text)
    return ""

# --- ২. পেজ সেটিংস ও SEO ---
st.set_page_config(
    page_title="Global Retail Intelligence | AI Smart Shopper",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- ৩. অত্যাধুনিক CSS ডিজাইন (E-commerce Giant Look) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;700&display=swap');
    
    html, body, [class*="css"] { font-family: 'Roboto', sans-serif; }
    
    .stApp {
        background: #f0f2f5;
        color: #333;
    }

    /* নেভিগেশন বার */
    .header-bar {
        background: white;
        padding: 15px 5%;
        display: flex;
        justify-content: space-between;
        align-items: center;
        box-shadow: 0 2px 15px rgba(0,0,0,0.08);
        border-bottom: 1px solid #e0e0e0;
    }

    /* লোগো */
    .logo-text {
        font-size: 28px;
        font-weight: 700;
        color: #007bff;
        text-transform: uppercase;
        letter-spacing: 1px;
    }

    /* হিরো সেকশন */
    .hero {
        background: linear-gradient(rgba(0,0,0,0.6), rgba(0,0,0,0.8)), url("https://images.unsplash.com/photo-1517430489115-d242c75a967f?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1920&q=80");
        background-size: cover;
        background-position: center;
        padding: 120px 5%;
        text-align: center;
        color: white;
        border-radius: 0 0 50px 50px;
        margin-bottom: 50px;
    }
    .hero h1 { font-size: 68px; font-weight: 700; margin-bottom: 20px; }
    .hero p { font-size: 22px; max-width: 800px; margin: 0 auto; line-height: 1.5; }

    /* প্রোডাক্ট কার্ড */
    .product-card {
        background: white;
        border-radius: 18px;
        padding: 30px;
        box-shadow: 0 6px 20px rgba(0,0,0,0.06);
        border: 1px solid #e0e0e0;
        transition: all 0.3s ease;
        text-align: center;
    }
    .product-card:hover {
        transform: translateY(-8px);
        box-shadow: 0 12px 25px rgba(0,0,0,0.12);
    }
    .product-img {
        width: 100%;
        max-height: 200px;
        object-fit: contain;
        border-radius: 10px;
        margin-bottom: 20px;
    }
    .card-title { font-size: 24px; font-weight: 700; color: #333; margin-bottom: 10px; }
    .card-price { font-size: 38px; font-weight: 800; color: #007bff; margin-bottom: 15px; }
    .risk-label { font-size: 16px; font-weight: 600; margin-bottom: 15px; }
    .risk-low { color: #28a745; }
    .risk-medium { color: #ffc107; }
    .risk-high { color: #dc3545; }

    /* চ্যাটবট */
    .chat-box {
        background: #e9ecef;
        border-radius: 10px;
        padding: 15px;
        margin-top: 20px;
    }
    .chat-message {
        background: #d4edda;
        color: #155724;
        padding: 10px;
        border-radius: 8px;
        margin-bottom: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- ৪. নেভিগেশন বার (লোগো ও মেনু) ---
st.markdown("""
    <div class="header-bar">
        <div class="logo-text">AI DEALS</div>
        <div style="display:flex; gap:20px;">
            <a href="#" style="color:#333; text-decoration:none; font-weight:600;">Home</a>
            <a href="#" style="color:#333; text-decoration:none; font-weight:600;">About</a>
            <a href="#" style="color:#333; text-decoration:none; font-weight:600;">Contact</a>
            <a href="#" style="color:#333; text-decoration:none; font-weight:600;">Login</a>
        </div>
    </div>
    <div style="padding-top: 80px;"></div>
    """, unsafe_allow_html=True) # padding-top to account for fixed header

# --- ৫. হিরো সেকশন ও সার্চ বক্স ---
st.markdown("""
    <div class="hero">
        <h1>Unleash Smart Shopping.</h1>
        <p>Your personal AI assistant for finding the best liquidation deals across the globe.</p>
        <div style="margin-top: 40px; display: flex; justify-content: center;">
            <input type="text" id="main_search_input" placeholder="Search for iPhone 15 Pro, Gaming Laptop..." 
                   style="width: 60%; padding: 15px 20px; border-radius: 30px; border: none; font-size: 18px; box-shadow: 0 4px 15px rgba(0,0,0,0.2);">
        </div>
    </div>
    """, unsafe_allow_html=True)

# Streamlit-এর নিজস্ব সার্চ ইনপুট (যাতে কাজ করে)
search_query = st.text_input(" ", placeholder="Type your search here...", label_visibility="collapsed")
cleaned_query = clean_input(search_query)

# --- ৬. অতিরিক্ত ফিচার্স (সাইডবার) ---
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/6214/6214534.png", width=100)
    st.markdown("### ⚡ AI Smart Tools")
    st.button("🎁 Daily Deals", use_container_width=True)
    st.button("❤️ Wishlist", use_container_width=True)
    st.button("📊 Compare Products", use_container_width=True)
    st.button("📧 Newsletter", use_container_width=True)
    st.divider()
    st.markdown("### 💬 Live AI Chatbot")
    chat_input = st.text_input("Ask me anything!", key="chatbot_input")
    if chat_input:
        with st.spinner("AI is typing..."):
            try:
                response = model.generate_content(f"User query: {chat_input}. Act as a helpful e-commerce AI assistant. Keep responses concise.")
                st.markdown(f'<div class="chat-message">{response.text}</div>', unsafe_allow_html=True)
            except Exception as e:
                st.error("AI chatbot is busy. Please try again later.")

# --- ৭. প্রোডাক্ট রেজাল্ট ও ডেটা অ্যানালাইসিস ---
if cleaned_query:
    st.markdown(f"<h2 style='text-align: center; margin-bottom: 40px;'>AI-Verified Deals for '{cleaned_query}'</h2>", unsafe_allow_html=True)
    
    # এআই থেকে রিয়ালিস্টিক ডাটা আনার চেষ্টা
    try:
        # Gemini-কে দিয়ে ডামি ডাটা জেনারেট করাচ্ছি
        ai_data_prompt = f"""Generate a JSON object for a product '{cleaned_query}' with 3 conditions:
        1. "Grade A++": New/Open Box. Estimate a high price, low risk (e.g., 2%), and a premium image URL (e.g., from Unsplash, Pexels).
        2. "Grade A": Certified Refurbished. Estimate a 30% lower price than A++, medium risk (e.g., 15%), and a relevant image URL.
        3. "Grade B/C": Liquidation/Used. Estimate a 60% lower price than A++, high risk (e.g., 40%), and a relevant image URL.
        Include brief descriptions for each. Ensure image URLs are valid.
        Example image URL format: "https://images.unsplash.com/photo-1517336714730-4965858004e0?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=800&q=80"
        """
        
        # এখানে এপিআই কল হচ্ছে। যদি Secrets বসানো থাকে, তবে কাজ করবে।
        response_data = model.generate_content(ai_data_prompt)
        # JSON পার্স করার আগে কোড ব্লক রিমুভ করা
        json_string = response_data.text.strip()
        if json_string.startswith("```json"):
            json_string = json_string[len("```json"):].strip()
        if json_string.endswith("```"):
            json_string = json_string[:-len("```")].strip()

        product_data = json.loads(json_string)

        grade_a_plus = product_data[0]
        grade_a = product_data[1]
        grade_b_c = product_data[2]

        cols = st.columns(3)

        with cols[0]:
            st.markdown(f"""
                <div class="product-card">
                    <img src="{grade_a_plus['image_url']}" class="product-img">
                    <h3 class="card-title">{grade_a_plus['condition']}</h3>
                    <p>{grade_a_plus['description']}</p>
                    <p class="card-price">${grade_a_plus['price']}</p>
                    <p class="risk-label risk-low">Risk: {grade_a_plus['risk']}</p>
                    <a href="#" class="btn">View Deal</a>
                </div>
            """, unsafe_allow_html=True)

        with cols[1]:
            st.markdown(f"""
                <div class="product-card">
                    <img src="{grade_a['image_url']}" class="product-img">
                    <h3 class="card-title">{grade_a['condition']}</h3>
                    <p>{grade_a['description']}</p>
                    <p class="card-price">${grade_a['price']}</p>
                    <p class="risk-label risk-medium">Risk: {grade_a['risk']}</p>
                    <a href="#" class="btn" style="background:#ffc107;">View Deal</a>
                </div>
            """, unsafe_allow_html=True)
            
        with cols[2]:
            st.markdown(f"""
                <div class="product-card">
                    <img src="{grade_b_c['image_url']}" class="product-img">
                    <h3 class="card-title">{grade_b_c['condition']}</h3>
                    <p>{grade_b_c['description']}</p>
                    <p class="card-price">${grade_b_c['price']}</p>
                    <p class="risk-label risk-high">Risk: {grade_b_c['risk']}</p>
                    <a href="#" class="btn" style="background:#dc3545;">View Deal</a>
                </div>
            """, unsafe_allow_html=True)

    except Exception as e:
        st.error(f"Failed to fetch AI data. Ensure GEMINI_API_KEY is set correctly. Error: {e}")
        st.info("Displaying static example for now.")
        # স্ট্যাটিক এক্সাম্পল (যদি এপিআই কাজ না করে)
        cols = st.columns(3)
        with cols[0]:
            st.markdown(f"""
                <div class="product-card">
                    <img src="https://images.unsplash.com/photo-1610945415295-cf822368c22a?q=80&w=1974&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D" class="product-img">
                    <h3 class="card-title">Grade A++</h3>
                    <p>New / Open Box</p>
                    <p class="card-price">$1200</p>
                    <p class="risk-label risk-low">Risk: 2%</p>
                    <a href="#" class="btn">View Deal</a>
                </div>
            """, unsafe_allow_html=True)
        # বাকি কলামগুলোতেও অনুরূপ স্ট্যাটিক কার্ড যুক্ত করুন


# --- ৮. ফুটার ---
st.markdown("""
    <div style="background: #333; color: #f0f2f5; padding: 40px 5%; text-align: center; margin-top: 50px; border-radius: 50px 50px 0 0;">
        <p>© 2026 Global Retail Intelligence. All rights reserved.</p>
        <p style="margin-top: 10px; font-size: 14px;">Privacy Policy | Terms of Service | Security</p>
    </div>
    """, unsafe_allow_html=True)    
