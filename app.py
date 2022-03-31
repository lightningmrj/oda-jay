import streamlit as st
from multiapp import MultiApp
from apps import AthleteAnalysis, CountryAnalysis, MedalTally, OverallAnalysis # import your app modules here
import pandas as pd
import time
import numpy as np


app = MultiApp()

df = pd.read_csv('athlete_events.csv')
region_df = pd.read_csv('noc_regions.csv')

st.title('Olympics Data Analysis App')

st.header('This is an Analytical App which gives you the insights of the Olympics data from 1896 to 2016')

st.sidebar.title('Olympics Analysis')
st.sidebar.info('This is a additional container to statify your perosnal search')

# Add all your application here
app.add_app("Medal Tally", MedalTally.app)
app.add_app("Overall Analysis", OverallAnalysis.app)
app.add_app("Country-wise Analysis", CountryAnalysis.app)
app.add_app("Athlete wise Analysis", AthleteAnalysis.app)
# The main app

with st.spinner('Wait for it...'):
    time.sleep(2)
app.run()
