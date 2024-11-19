import streamlit as st

# Set page configuration
st.set_page_config(page_title="E-Commerce Delivery Prediction", page_icon="📦", layout="wide")

# App title and description
st.title("📦 E-Commerce Delivery Prediction")
st.markdown("""
Welcome to the **E-Commerce Delivery Prediction App**!  
This app predicts whether your shipment will be delivered on time based on a few simple factors.
""")

# Input sections for the required attributes
with st.expander("🔍 Input Shipment Details"):
    shipment_mode = st.selectbox("Mode of Shipment", ["Flight", "Ship", "Road"], help="Select the transportation mode.")
    discount_offered = st.number_input("Discount Offered (%)", min_value=0.0, step=0.1, help="Enter the discount as a percentage.")
    weight = st.number_input("Weight (kg)", min_value=0.0, step=0.1, help="Enter the product weight in kilograms.")
    product_importance = st.selectbox("Product Importance", ["Low", "Medium", "High"], help="Select the importance level of the product.")
    cost_of_product = st.number_input("Cost of the Product ($)", min_value=0.0, step=0.01, help="Enter the product's cost.")

# Prediction logic
if st.button("🚚 Predict Delivery Status"):
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
        st.success(f"**Prediction:** Delivery is **{result}**.")

# Footer
st.markdown("""
---
Developed by Lakshman.
""")
