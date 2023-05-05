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
        height=600,  # <-- double the height
        width=600,  # <-- double the width
        title='Goals Over Time'
    )

    goals_per_match_chart = alt.Chart(df).mark_bar().encode(
        x='GameTime:O',
        y='Goals:Q'
    ).properties(
        height=600,  # <-- double the height
        width=600,  # <-- double the width
        title='Goals per Match'
    )

    assists_per_match_chart = alt.Chart(df).mark_bar().encode(
        x='GameTime:O',
        y='Assists:Q'
    ).properties(
        height=600,  # <-- double the height
        width=600,  # <-- double the width
        title='Assists per Match'
    )

    assists_over_time_chart = alt.Chart(df).mark_line().encode(
        x='Date:T',
        y='Assists:Q'
    ).properties(
        height=600,  # <-- double the height
        width=600,  # <-- double the width
        title='Assists Over Time'
    )

    return goals_over_time_chart | goals_per_match_chart, assists_per_match_chart | assists_over_time_chart


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

# Display video below charts
st.write("")
st.write("")
st.components.v1.html(f'<iframe width="560" height="315" src="https://www.youtube.com/embed/Xbl6PL3dgmE" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>', width=560, height=315, scrolling=False)