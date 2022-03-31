import numpy as numpy
import pandas as pd
import streamlit as st


def preprocess(df, region_df):

    df = df[df['Season'] == 'Summer']
    df = df.merge(region_df, on='NOC', how='left')
    df = pd.concat([df, pd.get_dummies(df['Medal'])], axis=1)
    return df
