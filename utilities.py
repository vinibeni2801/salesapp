from pathlib import Path

import streamlit as st
import pandas as pd


def reading_data():
    if not "data" in st.session_state:
        folder_datasets = Path(__file__).parents[0] / "datasets"

        df_sales = pd.read_csv(
            folder_datasets / "vendas.csv",
            decimal=",",
            sep=";",
            index_col=0,
            parse_dates=True,
        )
        df_branches = pd.read_csv(
            folder_datasets / "filiais.csv", decimal=",", sep=";", index_col=0
        )
        df_products = pd.read_csv(
            folder_datasets / "produtos.csv", decimal=",", sep=";", index_col=0
        )

        data = {
            "df_sales": df_sales,
            "df_branches": df_branches,
            "df_products": df_products,
        }
        st.session_state["data"] = data
