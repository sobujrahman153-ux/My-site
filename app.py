import streamlit as st

# আপনার কাছে থাকা HTML কোডটি নিচের তিন কোটেশনের মাঝখানে পেস্ট করুন
st.markdown("""
    <h1><!DOCTYPE html><html lang="en">
<head>
  <meta charset="UTF-8" />
  <title>GLOBAL-AI | Smart Product Finder</title>
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="bg-gray-100 text-gray-800"><!-- HEADER --><header class="bg-blue-900 text-white p-6 flex justify-between items-center">
  <h1 class="text-2xl font-bold">GLOBAL-AI</h1>
  <input id="searchInput" type="text" placeholder="Search products like Amazon..."
    class="w-1/2 p-3 rounded text-black" onkeyup="searchProducts()" />
</header><!-- ABOUT SECTION --><section class="bg-white p-8">
  <h2 class="text-xl font-bold mb-2">About Us</h2>
  <p>
    আমরা এমন একটি প্ল্যাটফর্ম যেখানে দামি ও ব্র্যান্ডেড রিটেল পণ্য
    কম দামে খুঁজে দেওয়া হয়। AI বিশ্লেষণের মাধ্যমে প্রিমিয়াম,
    গ্রেড-১ ও গ্রেড-২ পণ্যের সঠিক মূল্য তুলনা করা হয়।
  </p>
</section><!-- PRODUCTS --><section class="p-8">
  <h2 class="text-xl font-bold mb-4">🔥 Featured Products</h2>
  <div id="productGrid" class="grid grid-cols-1 md:grid-cols-3 lg:grid-cols-5 gap-4">
    <!-- 15 Products -->
    <script>
      const products = Array.from({ length: 15 }, (_, i) => ({
        name: `Premium Product ${i + 1}`,
        price: Math.floor(Math.random() * 800) + 200,
        rating: 5
      }));document.write(products.map(p => `
    <div class="bg-white p-4 rounded shadow product-card">
      <img src="https://picsum.photos/200/150?random=${Math.random()}" class="rounded mb-2" />
      <h3 class="font-bold">${p.name}</h3>
      <p class="text-red-600 font-bold">$${p.price}</p>
      <p class="text-yellow-500">⭐⭐⭐⭐⭐</p>
      <p class="text-sm text-gray-600">User reviews available</p>
    </div>
  `).join(''));
</script>

  </div>
</section><!-- REVIEWS --><section class="bg-white p-8">
  <h2 class="text-xl font-bold mb-4">💬 Customer Reviews</h2>
  <div class="space-y-2">
    <p>⭐ ⭐ ⭐ ⭐ ⭐ - "Amazing price!"</p>
    <p>⭐ ⭐ ⭐ ⭐ ⭐ - "Trusted liquidation platform"</p>
    <p>⭐ ⭐ ⭐ ⭐ ⭐ - "Got premium product cheaper"</p>
  </div>
</section><!-- PRICE ALERT --><section class="p-8">
  <h2 class="text-xl font-bold mb-4">🔔 Price Drop Alert</h2>
  <button onclick="showForm()" class="bg-blue-900 text-white px-4 py-2 rounded">
    Get Price Drop Alert
  </button>  <form id="alertForm" class="hidden mt-4 bg-white p-4 rounded shadow">
    <label class="block mb-2">Enter Your Mobile Number</label>
    <input type="text" class="border p-2 w-full mb-2" placeholder="01XXXXXXXXX" />
    <p class="text-sm mb-2">পণ্য দাম কমলে আপনাকে SMS/Alert দেওয়া হবে</p>
    <button type="submit" class="bg-green-600 text-white px-4 py-2 rounded">Submit</button>
  </form>
</section><!-- FOOTER --><footer class="bg-blue-900 text-white p-4 text-center">
  © 2026 GLOBAL-AI | Secure Platform
</footer><script>
  function showForm() {
    document.getElementById('alertForm').classList.toggle('hidden');
  }

  function searchProducts() {
    const value = document.getElementById('searchInput').value.toLowerCase();
    document.querySelectorAll('.product-card').forEach(card => {
      card.style.display = card.innerText.toLowerCase().includes(value)
        ? 'block'
        : 'none';
    });
  }
</script></body>
</html></h1>
    
    """, unsafe_allow_html=True)
import streamlit as st
import random
import time

# ১.পেজ কনফিগারেশন ও থিম
st.set_page_config(page_title="Global AI Liquidation", layout="wide", initial_sidebar_state="expanded")

# ২. প্রিমিয়াম সিএসএস (ক্যানভা ও আমাজন স্টাইল)
st.markdown("""
<style>
    .stApp { background-color: #f4f7f9; }
    .hero-banner {
        background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
        color: white; padding: 60px; text-align: center; border-radius: 20px; margin-bottom: 30px;
    }
    .product-card {
        background: white; padding: 20px; border-radius: 15px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1); border: 1px solid #eee;
        transition: 0.3s; height: 100%; text-align: center;
    }
    .product-card:hover { transform: translateY(-5px); box-shadow: 0 8px 25px rgba(0,0,0,0.15); }
    .price-tag { font-size: 24px; font-weight: bold; color: #d32f2f; }
    .old-price { text-decoration: line-through; color: #888; font-size: 16px; }
    .discount-badge {
        background: #ffeb3b; color: #000; padding: 5px 10px;
        border-radius: 5px; font-weight: bold; font-size: 14px;
    }
    .condition-badge {
        display: inline-block; padding: 3px 10px; border-radius: 20px;
        font-size: 12px; font-weight: bold; margin-bottom: 10px;
    }
</style>
""", unsafe_allow_html=True)

