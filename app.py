import streamlit as st
import pickle
import numpy as np

# Load the trained model
model = pickle.load(open("ecommerce_model.pkl", "rb"))

# Set page config for a better layout
st.set_page_config(page_title="E-Commerce Delivery Prediction", page_icon="📦", layout="wide")

# Title and description
st.title("E-Commerce Delivery Prediction 📦")
st.write("""
    **Welcome to the E-Commerce Delivery Prediction App!**
    This app predicts whether an e-commerce shipment will arrive on time based on various factors like shipment mode, product cost, customer care calls, and more.
""")

# Sidebar for navigation and inputs
st.sidebar.header("Input Features")
st.sidebar.write("Provide the following details about the shipment:")

# Use columns to organize input fields neatly
col1, col2 = st.columns(2)

with col1:
    shipment_mode = st.selectbox("Mode of Shipment", ["Flight", "Ship", "Road"])
    customer_care_calls = st.slider("Customer Care Calls", 0, 10, 4)
    cost_of_product = st.number_input("Cost of the Product", min_value=0)

with col2:
    discount_offered = st.number_input("Discount Offered", min_value=0)
    weight = st.number_input("Weight in grams", min_value=0)
    product_importance = st.selectbox("Product Importance", ["Low", "Medium", "High"])

# Additional features (using default values or placeholders)
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

# Prediction button with styled text
if st.button("Predict", use_container_width=True):
    try:
        prediction = model.predict(input_data)
        result = "On Time" if prediction[0] == 1 else "Not On Time"
        st.markdown(f"### 🚚 **Prediction Result**: The shipment is predicted to be: **{result}**")
    except Exception as e:
        st.error(f"Error during prediction: {str(e)}")

# Add some explanatory text or additional styling
st.markdown("""
    ---
    **Note:** The model considers multiple factors, including customer care calls, cost, shipment mode, and product importance.
    Please ensure all the data you input is correct for better prediction results.
""")

# Optional: Add an image or a visualization (e.g., for delivery times, etc.)
# st.image("image_path_or_url.png", caption="Sample Image")

# Add footer or credits
st.markdown("""
    ---
    Developed with ❤️ by [Your Name](https://your-profile-link) for E-Commerce Delivery Prediction.
""")
