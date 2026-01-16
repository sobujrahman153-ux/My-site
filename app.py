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
    st.image("https://images.unsplash.com/photo-1586528116311-a
