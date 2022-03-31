from re import S
from tracemalloc import Statistic
import streamlit as st
import pandas as pd
import preprocessor
import helper
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.figure_factory as ff

df = pd.read_csv('athlete_events.csv')
region_df = pd.read_csv('noc_regions.csv')

df = df[df['Season'] == 'Summer']
df = df.merge(region_df, on='NOC', how='left')
df = pd.concat([df, pd.get_dummies(df['Medal'])], axis=1)

def app():
    st.sidebar.header('Medal Tally')
    years, country = helper.country_year_list(df)
    st.sidebar.info('This department will give you the information of the Medals Countries achieved over the years')
    st.sidebar.info('Select Your Year')
    selected_year = st.sidebar.selectbox('Select Year', years)
    st.sidebar.info('Select Your Country')
    selected_country = st.sidebar.selectbox('Select Country', country)
    medal_tally = helper.fetch_medal_tally(df, selected_year, selected_country)

    if selected_year == 'Overall' and selected_country == 'Overall':
        st.title('Overall Medal Tally')
    if selected_year != 'Overall' and selected_country == 'Overall':
        st.title('Overall performance in ' + str(selected_year))
    if selected_year == 'Overall' and selected_country != 'Overall':
        st.title('Overall performance for ' + str(selected_country))
    if selected_year != 'Overall' and selected_country != 'Overall':
        st.title('Medal Tally for ' + str(selected_country) +
                 ' in ' + str(selected_year))
    st.dataframe(medal_tally)
