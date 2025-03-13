import streamlit as st
import pandas as pd
import numpy as np

st.title("My first cloud app")

st.write("A simple DataFrame: ")

df=pd.DataFrame(np.random.randn(10,2),columns=['col1','col2'])
st.dataframe(df)