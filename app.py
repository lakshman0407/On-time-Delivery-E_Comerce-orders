import streamlit as st
import pickle
import numpy as np
from sklearn.preprocessing import LabelEncoder

# Load the trained model
model = pickle.load(open("On-Time Delivery of E-Commerce Orders.pkl", "rb"))

# Initialize the LabelEncoder
label_encoder = LabelEncoder()

st.title("E-Commerce Delivery Prediction")
st.write("Predict whether the shipment will reach on time.")

# User Inputs
shipment_mode = st.selectbox("Mode of Shipment", ["Flight", "Ship", "Road"])
customer_care_calls = st.slider("Customer Care Calls", 0, 10, 4)
cost_of_product = st.number_input("Cost of the Product", min_value=0)
discount_offered = st.number_input("Discount Offered", min_value=0)
weight = st.number_input("Weight in grams", min_value=0)

# Encoding the shipment_mode input
# This assumes that 'shipment_mode' is a categorical variable, so we use LabelEncoder.
shipment_mode_encoded = label_encoder.fit_transform(["Flight", "Ship", "Road"])  # Encode all values at once
shipment_mode_value = label_encoder.transform([shipment_mode])[0]  # Transform the selected input

# Preprocessing input (make sure to match the same order as used during training)
input_data = np.array([
    shipment_mode_value, customer_care_calls, cost_of_product, 
    discount_offered, weight
]).reshape(1, -1)

# Prediction
if st.button("Predict"):
    try:
        # Ensure that the model's predict method is available and that input shape is correct
        if hasattr(model, 'predict'):
            prediction = model.predict(input_data)
            result = "On Time" if prediction[0] == 1 else "Not On Time"
            st.write(f"The shipment is predicted to be: {result}")
        else:
            st.error("Model does not have a 'predict' method.")
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
