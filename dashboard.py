import streamlit as st
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

st.set_page_config(
    layout="wide",
    page_icon = "🎆",
    page_title = "Pokemon dashboard"
)
@st.cache_data
def load_data():
    file = "Pokemon.csv"
    data = pd.read_csv(file)
    return data

def main():
    with st.spinner("Loading Pokemons...."):
        df = load_data()
        # st.snow()
    rows,columns= df.shape
    col_names = df.columns.tolist()


    c1,c2,c3 = st.columns(3)
    c1.subheader(f"Total Rows: {rows}")
    c2.subheader(f"Total columns: {columns}")
    c3.subheader(f" Columns : {",".join(col_names)}")

if __name__ == "__main__":
    main()

