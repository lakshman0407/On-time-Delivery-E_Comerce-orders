import streamlit as st
import pickle
import numpy as np

# Load the trained model
try:
    model = pickle.load(open("ecommerce_model.pkl", "rb"))
except FileNotFoundError:
    st.error("Model file not found. Please ensure 'ecommerce_model.pkl' exists.")
    st.stop()

# Set page configuration
st.set_page_config(page_title="E-Commerce Delivery Prediction", page_icon="📦", layout="wide")

# App title and description
st.title("📦 E-Commerce Delivery Prediction")
st.markdown("""
Welcome to the **E-Commerce Delivery Prediction App**!
This app helps predict whether a shipment will arrive on time based on several factors.
""")

# Organize inputs into sections
with st.expander("🔍 Input Shipment Details"):
    shipment_mode = st.selectbox("Mode of Shipment", ["Flight", "Ship", "Road"], help="Select the transportation mode.")
    customer_care_calls = st.slider("Customer Care Calls", 0, 10, 4, help="Number of calls made to customer care.")
    cost_of_product = st.number_input("Cost of the Product ($)", min_value=0.0, step=0.01, help="Enter the product's cost.")

with st.expander("🛒 Product Details"):
    discount_offered = st.number_input("Discount Offered (%)", min_value=0.0, step=0.1, help="Percentage discount offered.")
    weight = st.number_input("Weight (grams)", min_value=0.0, step=0.1, help="Weight of the product in grams.")
    product_importance = st.selectbox("Product Importance", ["Low", "Medium", "High"], help="Select product importance level.")

with st.expander("👤 Customer Details"):
    gender = st.selectbox("Customer Gender", ["Male", "Female"], help="Select the gender of the customer.")
    warehouse_distance = st.number_input("Warehouse Distance (km)", min_value=0.0, step=0.1, value=10.0, help="Distance between warehouse and delivery point.")
    delivery_time = st.number_input("Expected Delivery Time (days)", min_value=1, value=5, help="Enter the estimated delivery time.")

# Encoding categorical features
def encode_inputs():
    shipment_mode_mapping = {"Flight": 0, "Ship": 1, "Road": 2}
    product_importance_mapping = {"Low": 0, "Medium": 1, "High": 2}
    gender_mapping = {"Male": 0, "Female": 1}

    return [
        shipment_mode_mapping[shipment_mode],
        customer_care_calls,
        cost_of_product,
        discount_offered,
        weight,
        product_importance_mapping[product_importance],
        gender_mapping[gender],
        warehouse_distance,
        delivery_time,
        0,  # Placeholder for Feature_10
        0   # Placeholder for Feature_11
    ]

# Prediction logic
if st.button("🚚 Predict Delivery Status"):
    try:
        input_data = np.array(encode_inputs()).reshape(1, -1)
        prediction = model.predict(input_data)
        prediction_proba = model.predict_proba(input_data) if hasattr(model, "predict_proba") else None

        # Result formatting
        result = "On Time" if prediction[0] == 1 else "Not On Time"
        st.markdown(f"### 🚚 **Prediction Result**: **{result}**")
        
        if prediction_proba is not None:
            st.markdown(f"**Confidence**: {max(prediction_proba[0]) * 100:.2f}%")
    except Exception as e:
        st.error(f"An error occurred during prediction: {str(e)}")

# Footer
st.markdown("""
---
Developed with ❤️ by Lakshman.
""")
