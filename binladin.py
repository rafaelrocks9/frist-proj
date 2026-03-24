import streamlit as st
st.title("my first streamlit app")
st.write("hello first web application using streamlit")
import pandas as pd

data = {
            "Name": ["rafael", "viggy", "rachit", "Dhruv"],
            "Age": [25, 30, 35, 40],
            "City": ["kodagu", "malyali", "bhopali", "up"],
            "Salary": [50000, 60000, 75000, 80000]
        }

df = pd.DataFrame(data)
print(df)
