import pandas as pd
import streamlit as st
import datetime

titanic_link = 'dataset/titanic.csv'

titanic_data = pd.read_csv(titanic_link)

# Create the title for the web app
st.title("Mi primera aplicacion con Streamlit")
sidebar = st.sidebar
sidebar.title("Esto es un Sinderbatr")
sidebar.write("Puedes agregar cualquier elemento a la barra lateral.")

# Give user the current date
today = datetime.date.today()
today_date = st.date_input('Current date', today)
st.success('Current date: `%s`' % (today_date))

# Display the content of the dataset if checkbox is true
st.header("Dataset")
agree = sidebar.checkbox("Mostar los datos del Dataset ")
if agree:
    st.dataframe(titanic_data)

# Select the embark town of the passanger and then display the dataset with this selection
selected_town = sidebar.radio("Selecciona la ciudad de embarque",
titanic_data['embark_town'].unique())
st.write("Ciudad de embarque seleccionada:", selected_town)
st.write(titanic_data.query(f"""embark_town==@selected_town"""))
st.markdown("___")

# Select a range of the fare and then display the dataset with this selection
optionals = sidebar.expander("Opciones de configuracion", True)
fare_min = optionals.slider(
    "Tarifa minima",
    min_value=float(titanic_data['fare'].min()),
    max_value=float(titanic_data['fare'].max())
)
fare_max = optionals.slider(
    "Tarifa maxima ",
    min_value=float(titanic_data['fare'].min()),
    max_value=float(titanic_data['fare'].max())
)
subset_fare = titanic_data[(titanic_data['fare'] <= fare_max) &
(fare_min <= titanic_data['fare'])]
sidebar.write(f"Número de registros con tarifa intermedia {fare_min} y {fare_max}: {subset_fare.shape[0]}")