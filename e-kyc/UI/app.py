import streamlit as st
import requests
import time

# FastAPI backend URL
FASTAPI_URL = "http://fastapi-backend:8000"

st.title("Addition Task")

# Input fields for numbers
num1 = st.number_input("Enter the first number", value=0.0, step=1.0)
num2 = st.number_input("Enter the second number", value=0.0, step=1.0)

# Submit button
if st.button("Add Numbers"):
    # Send request to FastAPI
    with st.spinner("Submitting task..."):
        response = requests.post(f"{FASTAPI_URL}/add", json={"num1": num1, "num2": num2})
        if response.status_code == 200:
            task_id = response.json().get("task_id")
            st.success(f"Task submitted! Task ID: {task_id}")
            
            # Poll for result
            st.info("Waiting for the result...")
            while True:
                result_response = requests.get(f"{FASTAPI_URL}/result/{task_id}")
                result_data = result_response.json()
                if result_data["status"] == "SUCCESS":
                    st.success(f"Result: {result_data['result']}")
                    break
                elif result_data["status"] == "FAILURE":
                    st.error(f"Task failed: {result_data['error']}")
                    break
                time.sleep(2)
        else:
            st.error("Failed to submit task!")
