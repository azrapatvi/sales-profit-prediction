import streamlit as st
import pandas as pd
import pickle

st.title("Sales Profit Prediction")

month=st.selectbox("Select Month:",['January','February','March','April','May','June','July','August','September','October','November','December'])

customer_age=st.number_input("Customer Age:", min_value=10, max_value=100)

customer_gender=st.selectbox("Select Gender:",['M','F'])

country = st.text_input("Country")
state = st.text_input("State")

product_category = st.text_input("Product Category")
sub_category = st.text_input("Sub Category")
product = st.text_input("Product Name")

order_quantity = st.number_input("Order Quantity", min_value=1)
unit_cost = st.number_input("Unit Cost")
unit_price = st.number_input("Unit Price")

if st.button("Predict"):

    if customer_gender=='M':
        customer_gender=0
    else:
        customer_gender=1

    df=pd.DataFrame({
        "month":[month],
        "customer_age":[customer_age],
        "customer_gender":[customer_gender],
        "country":[country],
        "state":[state],
        "product_category":[product_category],
        "sub_category":[sub_category],
        "product":[product],
        "order_quantity":[order_quantity],
        "unit_cost":[unit_cost],
        "unit_price":[unit_price]
    })

    st.dataframe(df)

    with open("model.pkl",'rb')as f:
        model=pickle.load(f)
    
    with open("preprocessor.pkl",'rb') as f:
        preprocessor=pickle.load(f)

    
    new_df_scaled=preprocessor.transform(df)

    pred=model.predict(new_df_scaled)
    pred_val = pred[0]
    lower = pred_val - 50   # example lower bound
    upper = pred_val + 50   # example upper bound

    st.success(f"Predicted Profit: {pred_val}")
    st.info(f"Expected Range: {lower} to {upper}")


