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

# Encoding for shipment_mode (manually encoded to match training)
shipment_mode_mapping = {"Flight": 0, "Ship": 1, "Road": 2}
shipment_mode_encoded = shipment_mode_mapping[shipment_mode]

# Preprocessing input (ensure the feature order matches training)
input_data = np.array([
    shipment_mode_encoded, customer_care_calls, cost_of_product,
    discount_offered, weight
]).reshape(1, -1)

# Prediction
if st.button("Predict"):
    try:
        prediction = model.predict(input_data)
        result = "On Time" if prediction[0] == 1 else "Not On Time"
        st.success(f"The shipment is predicted to be: {result}")
    except Exception as e:
        st.error(f"Error during prediction: {str(e)}")
