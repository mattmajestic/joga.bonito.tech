import streamlit as st
import pandas as pd
import altair as alt

# Set page config
st.set_page_config(page_title="Joga Bonito at Tech", page_icon=":soccer:")
st.title("Joga Bonito at Tech")
st.write("Analysis of player performance at Georgia Tech soccer games")

# Load data
df = pd.read_csv("tech-stats.csv")

def create_charts(df):
    goals_over_time_chart = alt.Chart(df).mark_line().encode(
        x='Date:T',
        y='Goals:Q'
    ).properties(
        height=400,  # <-- double the height
        width=400,  # <-- double the width
        title='Goals Over Time'
    )

    goals_per_match_chart = alt.Chart(df).mark_bar().encode(
        x='Player:N',
        y='Goals_per_match:Q'
    ).properties(
        height=400,  # <-- double the height
        width=400,  # <-- double the width
        title='Goals per Match'
    )

    assists_per_match_chart = alt.Chart(df).mark_bar().encode(
        x='Player:N',
        y='Assists_per_match:Q'
    ).properties(
        height=400,  # <-- double the height
        width=400,  # <-- double the width
        title='Assists per Match'
    )

    assists_over_time_chart = alt.Chart(df).mark_line().encode(
        x='Date:T',
        y='Assists:Q'
    ).properties(
        height=400,  # <-- double the height
        width=400,  # <-- double the width
        title='Assists Over Time'
    )

    return goals_over_time_chart | goals_per_match_chart, assists_per_match_chart | assists_over_time_chart


# Compute derived data
df["Date"] = pd.to_datetime(df["Date"])
df["Goals_per_match"] = df.groupby(['Player', 'Date'])['Goals'].transform('sum') / df.groupby(['Player', 'Date'])['Date'].transform('nunique')
df["Assists_per_match"] = df.groupby(['Player', 'Date'])['Assists'].transform('sum') / df.groupby(['Player', 'Date'])['Date'].transform('nunique')

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
