import streamlit as st
import pandas as pd
import altair as alt

# Set page config
st.set_page_config(page_title="Joga Bonito at Tech", page_description="Analysis of player performance at Georgia Tech soccer games", layout="wide")

# Load data
df = pd.read_csv("tech-stats.csv")

# Define chart functions
def goals_over_time_chart(data):
    chart = alt.Chart(data).mark_line().encode(
        x="Date:T",
        y="Goals:Q",
        color="Player:N"
    ).properties(
        height=300
    )
    return chart

def goals_per_match_chart(data):
    chart = alt.Chart(data).mark_bar().encode(
        y="Player:N",
        x="Goals_per_match:Q"
    ).properties(
        height=300
    )
    return chart

def assists_over_time_chart(data):
    chart = alt.Chart(data).mark_line().encode(
        x="Date:T",
        y="Assists:Q",
        color="Player:N"
    ).properties(
        height=300
    )
    return chart

def assists_per_match_chart(data):
    chart = alt.Chart(data).mark_bar().encode(
        y="Player:N",
        x="Assists_per_match:Q"
    ).properties(
        height=300
    )
    return chart

# Compute derived data
df["Date"] = pd.to_datetime(df["Date"])
df["Goals_per_match"] = df["Goals"] / df["GameTime"]
df["Assists_per_match"] = df["Assists"] / df["GameTime"]

# Create charts
col1, col2 = st.columns(2)
with col1:
    st.write("# Goals over Time")
    st.altair_chart(goals_over_time_chart(df))
    st.write("# Goals per Match")
    st.altair_chart(goals_per_match_chart(df))
with col2:
    st.write("# Assists over Time")
    st.altair_chart(assists_over_time_chart(df))
    st.write("# Assists per Match")
    st.altair_chart(assists_per_match_chart(df))