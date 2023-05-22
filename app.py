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
show_all_rows = st.button("Show All Player Stats")

if show_all_rows:
    st.dataframe(goals_per_game_df, height=500)
    st.dataframe(assists_per_game_df, height=500)
    st.dataframe(total_goals_df, height=500)
    st.dataframe(total_assists_df, height=500)
else:
    st.dataframe(goals_per_game_df.head(10), height=500)
    st.dataframe(assists_per_game_df.head(10), height=500)
    st.dataframe(total_goals_df.head(10), height=500)
    st.dataframe(total_assists_df.head(10), height=500)

# Display video
st.write("")
st.write("")
st.components.v1.html(f'<iframe width="560" height="315" src="https://www.youtube.com/embed/Xbl6PL3dgmE" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>', width=560, height=315, scrolling=False)
