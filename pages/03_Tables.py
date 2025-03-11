from pathlib import Path
from utilities import reading_data

import streamlit as st
import pandas as pd

reading_data()


df_sales = st.session_state["data"]["df_sales"]
df_branches = st.session_state["data"]["df_branches"]
df_products = st.session_state["data"]["df_products"]

st.dataframe(df_sales)
st.dataframe(df_branches)
st.dataframe(df_products)
