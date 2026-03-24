import streamlit as st
import pandas as pd
import pickle

st.title("Sales Profit Prediction")

month = st.selectbox("Select Month:", [
    'January', 'February', 'March', 'April', 'May', 'June',
    'July', 'August', 'September', 'October', 'November', 'December'
])

customer_age = st.number_input("Customer Age:", min_value=10, max_value=100)

customer_gender = st.selectbox("Select Gender:", ['M', 'F'])

country = st.selectbox("Select Country:", [
    'Australia', 'Canada', 'France', 'Germany', 'United Kingdom', 'United States'
])

state = st.selectbox("Select State:", [
    'Alabama', 'Alberta', 'Arizona', 'Bayern', 'Brandenburg',
    'British Columbia', 'California', 'Charente-Maritime', 'England',
    'Essonne', 'Florida', 'Garonne (Haute)', 'Georgia', 'Hamburg',
    'Hauts de Seine', 'Hessen', 'Illinois', 'Kentucky', 'Loir et Cher',
    'Loiret', 'Massachusetts', 'Minnesota', 'Mississippi', 'Missouri',
    'Montana', 'Moselle', 'New South Wales', 'New York', 'Nord',
    'Nordrhein-Westfalen', 'North Carolina', 'Ohio', 'Ontario', 'Oregon',
    'Pas de Calais', 'Queensland', 'Saarland', 'Seine (Paris)',
    'Seine Saint Denis', 'Seine et Marne', 'Somme', 'South Australia',
    'South Carolina', 'Tasmania', 'Texas', "Val d'Oise", 'Val de Marne',
    'Victoria', 'Virginia', 'Washington', 'Wyoming', 'Utah', 'Yveline'
])

product_category = st.selectbox("Select Product Category:", [
    'Accessories', 'Bikes', 'Clothing'
])

sub_category = st.selectbox("Select Sub Category:", [
    'Bike Racks', 'Bike Stands', 'Bottles and Cages', 'Caps', 'Cleaners',
    'Fenders', 'Gloves', 'Helmets', 'Hydration Packs', 'Jerseys',
    'Mountain Bikes', 'Road Bikes', 'Shorts', 'Socks', 'Tires and Tubes',
    'Touring Bikes', 'Vests'
])

