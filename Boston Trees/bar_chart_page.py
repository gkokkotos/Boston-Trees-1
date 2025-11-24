"""
Name: Grace Kokkotos
Date:
Description: Bar chart page showing the top 30 tree species in Boston (no filters)
"""

import streamlit as st
import plotly.express as px
from utils import load_data, clean_data
import plotly.colors as pc

def create_bar_chart(df, top_n=30):
    """Create a horizontal bar chart showing top N tree species with color gradient."""
    if df.empty:
        st.warning("No data available to create chart.")
        return

    # Compute top N species
    top_species_counts = df["species_common"].value_counts().nlargest(top_n).reset_index()
    top_species_counts.columns = ["species", "count"]

    # Create an interpolated color gradient
    # Use a continuous color scale from Plotly
    colorscale = pc.sequential.Viridis  # can be any Plotly sequential scale
    # Interpolate colors for all bars
    from matplotlib import colors as mcolors
    import matplotlib.cm as cm
    import numpy as np

    norm = mcolors.Normalize(vmin=0, vmax=top_n-1)
    cmap = cm.get_cmap('viridis', top_n)
    colors = [f'rgb({int(r*255)}, {int(g*255)}, {int(b*255)})' for r, g, b, _ in cmap(np.arange(top_n))]

    top_species_counts["color"] = colors

    # Plotly horizontal bar chart
    fig = px.bar(
        top_species_counts,
        x="count",
        y="species",
        orientation="h",
        labels={"count": "Number of Trees", "species": "Species"},
        title=f"Top {top_n} Tree Species in Boston",
        text="count",
        color="color",  # use the interpolated colors
        color_discrete_map="identity"  # tells Plotly to use the exact color values
    )

    fig.update_layout(
        yaxis=dict(autorange="reversed"),  # largest on top
        margin=dict(l=150, r=20, t=50, b=50)
    )

    st.plotly_chart(fig, use_container_width=True)


def bar_chart_page():
    """Main function to display the bar chart page."""
    st.title("Top Tree Species in Boston")
    df = load_data()
    if df.empty:
        st.warning("No data available.")
        return
    df = clean_data(df)

    create_bar_chart(df)