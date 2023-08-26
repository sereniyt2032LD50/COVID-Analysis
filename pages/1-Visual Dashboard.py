#--- Import dependencies

import pandas as pd
import streamlit as st
import folium
from streamlit_folium import st_folium

st.caption('A visual of the Vaccine Use; companies, quantities etc')

#load Data
df = pd.read_csv(r'C:\Users\HP\Documents\python_world\COVID-Analysis\data\vaccination-metadata.csv')
st.write('vaccination-metadata')
st.dataframe(df.head(10))

df['COMPANY_NAME'].fillna('Missing', inplace=True)
companies_list = list(df['COMPANY_NAME'].unique())
companies_list.sort()
Company = st.sidebar.selectbox('COMPANY_NAME', companies_list, len(companies_list)-1)

st.write(df['COMPANY_NAME'].value_counts())

# companies_list.sort()
# company = st.sidebar.selectbox('COMPANY_NAME', companies_list, len(companies_list)-1)
# for company in companies_list:
#     st.markdown(company)
# The column paramater in the folium or choropleth map takes the key and the value.

#For my first map, key and value were as follow; country, Total vaccination
#For my second map key and value can be as follow; country, Total Cases
#For my third map key and value will be as follow; country, Total Deaths
#For my fourth map key and value will be as follows; country