import streamlit as st
import pandas as pd
import altair as alt
import requests
import gspread

# Set page config
st.set_page_config(page_title="Joga Bonito at Tech", page_icon=":soccer:")
st.title("Joga Bonito at Tech")
st.write("Analysis of player performance at Georgia Tech soccer games")

r = requests.get(f'https://docs.google.com/spreadsheet/ccc?key=1tPCnVRoxTh597qqxCGqZ5PpFVw8JhvJW1ODo0jH9lA0&output=csv')
open('dataset.csv', 'wb').write(r.content)
df = pd.read_csv('dataset.csv')

# Load data
# df = pd.read_csv("tech-stats.csv")

# Compute derived data
df["Date"] = pd.to_datetime(df["Date"])
df["Goals_per_match"] = df["Goals"] / df.groupby("Player")["Date"].transform("nunique")
df["Assists_per_match"] = df["Assists"] / df.groupby("Player")["Date"].transform("nunique")

def create_goals_over_time_chart(df):
    chart = alt.Chart(df).mark_line().encode(
        x='Date:T',
        y='Goals:Q',
        color='Player:N'
    ).properties(
        height=400,  # <-- double the height
        width=400,  # <-- double the width
        title='Goals Over Time'
    )
    return chart

def create_goals_per_player_chart(df):
    chart = alt.Chart(df).mark_bar().encode(
        x='Player:N',
        y='Goals:Q'
    ).properties(
        height=400,
        width=400,
        title='Goals per Player'
    )
    return chart

def create_assists_per_player_chart(df):
    chart = alt.Chart(df).mark_bar().encode(
        x='Player:N',
        y='Assists:Q'
    ).properties(
        height=400,
        width=400,
        title='Assists per Player'
    )
    return chart

def create_assists_over_time_chart(df):
    chart = alt.Chart(df).mark_line().encode(
        x='Date:T',
        y='Assists:Q',
        color='Player:N'
    ).properties(
        height=400,  # <-- double the height
        width=400,  # <-- double the width
        title='Assists Over Time'
    )
    return chart

# Create charts
goals_over_time_chart = create_goals_over_time_chart(df)
goals_per_player_chart = create_goals_per_player_chart(df)
assists_per_player_chart = create_assists_per_player_chart(df)
assists_over_time_chart = create_assists_over_time_chart(df)

# Create charts
col1, col2 = st.columns(2)
with col1:
    st.write("## Goals over Time")
    st.altair_chart(goals_over_time_chart)
    st.write("## Assists per Player")
    st.altair_chart(assists_per_player_chart)
with col2:
    st.write("## Assists over Time")
    st.altair_chart(assists_over_time_chart)
    st.write("## Goals per Player")
    st.altair_chart(goals_per_player_chart)

# Display video below charts
st.write("")
st.write("")
st.components.v1.html(f'<iframe width="560" height="315" src="https://www.youtube.com/embed/Xbl6PL3dgmE" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>', width=560, height=315, scrolling=False)
