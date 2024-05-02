import streamlit as st
import datetime
st.title("My Streamlit App")

col1, col2 = st.columns(2)

with st.sidebar:
    sagree =st.checkbox("this is cheack box")
    value = st.slider("select a range of values", 0.0,100.0, (25.0,75.0))
    d = st.date_input("When's your birthday", datetime.date(2019, 7, 6))




with col1:

        st.write("hello world")

        my_btn=st.button("click me")

        if my_btn:
            st.write("salam")
        else:
            st.write("good by")

        st.text_input("first name")
        st.text_input("last name")

       
with col2:
        weight =st.number_input("Enter your wieght (kg)")
        height = st.number_input("Enter your height (cm)")

        my_calculate_bmi = st.button("Calculate BMI") 

        if my_calculate_bmi:
            bmi = weight / ((height/100)**2)
            st.info(bmi)
            if bmi < 18.5:
                st.write("thin")
            elif 18.5 < bmi < 25:
                st.write("very goo")
            elif 25 < bmi < 30:
                st.write("you are fat")

st.warning("this is new row")
