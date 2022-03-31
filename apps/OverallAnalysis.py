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
    st.title('Overall Analysis')
    st.sidebar.info('This department will give you the information of the participation of the nations,events held and athletes over the years')
    st.sidebar.info('This department will also give you the information of the most successful players for a particular country')
    editions = df['Year'].unique().shape[0] - 1
    cities = df['City'].unique().shape[0]
    events = df['Sport'].unique().shape[0]
    players = df['Name'].unique().shape[0]
    nations = df['region'].unique().shape[0]
    
    st.title('Top Statistics')
    col1, col2, col3 = st.columns(3)
    with col1:
        st.header('Editions')
        st.title(editions)
    with col2:
        st.header('Hosts')
        st.title(cities)
    with col3:
        st.header('Sports')
        st.title(events)

    col1, col2, col3 = st.columns(3)
    with col1:
        st.header('Events')
        st.title(events)
    with col2:
        st.header('Nations')
        st.title(nations)
    with col3:
        st.header('Athletes')
        st.title(players)
        
    nations_over_time = helper.data_over_time(df, 'region')
    fig = px.line(nations_over_time, x='Edition', y='region')
    st.title('Participating Nations Over the Years')
    st.plotly_chart(fig)
    
    events_over_time = helper.data_over_time(df, 'Event')
    fig = px.line(events_over_time, x='Edition', y='Event')
    st.title('Events Over the Years')
    st.plotly_chart(fig)

    athlete_over_time = helper.data_over_time(df, 'Name')
    fig = px.line(athlete_over_time, x='Edition', y='Name')
    st.title('Athletes Over the Years')
    st.plotly_chart(fig)

    st.title('No. of Events Over Time(Every Sport)')
    fig, ax = plt.subplots(figsize=(20, 30))
    x = df.drop_duplicates(['Year', 'Sport', 'Event'])
    x = x.pivot_table(index='Sport', columns='Year', values='Event',
                  aggfunc='count').fillna(0).astype(int)
    ax = sns.heatmap(x, annot=True)
    st.pyplot(fig)

    st.title('Most Successful Players in particular')
    sports_list = df['Sport'].unique().tolist()
    sports_list.sort()
    selected_sport = st.selectbox('Select a Sport', sports_list)
    x = helper.most_successful(df, selected_sport)
    st.dataframe(x)