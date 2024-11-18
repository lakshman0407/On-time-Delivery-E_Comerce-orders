import streamlit as st
import pickle
import numpy as np

# Load the trained model
model = pickle.load(open("On-Time Delivery of E-Commerce Orders.pkl", "rb"))

st.title("E-Commerce Delivery Prediction")
st.write("Predict whether the shipment will reach on time.")

# User Inputs
shipment_mode = st.selectbox("Mode of Shipment", ["Flight", "Ship", "Road"])
customer_care_calls = st.slider("Customer Care Calls", 0, 10, 4)
cost_of_product = st.number_input("Cost of the Product", min_value=0)
discount_offered = st.number_input("Discount Offered", min_value=0)
weight = st.number_input("Weight in grams", min_value=0)

# Preprocessing input
input_data = np.array([
    shipment_mode, customer_care_calls, cost_of_product, 
    discount_offered, weight
]).reshape(1, -1)

# Prediction
if st.button("Predict"):
    try:
        prediction = model.predict(input_data)
        result = "On Time" if prediction[0] == 1 else "Not On Time"
        st.write(f"The shipment is predicted to be: {result}")
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
