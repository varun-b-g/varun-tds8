import streamlit as st
import pandas as pd

st.header("User input Parameters")

def user_input_features():
    first_number=st.number_input("FIRST_NUMBER", min_value=0.0, max_value=100000000.0)
    second_number=st.number_input("SECOND_NUMBER", min_value=0.0, max_value=100000000.0)

    data={'FIRST_NUMBER': first_number, 
        'SECOND_NUMBER': second_number
        }

    features=pd.DataFrame(data, index=[0])
    return data

data=user_input_features()
st.subheader("User Input Features")
st.header(data["FIRST_NUMBER"]+data["SECOND_NUMBER"])
