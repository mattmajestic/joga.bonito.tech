import streamlit as st
import pandas as pd
import altair as alt

# Set the app title and description
st.set_page_config(page_title="Joga Bonito at Tech", page_icon=":soccer:", layout="wide")
st.title("Joga Bonito at Tech")
st.write("Analysis of player performance at Georgia Tech soccer games")

# Load the data
data = pd.read_csv("tech-stats.csv")

# Create the bar chart of total goals
total_goals = data.groupby("Player")["Goals"].sum().reset_index()
bar_chart = alt.Chart(total_goals).mark_bar().encode(
    x="Player:O",
    y="Goals:Q",
    tooltip=["Player", "Goals"]
).properties(width=400, height=300)

# Create the line chart of player performance
line_chart = alt.Chart(data).mark_line().encode(
    x="Date:T",
    y="Goals:Q",
    color="Player:N",
    tooltip=["Date", "Player", "Goals", "Assists"]
).properties(width=400, height=300)

# Display the charts in two columns
col1, col2 = st.columns(2)
col1.write(bar_chart)
col2.write(line_chart)
