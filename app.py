import streamlit as st
import pandas as pd
import altair as alt
import requests
import gspread

# Set page config
st.set_page_config(page_title="Joga Bonito at Tech", page_icon=":soccer:")
st.title("Joga Bonito at Tech ⚽")
st.write("Analysis of player performance at Georgia Tech soccer games")

r = requests.get(f'https://docs.google.com/spreadsheet/ccc?key=1tPCnVRoxTh597qqxCGqZ5PpFVw8JhvJW1ODo0jH9lA0&output=csv')
open('dataset.csv', 'wb').write(r.content)
df = pd.read_csv('dataset.csv')

# Remove rownames
df = df.rename(columns={'Unnamed: 0': ''})
df.set_index('', inplace=True)

# Calculate metrics
df['Goals per Game'] = df['Goals'] / df['Games Played']
df['Assists per Game'] = df['Assists'] / df['Games Played']
df['G/A per Game'] = (df['Goals'] + df['Assists']) / df['Games Played']

# Sort the dataframes
goals_per_game_df = df[['Player Name', 'Goals per Game']].sort_values(by='Goals per Game', ascending=False)
assists_per_game_df = df[['Player Name', 'Assists per Game']].sort_values(by='Assists per Game', ascending=False)
total_goals_df = df[['Player Name', 'Goals']].sort_values(by='Goals', ascending=False)
total_assists_df = df[['Player Name', 'Assists']].sort_values(by='Assists', ascending=False)

# Display tables
st.write("## Goals per Game")
st.table(goals_per_game_df)

st.write("## Assists per Game")
st.table(assists_per_game_df)

st.write("## Total Goals")
st.table(total_goals_df)

st.write("## Total Assists")
st.table(total_assists_df)

# Display video
st.write("")
st.write("")
st.components.v1.html(f'<iframe width="560" height="315" src="https://www.youtube.com/embed/Xbl6PL3dgmE" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>', width=560, height=315, scrolling=False)