# ৩. সাইডবার নেভিগেশন (পেজ কন্ট্রোল)
st.sidebar.title("💎 AI DEALS MENU")
page = st.sidebar.radio("Go to:", ["🔍 AI Search Engine", "🛍️ Top 15 Hot Deals", "📋 Quality Details"])

# --- পেজ ১: AI সার্চ ইঞ্জিন (৪টি কোয়ালিটি) ---
if page == "🔍 AI Search Engine":
    st.markdown('<div class="hero-banner"><h1>Smart AI Search</h1><p>Find the best liquidation deals in seconds</p></div>', unsafe_allow_html=True)
    
    query = st.text_input("What are you looking for?", placeholder="e.g. iPhone 15, Laptop, Watch...")
    
    if query:
        with st.spinner('Analyzing 4 Quality Grades...'):
            time.sleep(1)
        
        st.subheader(f"Results for: {query}")
        cols = st.columns(4)
        
        base_price = random.randint(500, 2000)
        grades = [
            {"name": "Grade A++", "cond": "Brand New", "img": "https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=500", "price": base_price, "risk": "Low"},
            {"name": "Grade A", "cond": "Certified Refurb", "img": "https://images.unsplash.com/photo-1546868871-7041f2a55e12?w=500", "price": int(base_price*0.75), "risk": "Medium"},
            {"name": "Grade B", "cond": "Open Box", "img": "https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=500", "price": int(base_price*0.55), "risk": "Moderate"},
            {"name": "Grade C", "cond": "Bulk Stock", "img": "https://images.unsplash.com/photo-1526170315876-db60ec51068a?w=500", "price": int(base_price*0.35), "risk": "High"}
        ]
        
        for i, g in enumerate(cols):
            with g:
                item = grades[i]
                st.markdown(f"""
                <div class="product-card">
                    <span class="condition-badge" style="background:#e3f2fd; color:#1565c0;">{item['name']}</span>
                    <img src="{item['img']}" style="width:100%; border-radius:10px; margin-bottom:15px;">
                    <h4>{query} - {item['cond']}</h4>
                    <p class="old-price">${int(item['price']*1.33)}</p>
                    <p class="price-tag">${item['price']} <span class="discount-badge">25% OFF</span></p>
                    <p style="font-size:13px; color:#666;">Risk Index: {item['risk']}</p>
                </div>
                """, unsafe_allow_html=True)
                st.button(f"View Details {i}", use_container_width=True)

# --- পেজ ২: ১৫টি পন্যের লিস্ট ---
elif page == "🛍️ Top 15 Hot Deals":
    st.header("🔥 Today's Top 15 Liquidation Deals")
    st.info("Flash Sale: Extra 25% Discount Applied on all items!")
    
    # ১৫টি ডামি পন্য
    products = ["Smart Watch", "Gaming Laptop", "Wireless Buds", "DSLR Camera", "Tablet", 
                "Bluetooth Speaker", "Monitor", "Keyboard", "Drone", "VR Headset", 
                "Smartphone", "Console", "Smart Bulb", "Power Bank", "Headphones"]
    
    for i in range(0, 15, 3): # ৩টি করে প্রতি লাইনে
        cols = st.columns(3)
        for j in range(3):
            if i + j < 15:
                with cols[j]:
                    p_price = random.randint(100, 1000)
                    st.markdown(f"""
                    <div class="product-card">
                        <img src="https://picsum.photos/seed/{i+j+10}/300/200" style="width:100%; border-radius:10px;">
                        <h4 style="margin-top:10px;">{products[i+j]}</h4>
                        <p style="font-size:14px; color:#777;">High-quality liquidation stock from global retail hub.</p>
                        <p class="price-tag">${p_price} <span style="font-size:12px; color:#888; text-decoration:line-through;">${int(p_price*1.3)}</span></p>
                        <span class="discount-badge">Save 25% Today</span>
                    </div>
                    """, unsafe_allow_html=True)
                    st.button(f"Buy Now {i+j}", use_container_width=True)

# --- পেজ ৩: কোয়ালিটি ডিটেইলস ---
elif page == "📋 Quality Details":
    st.header("Understand Our Quality Grades")
    st.markdown("""
    ### 🛡️ How we analyze products:
    আমাদের এআই সিস্টেম প্রতিটি পন্যকে ৪টি প্রধান ভাগে ভাগ করে যাতে আপনি সঠিক সিদ্ধান্ত নিতে পারেন।
    
    1. **Grade A++ (Pristine):** এগুলো একদম নতুনের মতো। অরিজিনাল বক্স এবং ওয়ারেন্টি থাকে।
    2. **Grade A (Certified):** হালকা রিফারবিশড কিন্তু ১০০% কাজ করে। প্রফেশনাল চেক করা।
    3. **Grade B (Open Box):** বক্স খোলা হয়েছে বা হালকা দাগ থাকতে পারে। দাম অনেক কম।
    4. **Grade C (Liquidation):** সরাসরি কোম্পানির স্টক ক্লিয়ারেন্স থেকে আসা পন্য। রিস্ক বেশি কিন্তু লাভও বেশি।
    
    **কেন আমাদের ডিসকাউন্ট বেশি?**
    আমরা সরাসরি বড় বড় রিটেইল চেইন থেকে বাল্ক আকারে পন্য কিনি, তাই গ্রাহকদের ২৫% পর্যন্ত ডিসকাউন্ট দিতে পারি।
    """)
    st.image("https://images.unsplash.com/photo-1586528116311-ad8dd3c8310d?w=800")

# ফুটার
st.markdown("<hr><center>© 2026 AI Dealer Engine | Trusted by 10k+ Professionals</center>", unsafe_allow_html=True)
