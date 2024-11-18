import streamlit as st
import pickle
import numpy as np

# Load the trained model
model = pickle.load(open("model.pkl", "rb"))

st.title("E-Commerce Delivery Prediction")
st.write("Predict whether the shipment will reach on time.")

# User Inputs
warehouse = st.selectbox("Warehouse Block", ["A", "B", "C", "D", "F"])
shipment_mode = st.selectbox("Mode of Shipment", ["Flight", "Ship", "Road"])
customer_care_calls = st.slider("Customer Care Calls", 0, 10, 4)
customer_rating = st.slider("Customer Rating", 1, 5, 3)
cost_of_product = st.number_input("Cost of the Product", min_value=0)
prior_purchases = st.slider("Prior Purchases", 0, 15, 3)
product_importance = st.selectbox("Product Importance", ["low", "medium", "high"])
gender = st.selectbox("Gender", ["M", "F"])
discount_offered = st.number_input("Discount Offered", min_value=0)
weight = st.number_input("Weight in grams", min_value=0)

# Preprocessing input
input_data = np.array([
    warehouse, shipment_mode, customer_care_calls, customer_rating, 
    cost_of_product, prior_purchases, product_importance, gender, 
    discount_offered, weight
]).reshape(1, -1)

# Prediction
if st.button("Predict"):
    prediction = model.predict(input_data)
    result = "On Time" if prediction[0] == 1 else "Not On Time"
    st.success(f"The shipment is predicted to be: {result}")
