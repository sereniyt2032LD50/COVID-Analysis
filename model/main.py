# """ Covid Data Analysis, to demonstrate my understanding of EDA, data vizualisation and deployment
# The model in this case will be where I will do the data exploration and analysis  """

# import pandas as pd
# import numpy as np

# data = pd.read_csv("data\vaccination-data.csv")
# data.head()


# """ 
#  Covid Data Analysis, to demonstrate my understanding of EDA, data vizualisation and deployment
# The model in this case will be where I will do the data exploration and analysis  """

# # --- Importing required dependencies

# import streamlit as st
# from PIL import Image


# st.set_page_config(page_title="Covid-19 Analysis", page_icon="hospital")
# st.title(':red[Covid Data Analysis]')
# st.sidebar.success("Select page above")
# st.write(""" 
# In 2020, the world was brought to its knees; a pandemic. The last one was almost 100 years ago
# in 1920. The first appearance of the disease originated from wuhan in mainland china and gradually
# to other the whole of Asia and other continents
#  """)

# st.subheader('Country Statistics')

# # df = pd.read_csv(r'C:\Users\HP\Documents\python_world\COVID-Analysis\data\vaccination-metadata.csv')
# # st.dataframe(df)

# """

# import plotly.express as px


# # data = pd.read_csv


# gapminder = px.data.gapminder()
# #print(gapminder.head(15))
# fig = px.choropleth(gapminder, 
#                     locations = "iso_alpha",
#                     color = "lifeExp",
#                     scope = "world",
#                     animation_frame = "year")

# fig.show()

import streamlit as st
import folium
from streamlit_folium import st_folium

map = folium.Map()
st_map = st_folium(map, width=700, height=450)


# m = folium.Map()
# m.save('footprint.html')

# APP_TITLE = "COVID_19 Data Analysis"
# APP_SUB_TITLE = "Detail Vaccine analysis"


# def main():
#     st.set_page_config(APP_TITLE)
#     st.title(APP_TITLE)
#     st.caption(APP_SUB_TITLE)



# if __name__ == "__main__":
#     main()