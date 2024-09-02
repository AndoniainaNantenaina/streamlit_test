import streamlit as st
import pandas as pd

data = pd.read_csv('E:/SIZEPLUS/streamlit_test/athletes.csv')
st.dataframe(data)
