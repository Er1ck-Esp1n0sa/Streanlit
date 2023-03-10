import streamlit as st
import pandas as pd

st.title('Streanlit - Search name')

DATA_URL = ('dataset/dataset1.csv')

@st.cache
def load_data_byname(name):
    data = pd.read_csv(DATA_URL)
    filtered_data_byname = data[data['name'].str.contains(name)]

    return filtered_data_byname

myname = st.text_input('Name :')
if(myname):
    filterbyname = load_data_byname(myname)
    count_row = filterbyname.shape[0]
    st.dataframe(filterbyname)

    st.dataframe(filterbyname)