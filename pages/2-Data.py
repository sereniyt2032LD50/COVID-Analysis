import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image


""" 
Vaccine company - World distribution 
Vaccine used by countries - world distribution
Mapping cumulative death with vaccine use and number of doses administered
Mapping data from two dataframes and analysing the group data

"""

st.write("In this section, we will try to understand the vaccine utilisation by country")

# data = pd.read_csv("data\vaccination-data.csv")
# data.head()

# #Can you create a function to load the data. See if it is possible
# def load_data(name):
#     df =  pd.read_csv(name)
#     return df

# load_data()


st.subheader('Vaccine Analysis')

df = pd.read_csv(r'C:\Users\HP\Documents\python_world\COVID-Analysis\data\vaccination-metadata.csv')
st.write('vaccination-metadata')
st.write(df.shape)
st.dataframe(df.head(10))


# """ 
# df.groupby(['COMPANY_NAME']).group.keys()
# df.groupby(['COMPANY_NAME']).get_group('Moderna')
# df.groupby(['COMPANY_NAME','PRODUCT_NAME']).value_counts().plot()
# A map view of the vaccine distribution
# A plot of the world vaccine distribution by company; pie graph
# df.groupby('ISO3')

# df['COMPANY_NAME'].value_count()

# """


df1 = pd.read_csv(r'C:\Users\HP\Documents\python_world\COVID-Analysis\data\vaccination-data.csv')
st.write('Vaccination-data')
st.write(df1.shape)
st.dataframe(df1.head(10))


df2 = pd.read_csv(r'C:\Users\HP\Documents\python_world\COVID-Analysis\data\WHO-COVID-19-global-data.csv')
st.write('WHO-COVID-19-global-data')
st.write(df2.shape)
st.dataframe(df2.head(10))


df3 = pd.read_csv(r'C:\Users\HP\Documents\python_world\COVID-Analysis\data\WHO-COVID-19-global-table-data.csv')
st.write('WHO-COVID-19-global-table-data')
st.write(df3.shape)
st.dataframe(df3.head(50))

st.write(df3.columns)

merged_df = pd.merge(df, df1)
st.write('vaccination-metadata - Vaccination-data')
st.write(merged_df.shape)
st.dataframe(merged_df.head())
st.write(merged_df.keys())