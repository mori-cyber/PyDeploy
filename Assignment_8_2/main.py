import numpy as np
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt



# Function to read CSV file
def read_csv_file(file):
    df = pd.read_csv(file)
    
    return df

# Main function to run the Streamlit app
def main():
    st.title('CSV File Reader')

    # Upload CSV file
    uploaded_file = st.file_uploader("/home/morteza/Desktop/my_python_project/Assignment_8_2/housing.csv", type=["csv"])

    if uploaded_file is not None:
        st.write("File uploaded successfully!")

        # Call function to read CSV file
        df = read_csv_file(uploaded_file)
        st.write(df.head())
        # Display DataFrame
        # data=df['total_rooms', 'total_median_age']
        st.bar_chart(df, x="total_rooms", y="housing_median_age", color="#ffaa0088")
        
        with st.sidebar:
     #process   
                st.subheader("Dataset Information:")
                st.write(df.describe())
                st.success(" The housing dataset usually contains information about various attributes of houses, which can be used for tasks such as regression analysis, predicting house prices, or understanding housing market trends.")
                

# Run the app
if __name__ == "__main__":
    main()
    