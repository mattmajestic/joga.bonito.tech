import streamlit as st
import pandas as pd
import altair as alt

# Set page config
st.set_page_config(page_title="Joga Bonito at Tech", page_icon=":soccer:")
st.title("Joga Bonito at Tech")
st.write("Analysis of player performance at Georgia Tech soccer games")

# Load data
df = pd.read_csv("tech-stats.csv")

def create_goals_over_time_chart(df):
    chart = alt.Chart(df).mark_line().encode(
        x='Date:T',
        y='Goals:Q'
    ).properties(
        height=400,
        width=400,
        title='Goals Over Time'
    )
    return chart

def create_goals_per_match_chart(df):
    goals_per_match = df.groupby(['Player', 'Date'])['Goals'].sum().reset_index()
    chart = alt.Chart(goals_per_match).mark_bar().encode(
        x='Date:T',
        y='Goals:Q',
        color='Player:N'
    ).properties(
        height=400,
        width=400,
        title='Goals per Match'
    )
    return chart

def create_assists_per_match_chart(df):
    assists_per_match = df.groupby(['Player', 'Date'])['Assists'].sum().reset_index()
    chart = alt.Chart(assists_per_match).mark_bar().encode(
        x='Date:T',
        y='Assists:Q',
        color='Player:N'
    ).properties(
        height=400,
        width=400,
        title='Assists per Match'
    )
    return chart

def create_assists_over_time_chart(df):
    chart = alt.Chart(df).mark_line().encode(
        x='Date:T',
        y='Assists:Q'
    ).properties(
        height=400,
        width=400,
        title='Assists Over Time'
    )
    return chart

# Compute derived data
df["Date"] = pd.to_datetime(df["Date"])
df["Goals_per_match"] = df.groupby(['Player', 'Date'])['Goals'].transform('sum') / df.groupby(['Player', 'Date'])['Date'].transform('nunique')

# Create charts
col1, col2 = st.columns(2)
with col1:
    st.write("# Goals over Time")
    st.altair_chart(create_goals_over_time_chart(df))
    st.write("# Goals per Match")
    st.altair_chart(create_goals_per_match_chart(df))
with col2:
    st.write("# Assists over Time")
    st.altair_chart(create_assists_over_time_chart(df))
    st.write("# Assists per Match")
    st.altair_chart(create_assists_per_match_chart(df))

# Display video below charts
st.write("")
st.write("")
st.components.v1.html(f'<iframe width="560" height="315" src="https://www.youtube.com/embed/Xbl6PL3dgmE" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>', width=560, height=315, scrolling=False)
