import streamlit as st
import pickle
import numpy as np

# Load the trained model
model = pickle.load(open("ecommerce_model.pkl", "rb"))

st.title("E-Commerce Delivery Prediction")
st.write("Predict whether the shipment will reach on time based on user inputs.")

# User Inputs
shipment_mode = st.selectbox("Mode of Shipment", ["Flight", "Ship", "Road"])
customer_care_calls = st.slider("Customer Care Calls", 0, 10, 4)
cost_of_product = st.number_input("Cost of the Product", min_value=0)
discount_offered = st.number_input("Discount Offered", min_value=0)
weight = st.number_input("Weight in grams", min_value=0)

# Additional features (use default values or collect more inputs if needed)
product_importance = st.selectbox("Product Importance", ["Low", "Medium", "High"])
gender = st.selectbox("Gender of Customer", ["Male", "Female"])

# Encoding categorical features
shipment_mode_mapping = {"Flight": 0, "Ship": 1, "Road": 2}
product_importance_mapping = {"Low": 0, "Medium": 1, "High": 2}
gender_mapping = {"Male": 0, "Female": 1}

shipment_mode_encoded = shipment_mode_mapping[shipment_mode]
product_importance_encoded = product_importance_mapping[product_importance]
gender_encoded = gender_mapping[gender]

# Placeholder values for other missing features
warehouse_distance = st.number_input("Warehouse Distance (km)", min_value=0, value=10)  # Default value
delivery_time = st.number_input("Expected Delivery Time (days)", min_value=1, value=5)  # Default value

# Combine all features into one input array
input_data = np.array([
    shipment_mode_encoded, customer_care_calls, cost_of_product,
    discount_offered, weight, product_importance_encoded,
    gender_encoded, warehouse_distance, delivery_time,
    0,  # Replace with actual value for 'Feature_10'
    0   # Replace with actual value for 'Feature_11'
]).reshape(1, -1)

# Prediction
if st.button("Predict"):
    try:
        prediction = model.predict(input_data)
        result = "On Time" if prediction[0] == 1 else "Not On Time"
        st.success(f"The shipment is predicted to be: {result}")
    except Exception as e:
        st.error(f"Error during prediction: {str(e)}")
