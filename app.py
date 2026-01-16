import streamlit as st
import random

# ১. পেজ এবং থিম সেটআপ
st.set_page_config(page_title="GLOBAL-AI | Premium Liquidation Hub", layout="wide")

# ২. কাস্টম সিএসএস (ডিজাইন সুন্দর করার জন্য)
st.markdown("""
<style>
    .stApp { background-color: #f8fafc; }
    .header-box { background: linear-gradient(90deg, #1e3a8a 0%, #3b82f6 100%); color: white; padding: 30px; border-radius: 15px; text-align: center; margin-bottom: 25px; }
    .product-card { background: white; padding: 20px; border-radius: 15px; border: 1px solid #e2e8f0; text-align: center; transition: 0.3s; height: 450px; }
    .product-card:hover { transform: translateY(-5px); box-shadow: 0 10px 20px rgba(0,0,0,0.1); }
    .price-tag { color: #1e40af; font-size: 22px; font-weight: 800; }
    .old-price { text-decoration: line-through; color: #94a3b8; font-size: 14px; }
    .badge { background: #ef4444; color: white; padding: 2px 8px; border-radius: 5px; font-size: 12px; font-weight: bold; }
</style>
""", unsafe_allow_html=True)

# ৩. হেডার ও দেশ নির্বাচন
st.markdown("<div class='header-box'><h1>💠 GLOBAL-AI INTELLIGENCE</h1><p>AI-Powered Professional Liquidation Engine</p></div>", unsafe_allow_html=True)

countries = ["USA", "UK", "Bangladesh", "UAE", "Germany", "Canada", "Australia", "India", "France", "Japan", "Italy", "Singapore", "Malaysia", "KSA", "Qatar", "China", "Brazil", "Spain", "Turkey", "Netherlands"]
selected_country = st.sidebar.selectbox("🌍 Select Shipping Region", countries)
st.sidebar.info(f"Showing best deals for: {selected_country}")

# ৪. সার্চ বার এবং ৪ রকম পন্যের রেজাল্ট
query = st.text_input("🔍 Search for a product...", placeholder="e.g. iPhone, Watch, Sneakers")

if query:
    st.subheader(f"AI Market Comparison for: {query}")
    c1, c2, c3, c4 = st.columns(4)
    base_p = random.randint(500, 1500)
    
    grades = [
        {"name": "Amazon Premium", "price": base_p, "tag": "Original Retail", "color": "#ff9900"},
        {"name": "Grade 1 (Mint)", "price": int(base_p*0.75), "tag": "25% OFF", "color": "#2e7d32"},
        {"name": "Grade 2 (Open Box)", "price": int(base_p*0.50), "tag": "50% OFF", "color": "#1565c0"},
        {"name": "Grade 3 (Bulk)", "price": int(base_p*0.30), "tag": "70% OFF", "color": "#c62828"}
    ]
    
    for i, col in enumerate([c1, c2, c3, c4]):
        with col:
            st.markdown(f"""
            <div class="product-card" style="border-top: 5px solid {grades[i]['color']};">
                <span class="badge" style="background:{grades[i]['color']}">{grades[i]['tag']}</span>
                <img src="https://loremflickr.com/300/200/{query}?lock={i}" style="width:100%; border-radius:10px; margin:15px 0;">
                <h4>{grades[i]['name']}</h4>
                <p class="price-tag">${grades[i]['price']}</p>
                <p style="font-size:12px; color:gray;">Verified stock in {selected_country}</p>
            </div>
            """, unsafe_allow_html=True)
            if st.button("Set Price Alert", key=f"alert_{i}"):
                st.toast(f"✅ Alert set! We'll notify you when {query} drops more.", icon="🔔")

st.divider()

# ৫. ১৫টি ডিমান্ডিং রিটেইল পণ্য (Default লিস্ট)
st.subheader("🔥 Top 15 High-Demand Retail Products")
top_products = [
    "iPhone 15 Pro", "Samsung S24 Ultra", "MacBook Air M3", "Sony Headphones", "Rolex Submariner",
    "PlayStation 5", "Dyson Vacuum", "Nike Air Jordan", "iPad Pro", "Dell XPS 13",
    "GoPro HERO12", "Canon EOS R6", "Nintendo Switch", "Bose Speakers", "Electric Scooter"
]

for row in range(3):
    cols = st.columns(5)
    for j in range(5):
        index = row * 5 + j
        product_name = top_products[index]
        with cols[j]:
            p_price = random.randint(150, 950)
            st.markdown(f"""
            <div class="product-card">
                <img src="https://loremflickr.com/300/200/{product_name.replace(' ', ',')}?lock={index+10}" style="width:100%; border-radius:10px;">
                <p style="font-weight:bold; margin-top:10px;">{product_name}</p>
                <p class="old-price">${int(p_price*1.4)}</p>
                <p class="price-tag">${p_price}</p>
            </div>
            """, unsafe_allow_html=True)

# ৬. ইউজার রেটিং (১২-২০ জন)
st.divider()
st.subheader("🌟 Trusted by Global Users")
col_rev1, col_rev2 = st.columns([1, 2])
with col_rev1:
    st.markdown("## 4.9 / 5.0")
    st.write("⭐⭐⭐⭐⭐ (12,450 Reviews)")
with col_rev2:
    for i in range(3):
        st.markdown(f"> **User_{random.randint(100,999)}**: 'Incredible price for {top_products[i]}! Highly recommended.' ⭐⭐⭐⭐⭐")

st.markdown("<hr><center>© 2026 GLOBAL-AI INTELLIGENCE | Professional Enterprise System</center>", unsafe_allow_html=True)
