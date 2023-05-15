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
df['Date'] = pd.to_datetime(df['Date'])

# Load data
# df = pd.read_csv("tech-stats.csv")

# Compute derived data
df["Goals_per_game"] = df["Goals"] / df.groupby("Player")["Date"].transform("nunique")
df["Assists_per_game"] = df["Assists"] / df.groupby("Player")["Date"].transform("nunique")
total_goals = df.groupby("Player")["Goals"].sum()
total_assists = df.groupby("Player")["Assists"].sum()

# Display tables
st.write("## Goals per Game")
goals_per_game_table = df.groupby("Player")["Goals_per_game"].mean().reset_index()
st.table(goals_per_game_table)

st.write("## Assists per Game")
assists_per_game_table = df.groupby("Player")["Assists_per_game"].mean().reset_index()
st.table(assists_per_game_table)

st.write("## Total Goals")
st.table(total_goals)

st.write("## Total Assists")
st.table(total_assists)

# Display video
st.write("")
st.write("")
st.components.v1.html(f'<iframe width="560" height="315" src="https://www.youtube.com/embed/Xbl6PL3dgmE" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>', width=560, height=315, scrolling=False)