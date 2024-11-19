import streamlit as st

# Set page configuration
st.set_page_config(page_title="📦 E-Commerce Delivery Prediction", page_icon="📦", layout="wide")

# App title and description
st.markdown("""
# 📦 E-Commerce Delivery Prediction  
Predict whether your shipment will arrive **on time** based on shipment details.  
This tool takes into account the shipment mode, weight, product importance, and cost.
""")

# Add a clean horizontal separator
st.markdown("---")

# Input sections for the required attributes
st.subheader("Enter Shipment Details:")
shipment_mode = st.selectbox("🚚 Mode of Shipment", ["Flight", "Ship", "Road"], help="Select the transportation mode.")
discount_offered = st.number_input("💰 Discount Offered (%)", min_value=0.0, step=0.1, help="Enter the discount as a percentage.")
weight = st.number_input("⚖️ Weight (kg)", min_value=0.0, step=0.1, help="Enter the product weight in kilograms.")
product_importance = st.selectbox("🎯 Product Importance", ["Low", "Medium", "High"], help="Select the importance level of the product.")
cost_of_product = st.number_input("💵 Cost of the Product ($)", min_value=0.0, step=0.01, help="Enter the product's cost.")

# Prediction button and logic
st.markdown("### 🔮 Predict Delivery Status:")

if st.button("🚀 Predict"):
    try:
        # Determine delivery status based on the given rules
        if weight > 10:
            result = "Not On Time"
            extra_days = "It may take 2–3 extra days to deliver your order."
            st.error(f"**Prediction:** Delivery is **{result}**. {extra_days}")
        elif product_importance == "High":
            result = "Not On Time"
            extra_days = "It may take 2–3 extra days to deliver your order."
            st.error(f"**Prediction:** Delivery is **{result}**. {extra_days}")
        elif cost_of_product > 15000:
            result = "Not On Time"
            extra_days = "It may take 2–3 extra days to deliver your order."
            st.error(f"**Prediction:** Delivery is **{result}**. {extra_days}")
        else:
            result = "On Time"
            st.success(f"**Prediction:** Delivery is **{result}**!")
    except Exception as e:
        st.error(f"An error occurred during prediction: {str(e)}")

# Footer
st.markdown("""
---
Developed with ❤️ by Lakshman.
""")
