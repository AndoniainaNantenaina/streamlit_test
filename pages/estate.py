import streamlit as st
import pandas as pd

data = pd.read_csv('E:/SIZEPLUS/streamlit_test/sample_data.csv')

conditions_value = data.get('Condition')
conditions_value = set(conditions_value)
conditions_value = list(conditions_value)
conditions_value.append('All')

condition_filter = st.selectbox('Filter by condition', list(conditions_value))

if condition_filter != 'All':
    data = data[data['Condition'] == condition_filter]
else:
    data = data

st.map(
    data,
    latitude='Latitude',
    longitude='Longitude'
)

st.dataframe(data, width=1200)
