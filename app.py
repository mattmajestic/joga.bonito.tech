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

# Display tables in two columns
col1, col2 = st.columns(2)

col1.header("Goals per Game")
show_all_rows1 = st.checkbox("All Goals per Game Stats", key='goals_per_game')
if show_all_rows1:
    col1.table(goals_per_game_df)
else:
    col1.table(goals_per_game_df.head(10))

col1.header("Assists per Game")
show_all_rows2 = st.checkbox("All Assists per Game Stats", key='assists_per_game')
if show_all_rows2:
    col1.table(assists_per_game_df)
else:
    col1.table(assists_per_game_df.head(10))

col2.header("Total Goals")
show_all_rows3 = st.checkbox("All Total Goals Stats", key='total_goals')
if show_all_rows3:
    col2.table(total_goals_df)
else:
    col2.table(total_goals_df.head(10))

col2.header("Total Assists")
show_all_rows4 = st.checkbox("All Total Assists Stats", key='total_assists')
if show_all_rows4:
    col2.table(total_assists_df)
else:
    col2.table(total_assists_df.head(10))

# Display video
st.write("")
st.write("")
st.components.v1.html(f'<iframe width="560" height="315" src="https://www.youtube.com/embed/Xbl6PL3dgmE" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>', width=560, height=315, scrolling=False)
