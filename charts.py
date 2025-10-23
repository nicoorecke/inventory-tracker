# charts.py
import altair as alt
import streamlit as st

def sales_by_category_chart(df):
    """
    Muestra un gráfico de columnas con las unidades vendidas por producto.
    """
    st.subheader("Sales by product", divider="blue")

    chart = (
        alt.Chart(df)
        .mark_bar()
        .encode(
            x=alt.X("item_name", sort="-y", title="Product"),
            y=alt.Y("units_sold", title="Units Sold"),
            tooltip=["item_name", "units_sold"]
        )
        .properties(height=400)
    )

    st.altair_chart(chart, use_container_width=True)
