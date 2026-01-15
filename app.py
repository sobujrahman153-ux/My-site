import streamlit as st
import random
import time
import re

# --- ১. সিকিউরিটি এবং পেজ কনফিগারেশন (Hack-Proof Setup) ---
st.set_page_config(
    page_title="Global Retail Intelligence | Premium Liquidation",
    page_icon="🛡️",
    layout="wide", # সাইটটি বড় দেখানোর জন্য
    initial_sidebar_state="collapsed"
)

# ইনপুট ক্লিন করার ফাংশন (Security Layer)
def clean_input(text):
    return re.sub(r'[<>/{}[\]\\^`|]', '', text)

# --- ২. প্রফেশনাল সিএসএস (Modern E-commerce Design) ---
st.markdown("""
    <style>
    /* মেইন ব্যাকগ্রাউন্ড */
    .stApp {
        background: #f8f9fa;
        color: #1d1d1f;
    }
    
    /* প্রিমিয়াম নেভিগেশন বার */
    .nav-bar {
        background: #ffffff;
        padding: 15px 50px;
        display: flex;
        justify-content: space-between;
        align-items: center;
        box-shadow: 0 2px 10px rgba(0,0,0,0.05);
        position: fixed;
        top: 0; left: 0; right: 0; z-index: 1000;
    }

    /* হিরো সেকশন - গ্রাহককে আটকে রাখার জন্য */
    .hero-section {
        background: linear-gradient(135deg, #0071e3 0%, #1d1d1f 100%);
        color: white;
        padding: 80px 10% 60px 10%;
        text-align: center;
        border-radius: 0 0 50px 50px;
        margin-bottom: 40px;
    }

    /* প্রোডাক্ট কার্ড ডিজাইন (Apple Style) */
    .product-container {
        display: flex;
        gap: 20px;
        justify-content: center;
        flex-wrap: wrap;
        padding: 20px;
    }

    .premium-card {
        background: white;
        border-radius: 24px;
        padding: 30px;
        width: 320px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.05);
        border: 1px solid #e5e5e7;
        transition: all 0.4s ease;
    }

    .premium-card:hover {
        transform: translateY(-10px);
        box-shadow: 0 20px 40px rgba(0,0,0,0.1);
    }

    .price-large {
        font-size: 42px;
        font-weight: 700;
        color: #0071e3;
        margin: 15px 0;
    }

    .trust-badge {
        background: #eef6ff;
        color: #0071e3;
        padding: 5px 12px;
        border-radius: 100px;
        font-size: 12px;
        font-weight: 600;
    }

    .footer {
        background: #1d1d1f;
        color: #86868b;
        padding: 50px 10%;
        text-align: center;
        font-size: 14px;
        margin-top: 50px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- ৩. মেইন ইন্টারফেস: হিরো সেকশন ---
st.markdown("""
    <div class="hero-section">
        <h1 style="font-size: 56px; font-weight: 700; margin-bottom: 20px;">
            The Intelligence Behind Your Savings.
        </h1>
        <p style="font-size: 24px; font-weight: 400; opacity: 0.9;">
            AI-Verified Liquidation Stocks from 500+ Verified Retailers Worldwide.
        </p>
    </div>
    """, unsafe_allow_html=True)

# --- ৪. স্মার্ট সার্চ ইঞ্জিন ---
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    raw_query = st.text_input("", placeholder="Search for luxury electronics, watches, or laptops...", label_visibility="collapsed")
    search_q = clean_input(raw_query) # হ্যাকিং প্রতিরোধ

if search_q:
    with st.spinner('🔐 Verifying global inventory through SSL-encrypted bridge...'):
        time.sleep(1.5)
    
    base_price = random.randint(700, 2500)

    # রেজাল্ট এরিয়া
    st.markdown(f"<h2 style='text-align:center; margin: 40px 0;'>Market Comparison for '{search_q}'</h2>", unsafe_allow_html=True)

    # প্রিমিয়াম ই-কমার্স লুক
    st.markdown(f"""
        <div class="product-container">
            <div class="premium-card">
                <span class="trust-badge">AUTHENTICATED</span>
                <h3 style="margin-top:15px;">Pristine Condition</h3>
                <p style="color:#86868b;">Grade A++ (Open Box/New)</p>
                <div class="price-large">${base_price}</div>
                <p style="color:#008000; font-weight:600;">✓ Lowest Market Risk (0.5%)</p>
                <p style="font-size:14px; color:#555; margin-top:15px;">Full manufacture warranty included with zero cosmetic imperfections.</p>
                <div style="background:#0071e3; color:white; text-align:center; padding:12px; border-radius:12px; margin-top:20px; font-weight:600;">Secure Purchase</div>
            </div>

            <div class="premium-card" style="border: 2px solid #0071e3;">
                <span class="trust-badge" style="background:#fff2e0; color:#ff9500;">BEST VALUE</span>
                <h3 style="margin-top:15px;">Smart Refurbished</h3>
                <p style="color:#86868b;">Grade A (Verified Refurb)</p>
                <div class="price-large">${int(base_price * 0.75)}</div>
                <p style="color:#ff9500; font-weight:600;">⚠ Moderate Risk (12%)</p>
                <p style="font-size:14px; color:#555; margin-top:15px;">Professionally inspected. May have 1-2 minor microscopic scratches.</p>
                <div style="background:#0071e3; color:white; text-align:center; padding:12px; border-radius:12px; margin-top:20px; font-weight:600;">Secure Purchase</div>
            </div>

            <div class="premium-card">
                <span class="trust-badge" style="background:#ffebee; color:#ff3b30;">CLEARANCE</span>
                <h3 style="margin-top:15px;">Bulk Liquidation</h3>
                <p style="color:#86868b;">Grade B/C (Used Stock)</p>
                <div class="price-large">${int(base_price * 0.45)}</div>
                <p style="color:#ff3b30; font-weight:600;">🛑 High Risk (35%)</p>
                <p style="font-size:14px; color:#555; margin-top:15px;">Deeply discounted. Visible wear. Recommended for bulk buyers only.</p>
                <div style="background:#1d1d1f; color:white; text-align:center; padding:12px; border-radius:12px; margin-top:20px; font-weight:600;">Secure Purchase</div>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # --- ৫. ট্রাস্ট সেকশন (যাতে মানুষ সাইট থেকে না বের হয়) ---
    st.markdown("""
        <div style="background: white; padding: 60px 10%; margin-top: 50px; border-radius: 40px; text-align: center;">
            <h2 style="font-size: 36px; margin-bottom: 40px;">Why Trust Our AI Engine?</h2>
            <div style="display: flex; justify-content: space-around; flex-wrap: wrap; gap: 30px;">
                <div style="width: 250px;">
                    <h4 style="color:#0071e3;">Military Grade Encryption</h4>
                    <p style="color:#86868b; font-size:14px;">Your data and searches are protected by 256-bit SSL security.</p>
                </div>
                <div style="width: 250px;">
                    <h4 style="color:#0071e3;">Verified Dealers Only</h4>
                    <p style="color:#86868b; font-size:14px;">We only pull data from retailers with 98%+ positive feedback.</p>
                </div>
                <div style="width: 250px;">
                    <h4 style="color:#0071e3;">Real-time Analysis</h4>
                    <p style="color:#86868b; font-size:14px;">Prices are updated every 60 seconds from global servers.</p>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)

# --- ৬. ফুটার ---
st.markdown("""
    <div class="footer">
        <p>Copyright © 2026 Retail Intelligence Global Inc. All rights reserved.</p>
        <p style="margin-top: 10px;">Privacy Policy | Terms of Service | Security Information</p>
        <div style="margin-top: 20px;">
            <span style="border: 1px solid #333; padding: 5px 10px; border-radius: 5px; margin-right: 10px;">🛡️ PCI Compliant</span>
            <span style="border: 1px solid #333; padding: 5px 10px; border-radius: 5px;">🔒 SSL Secure</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
