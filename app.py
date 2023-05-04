import streamlit as st
import pandas as pd
import altair as alt

# Set page title and favicon
st.set_page_config(page_title="Joga Bonito at Tech", page_icon=":soccer:")

# Load data from CSV file
data = pd.read_csv("tech-stats.csv")

# Convert date column to datetime format
data["Date"] = pd.to_datetime(data["Date"])

# Set up sidebar
st.sidebar.title("Joga Bonito at Tech")
st.sidebar.markdown("Analysis of player performance at Georgia Tech soccer games")

# Define function to create goals over time chart
def create_goals_over_time_chart(data):
    chart = alt.Chart(data).mark_line().encode(
        x="Date:T",
        y="Goals:Q",
        color="Player:N"
    ).properties(
        width=350,
        height=200
    )
    return chart

# Define function to create goals per match chart
def create_goals_per_match_chart(data):
    chart_data = data.groupby("Player").agg({"Goals": "sum", "GameTime": "sum"})
    chart_data["Goals per Match"] = chart_data["Goals"] / chart_data["GameTime"]
    chart = alt.Chart(chart_data.reset_index()).mark_bar().encode(
        x="Player:N",
        y="Goals per Match:Q",
        color="Player:N"
    ).properties(
        width=350,
        height=200
    )
    return chart

# Define function to create assists per match chart
def create_assists_per_match_chart(data):
    chart_data = data.groupby("Player").agg({"Assists": "sum", "GameTime": "sum"})
    chart_data["Assists per Match"] = chart_data["Assists"] / chart_data["GameTime"]
    chart = alt.Chart(chart_data.reset_index()).mark_bar().encode(
        x="Player:N",
        y="Assists per Match:Q",
        color="Player:N"
    ).properties(
        width=350,
        height=200
    )
    return chart

# Define function to create assists over time chart
def create_assists_over_time_chart(data):
    chart = alt.Chart(data).mark_line().encode(
        x="Date:T",
        y="Assists:Q",
        color="Player:N"
    ).properties(
        width=350,
        height=200
    )
    return chart

# Create goals over time chart
st.subheader("Goals over Time")
goals_over_time_chart = create_goals_over_time_chart(data)
st.altair_chart(goals_over_time_chart)

# Create goals per match chart
st.subheader("Goals per Match")
goals_per_match_chart = create_goals_per_match_chart(data)
st.altair_chart(goals_per_match_chart)

# Create assists per match chart
st.subheader("Assists per Match")
assists_per_match_chart = create_assists_per_match_chart(data)
st.altair_chart(assists_per_match_chart)

# Create assists over time chart
st.subheader("Assists over Time")
assists_over_time_chart = create_assists_over_time_chart(data)
st.altair_chart(assists_over_time_chart)

# Add some padding to the layout
st.markdown("<style>div.stApp { padding: 2rem; }</style>", unsafe_allow_html=True)
