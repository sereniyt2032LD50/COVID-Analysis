#-----Importing dependencies
import pandas as pd
import streamlit as st
import folium
from streamlit_folium import st_folium


st.set_page_config(page_title="Covid Data Analysis", page_icon="hospital")
st.title("COVID-19 Data Analysis")
st.caption('An indepth analysis: Cases, Deaths, Recovered, Vaccinnations')
  
st.sidebar.success("Select page above")


Covid_19_global = pd.read_csv(r'C:\Users\HP\Documents\python_world\COVID-Analysis\data\vaccination-data.csv')
#countries_json_url = ("https://raw.githubusercontent.com/python-visualization/folium/master/examples/data/world-countries.json")
countries_json_url = (r'C:\Users\HP\Documents\python_world\COVID-Analysis\data\countries_json.json')

map = folium.Map(location=(30, 10), zoom_start=1.2, tiles="cartodb positron")
folium.Choropleth(
    geo_data = countries_json_url,
    data = Covid_19_global,
    columns = ("COUNTRY", "TOTAL_VACCINATIONS"),
    key_on = "feature.properties.name",
    highlight=True,
    fill_color = "RdYlGn_r",
    fill_opacity = 0.8,
    line_opacity = 0.3,
    nan_fill_color = "white",
    legend_name = "total vaccine per country",
).add_to(map)
folium.features.GeoJson(countries_json_url, 
       name = 'Countries', popup=folium.features.GeoJsonPopup(field =["name"])).add_to(map)

st_map = st_folium(map, width= 900, height=450)

region_list = list(Covid_19_global['WHO_REGION'].unique())
region_list.sort()
region = st.sidebar.selectbox('WHO_REGION', region_list, len(region_list)-1)

# COUNTRY = ''
# if st_map['last_active_drawing']:
#     COUNTRY = st_map['last_active_drawing']['properties']['name']

# return COUNTRY

st.write("""
         Early 2020, the world was force to a halt by a global pandemic. The last one was in 1920.
         Covid started in wuhan, a small village in China. 
         As of the 7 of July, the WHO stop collecting covid-19 data around the world.

         - The map visualizes the COVID vaccine 19 report publish by the WHO as of June 2023
         - Choropleth of cases cumulated global and death cumulated global - Follium

         - Choropleth of 
         
         """)