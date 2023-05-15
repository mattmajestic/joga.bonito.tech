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
df['Date'] = pd.to_datetime(df['Date'])

# Load data
# df = pd.read_csv("tech-stats.csv")

# Compute derived data
df["Goals_per_game"] = df["Goals"] / df.groupby("Player")["Date"].transform("nunique")
df["Assists_per_game"] = df["Assists"] / df.groupby("Player")["Date"].transform("nunique")
total_goals = df.groupby("Player")["Goals"].sum()
total_assists = df.groupby("Player")["Assists"].sum()

# Display tables
st.write("## Per Game Goals and Assists")
per_game_table = pd.DataFrame({
    "Player": df["Player"].unique(),
    "Goals per Game": df.groupby("Player")["Goals_per_game"].mean(),
    "Assists per Game": df.groupby("Player")["Assists_per_game"].mean()
})
per_game_table = per_game_table.sort_values("Goals per Game", ascending=False)  # Sort by Goals per Game
per_game_table.reset_index(drop=True, inplace=True) 
st.table(per_game_table)

st.write("## Total Goals and Assists")
total_table = pd.DataFrame({
    "Player": total_goals.index,
    "Total Goals": total_goals,
    "Total Assists": total_assists
})
total_table = total_table.sort_values("Total Goals", ascending=False)  # Sort by Total Goals
total_table.reset_index(drop=True, inplace=True)
st.table(total_table)

# Display video
st.write("")
st.write("")
st.components.v1.html(f'<iframe width="560" height="315" src="https://www.youtube.com/embed/Xbl6PL3dgmE" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>', width=560, height=315, scrolling=False)
