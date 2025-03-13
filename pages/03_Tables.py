from pathlib import Path
from utilities import reading_data

import streamlit as st
import pandas as pd

reading_data()


df_sales = st.session_state["data"]["df_sales"]
df_branches = st.session_state["data"]["df_branches"]
df_products = st.session_state["data"]["df_products"]

st.sidebar.markdown("## Table Selection")
tables_selected = st.sidebar.selectbox(
    "Select the table you want to see:", ["Sales", "Products", "Branches"]
)


def print_products_table():
    st.dataframe(df_products)


def print_branches_table():
    st.dataframe(df_branches)


def print_sales_table():
    st.sidebar.divider()
    st.markdown("### Table Filter")
    coluns_selected = st.sidebar.multiselect(
        "Select the table columns:", list(df_sales.columns), list(df_sales.columns)
    )
    col1, col2 = st.sidebar.columns(2)
    selected_filter = col1.selectbox("Column Filter:", list(df_sales.columns))
    unique_values_columns = list(df_sales[selected_filter].unique())
    values_filter = col2.selectbox("Value Filter:", unique_values_columns)

    filter = col1.button("Filter")
    clean = col2.button("Clean")

    if filter:
        st.dataframe(
            df_sales.loc[df_sales[selected_filter] == values_filter, coluns_selected],
            height=800,
        )
    elif clean:
        st.dataframe(df_sales[coluns_selected], height=800)
    else:
        st.dataframe(df_sales[coluns_selected], height=800)


if tables_selected == "Products":
    print_products_table()
elif tables_selected == "Branches":
    print_branches_table()
elif tables_selected == "Sales":
    print_sales_table()