product = st.selectbox("Select Product:", [
    'All-Purpose Bike Stand', 'AWC Logo Cap', 'Bike Wash - Dissolver',
    'Classic Vest, L', 'Classic Vest, M', 'Classic Vest, S',
    'Fender Set - Mountain', 'Half-Finger Gloves, L', 'Half-Finger Gloves, M',
    'Half-Finger Gloves, S', 'Hitch Rack - 4-Bike', 'HL Mountain Tire',
    'HL Road Tire', 'Hydration Pack - 70 oz.', 'LL Mountain Tire',
    'LL Road Tire', 'Long-Sleeve Logo Jersey, L', 'Long-Sleeve Logo Jersey, M',
    'Long-Sleeve Logo Jersey, S', 'Long-Sleeve Logo Jersey, XL',
    'ML Mountain Tire', 'ML Road Tire', 'Mountain Bottle Cage',
    'Mountain Tire Tube', 'Mountain-100 Black, 38', 'Mountain-100 Black, 42',
    'Mountain-100 Black, 44', 'Mountain-100 Black, 48', 'Mountain-100 Silver, 38',
    'Mountain-100 Silver, 42', 'Mountain-100 Silver, 44', 'Mountain-100 Silver, 48',
    'Mountain-200 Black, 38', 'Mountain-200 Black, 42', 'Mountain-200 Black, 46',
    'Mountain-200 Silver, 38', 'Mountain-200 Silver, 42', 'Mountain-200 Silver, 46',
    'Mountain-400-W Silver, 38', 'Mountain-400-W Silver, 40',
    'Mountain-400-W Silver, 42', 'Mountain-400-W Silver, 46',
    'Mountain-500 Black, 40', 'Mountain-500 Black, 42', 'Mountain-500 Black, 44',
    'Mountain-500 Black, 48', 'Mountain-500 Black, 52', 'Mountain-500 Silver, 40',
    'Mountain-500 Silver, 42', 'Mountain-500 Silver, 44', 'Mountain-500 Silver, 48',
    'Mountain-500 Silver, 52', 'Patch Kit/8 Patches', 'Racing Socks, L',
    'Racing Socks, M', 'Road Bottle Cage', 'Road Tire Tube',
    'Road-150 Red, 44', 'Road-150 Red, 48', 'Road-150 Red, 52',
    'Road-150 Red, 56', 'Road-150 Red, 62', 'Road-250 Black, 44',
    'Road-250 Black, 48', 'Road-250 Black, 52', 'Road-250 Black, 58',
    'Road-250 Red, 44', 'Road-250 Red, 48', 'Road-250 Red, 52',
    'Road-250 Red, 58', 'Road-350-W Yellow, 40', 'Road-350-W Yellow, 42',
    'Road-350-W Yellow, 44', 'Road-350-W Yellow, 48', 'Road-550-W Yellow, 38',
    'Road-550-W Yellow, 40', 'Road-550-W Yellow, 42', 'Road-550-W Yellow, 44',
    'Road-550-W Yellow, 48', 'Road-650 Black, 44', 'Road-650 Black, 48',
    'Road-650 Black, 52', 'Road-650 Black, 58', 'Road-650 Black, 60',
    'Road-650 Black, 62', 'Road-650 Red, 44', 'Road-650 Red, 48',
    'Road-650 Red, 52', 'Road-650 Red, 58', 'Road-650 Red, 60',
    'Road-650 Red, 62', 'Road-750 Black, 44', 'Road-750 Black, 48',
    'Road-750 Black, 52', 'Road-750 Black, 58', 'Short-Sleeve Classic Jersey, L',
    'Short-Sleeve Classic Jersey, M', 'Short-Sleeve Classic Jersey, S',
    'Short-Sleeve Classic Jersey, XL', 'Sport-100 Helmet, Black',
    'Sport-100 Helmet, Blue', 'Sport-100 Helmet, Red', 'Touring Tire',
    'Touring Tire Tube', 'Touring-1000 Blue, 46', 'Touring-1000 Blue, 50',
    'Touring-1000 Blue, 54', 'Touring-1000 Blue, 60', 'Touring-1000 Yellow, 46',
    'Touring-1000 Yellow, 50', 'Touring-1000 Yellow, 54', 'Touring-1000 Yellow, 60',
    'Touring-2000 Blue, 46', 'Touring-2000 Blue, 50', 'Touring-2000 Blue, 54',
    'Touring-2000 Blue, 60', 'Touring-3000 Blue, 44', 'Touring-3000 Blue, 50',
    'Touring-3000 Blue, 54', 'Touring-3000 Blue, 58', 'Touring-3000 Blue, 62',
    'Touring-3000 Yellow, 44', 'Touring-3000 Yellow, 50', 'Touring-3000 Yellow, 54',
    'Touring-3000 Yellow, 58', 'Touring-3000 Yellow, 62',
    "Women's Mountain Shorts, L", "Women's Mountain Shorts, M",
    "Women's Mountain Shorts, S", 'Water Bottle - 30 oz.'
])

order_quantity = st.number_input("Order Quantity", min_value=1)
unit_cost = st.number_input("Unit Cost")
unit_price = st.number_input("Unit Price")

if st.button("Predict"):

    if customer_gender == 'M':
        customer_gender = 0
    else:
        customer_gender = 1

    df = pd.DataFrame({
        "month": [month],
        "customer_age": [customer_age],
        "customer_gender": [customer_gender],
        "country": [country],
        "state": [state],
        "product_category": [product_category],
        "sub_category": [sub_category],
        "product": [product],
        "order_quantity": [order_quantity],
        "unit_cost": [unit_cost],
        "unit_price": [unit_price]
    })

    st.dataframe(df)

    with open("model.pkl", 'rb') as f:
        model = pickle.load(f)

    with open("preprocessor.pkl", 'rb') as f:
        preprocessor = pickle.load(f)

    new_df_scaled = preprocessor.transform(df)

    pred = model.predict(new_df_scaled)
    pred_val = pred[0]
    lower = pred_val - 50
    upper = pred_val + 50

    st.success(f"Predicted Profit: {pred_val:.2f}")
    st.info(f"Expected Range: {lower:.2f} to {upper:.2f}")