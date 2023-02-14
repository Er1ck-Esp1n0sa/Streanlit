import pandas as pd
import streamlit as st

st.title('Streamlit con atributo cache')

DATA_URL  = ( 'dataset/dataset1.csv')

@st.cache
def load_data(nrows):
    data = pd.read_csv(DATA_URL,nrows=nrows)
    return data

data_load_state = st.text('loading data. . .')
data = load_data(501)
data_load_state.text("Done! (using st.cache)")

st.dataframe(data)