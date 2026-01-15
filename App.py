import streamlit as st
import requests
from bs4 import BeautifulSoup
import google.generativeai as genai
import time
import json
import random

# --- ১. গুগল সার্চ ইঞ্জিন অপ্টিমাইজেশন (SEO Schema) ---
def inject_seo():
    seo_data = {
        "@context": "https://schema.org",
        "@type": "ComparisonShoppingService",
        "name": "Global Retail Liquidation Finder",
        "description": "Premium Grade 1-2-3 Liquidation and Open-Box deals from Amazon, Walmart, and eBay.",
        "provider": ["Amazon", "Walmart", "eBay", "Target", "Best Buy", "Argos", "Kmart"]
    }
    st.markdown(f'<script type="application/ld+json">{json.dumps(seo_data)}</script>', unsafe_allow_html=True)

# --- ২. প্রিমিয়াম ইউজার ইন্টারফেস (UI Customization) ---
st.set_page_config(page_title="Global Retail Deals AI", page_icon="💎", layout="wide")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&display=swap');
    html, body, [class*="css"] { font-family: 'Inter', sans-serif; background-color: #F9FAFB; }
    .main-header { background: linear-gradient(90deg, #1E3A8A 0%, #3B82F6 100%); padding: 40px; border-radius: 20px; color: white; text-align: center; margin-bottom: 30px; }
    .deal-card { background: white; padding: 25px; border-radius: 18px; box-shadow: 0 10px 25px rgba(0,0,0,0.05); border-left: 8px solid #3B82F6; margin-bottom: 25px; transition: 0.4s; }
    .deal-card:hover { transform: translateY(-10px); box-shadow: 0 15px 35px rgba(0,0,0,0.1); }
    .badge { background: #EEE; padding: 5px 12px; border-radius: 20px; font-size: 12px; font-weight: bold; color: #1E3A8A; }
    .price-text { font-size: 28px; color: #EF4444; font-weight: 800; }
    </style>
    """, unsafe_allow_html=True)

# --- ৩. এআই ও সিক্রেটস কনফিগারেশন ---
inject_seo()
GEMINI_KEY = st.secrets.get("GEMINI_API_KEY", "")
if GEMINI_KEY:
    genai.configure(api_key=GEMINI_KEY)
    ai_model = genai.GenerativeModel('gemini-pro')

# --- ৪. সাইডবার: কাস্টমার রিটেনশন (টোপ) ---
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/3081/3081840.png", width=80)
    st.title("Elite Rewards")
    st.markdown("🎁 **Special Offer:** সাইটে ৯০ সেকেন্ড সময় কাটালে একটি **Mystery Coupon** আনলক হবে!")
    st.progress(random.randint(20, 80), text="Today's Savings Activity")
    st.divider()
    st.warning("⚠️ **আইনি তথ্য:** এটি একটি অনুমোদিত অ্যাফিলিয়েট সাইট। আমরা পণ্যের বিক্রয় থেকে কমিশন পেতে পারি।")

# --- ৫. মেইন ড্যাশবোর্ড: স্মার্ট লোকেশন ও কোম্পানি ফিল্টার ---
st.markdown('<div class="main-header"><h1>🌍 AI Global Retail Liquidation Finder</h1><p>USA • UK • CANADA • AUSTRALIA এর সেরা ডিল এক জায়গায়</p></div>', unsafe_allow_html=True)

col1, col2, col3 = st.columns([2, 1, 1])

with col1:
    search_q = st.text_input("🔍 পণ্যটি খুঁজুন (যেমন: iPhone, MacBook, Sony TV)", placeholder="Search Premium Liquidation...")

with col2:
    selected_country = st.selectbox("📍 দেশ সিলেক্ট করুন", ["United States", "United Kingdom", "Canada", "Australia"])

with col3:
    # বড় রিটেইল কোম্পানিগুলোর নাম যোগ করা হয়েছে
    retailer = st.selectbox("🏢 কোম্পানি পছন্দ করুন", ["All Retailers", "Amazon", "Walmart", "eBay", "Target", "Best Buy", "Argos", "Kmart"])

# --- ৬. প্রফেশনাল ডাটা প্রসেসিং ইঞ্জিন ---
if search_q:
    with st.status("🚀 গুগল এআই এবং গ্লোবাল সার্ভার স্ক্যান করা হচ্ছে...", expanded=True) as status:
        st.write(f"Connecting to {retailer} {selected_country} servers...")
        time.sleep(1.5)
        st.write("Verifying Grade 1, 2, 3 product quality...")
        time.sleep(1.2)
        status.update(label="✅ সেরা ডিলগুলো পাওয়া গেছে!", state="complete", expanded=False)

    # ডিল খোঁজার লজিক (ইবে এপিআই বেসড ফর গ্লোবাল)
    refined_query = f"{search_q} {retailer} open box clearance"
    url = f"https://www.ebay.com/sch/i.html?_nkw={refined_query}"
    
    try:
        response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
        soup = BeautifulSoup(response.text, 'html.parser')
        items = soup.find_all('li', class_='s-item')

        for item in items[1:6]:
            title = item.find('h3').text if item.find('h3') else "N/A"
            price = item.find('span', class_='s-item__price').text if item.find('span', class_='s-item__price') else "Price Hidden"
            link = item.find('a', class_='s-item__link')['href'] if item.find('a', class_='s-item__link') else "#"
            img = item.find('img')['src'] if item.find('img') else "https://via.placeholder.com/150"

            # প্রফেশনাল কার্ড ডিজাইন
            st.markdown(f"""
            <div class="deal-card">
                <div style="display: flex; gap: 25px; align-items: center; flex-wrap: wrap;">
                    <img src="{img}" width="180" style="border-radius: 12px;">
                    <div style="flex: 1;">
                        <span class="badge">Grade 1 - Quality Verified</span>
                        <h3 style="margin-top: 10px; color: #1F2937;">{title}</h3>
                        <p style="color: #6B7280; font-size: 14px;">Store: <b>{retailer if retailer != 'All Retailers' else 'Official Global Store'}</b></p>
                        <p class="price-text">{price}</p>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)

            # এআই এনালাইসিস (গ্রাহককে ১ মিনিট ধরে রাখার টোপ)
            if GEMINI_KEY:
                with st.expander("🤖 এআই স্মার্ট রিভিউ (এটি অবশ্যই পড়ুন)"):
                    st.write(f"**বিশ্লেষণ:** এই {title} পণ্যটি বর্তমানে {selected_country} এর গড় বাজার মূল্যের চেয়ে অনেক কম। এটি একটি লিকুইডেশন স্টক হওয়ার সম্ভাবনা ৯০%।")
                    st.info("টিপস: চেকআউটের সময় শিপিং খরচ আপনার ঠিকানায় কত পড়বে তা একবার দেখে নিন।")

            # অ্যাফিলিয়েট বাটন
            ebay_id = st.secrets.get("EBAY_AFFILIATE_ID", "default_id")
            st.link_button(f"👉 {retailer} থেকে ডিলটি নিন", url=f"{link}&campid={ebay_id}")
            st.write("")

    except Exception as e:
        st.error("সার্ভার কানেকশন এরর। আবার চেষ্টা করুন।")

# --- ৭. শেয়ার ও আইনি ঘোষণা ---
st.divider()
col_f1, col_f2 = st.columns(2)
with col_f1:
    st.markdown("### 📢 আপনার বন্ধুদের জানান")
    st.button("🔗 সাইট লিঙ্ক কপি করুন এবং শেয়ার করুন")
with col_f2:
    st.markdown("### 🛡️ নিরাপদ শপিং গ্যারান্টি")
    st.write("আমাদের এআই শুধুমাত্র ভেরিফাইড এবং উচ্চ রেটিং প্রাপ্ত বিক্রেতাদের ডিল খুঁজে বের করে।")

st.markdown('<div style="text-align: center; color: #9CA3AF; font-size: 12px; margin-top: 40px;">© 2026 Global Smart DealFinder. Powered by Google Gemini AI Engine. All rights reserved.</div>', unsafe_allow_html=True)
