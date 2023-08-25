
import joblib
import streamlit as st

st.title("Welcome to my Iris flower Prediction App")
st.sidebar.header("Abideen Model Deployment")

#loading the model
model = joblib.load("iris_model.pkl")


sepal_lengt = st.number_input("Enter the sepal_lengt:")
sepal_width = st.number_input("Enter the sepal_width:")
petal_length = st.number_input("Enter the petal_length:")
petal_width = st.number_input("Enter the petal_width:")



prediction = model.predict([[sepal_lengt, sepal_width, petal_length, petal_width]])

if st.button("Get a prediction"):
    st.success(prediction)
else:
    st.write("You are yet to put values for prediction")

