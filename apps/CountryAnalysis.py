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
     st.sidebar.title('Country-wise Analysis')
     country_list = df['region'].dropna().unique().tolist()
     country_list.sort()
     selected_country = st.sidebar.selectbox('Search Country', country_list)
     country_df = helper.yearwise_medal_tally(df,selected_country)
     fig = px.line(country_df, x='Year', y='Medal')
     st.title(selected_country + ' ' + 'Medal Tally Over the Years')
     st.plotly_chart(fig)
    
     pt = helper.country_wise_heatmap(df,selected_country)
     fig, ax = plt.subplots(figsize=(20,40))
     st.title(selected_country+ ' '+ 'heatmap')
     ax = sns.heatmap(pt, annot=True)
     st.pyplot(fig)

     st.title('Top 10 Athletes of '+ ' '+ selected_country)
     top10 = helper.most_successful_countrywise(df,selected_country)
     st.table(top10)
