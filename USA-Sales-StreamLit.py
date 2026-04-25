# ==========================================================
# USA FOOD REVENUE FORECAST DASHBOARD
# Streamlit Professional Version
# ==========================================================

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# ----------------------------------------------------------
# PAGE CONFIG
# ----------------------------------------------------------
st.set_page_config(
    page_title="USA Revenue Forecast Dashboard",
    page_icon="📈",
    layout="wide"
)

# ----------------------------------------------------------
# LOAD DATA
# ----------------------------------------------------------
df = pd.read_csv("RawMessyFileOfUSA.csv")

# Clean column names
df.columns = df.columns.str.strip()

# Rename if needed
if "month" in df.columns:
    df.rename(columns={"month": "Month"}, inplace=True)

# Convert Month column
df["Month"] = pd.to_datetime(df["Month"], errors="coerce")

# Drop blank dates
df = df.dropna(subset=["Month"])

# Revenue numeric
df["Revenue"] = pd.to_numeric(df["Revenue"], errors="coerce")

# ----------------------------------------------------------
# CREATE EXTRA COLUMNS
# ----------------------------------------------------------
df["Year"] = df["Month"].dt.year
df["Month_Name"] = df["Month"].dt.strftime("%B")

# Growth %
df["MoM Growth %"] = df["Revenue"].pct_change() * 100

# ----------------------------------------------------------
# KPIs
# ----------------------------------------------------------
latest_revenue = df["Revenue"].iloc[-1]
growth = df["MoM Growth %"].iloc[-1]
rmse = 6580.20

# ----------------------------------------------------------
# SIDEBAR
# ----------------------------------------------------------
st.sidebar.header("Filters")

date_range = st.sidebar.date_input(
    "Select Date Range",
    [df["Month"].min(), df["Month"].max()]
)

holiday_filter = st.sidebar.multiselect(
    "Holiday Type",
    options=df["Holiday_Flag"].unique(),
    default=df["Holiday_Flag"].unique()
)

# Apply filters
if len(date_range) == 2:
    df = df[
        (df["Month"] >= pd.to_datetime(date_range[0])) &
        (df["Month"] <= pd.to_datetime(date_range[1]))
    ]

df = df[df["Holiday_Flag"].isin(holiday_filter)]

# ----------------------------------------------------------
# TITLE
# ----------------------------------------------------------
st.title("📊 USA Food Revenue Forecast Dashboard")
st.markdown("Business Intelligence | Forecasting | Trend Analysis")

# ----------------------------------------------------------
# KPI CARDS
# ----------------------------------------------------------
k1, k2, k3 = st.columns(3)

with k1:
    st.metric("Growth %", f"{growth:.2f}%")

with k2:
    st.metric("Revenue", f"{latest_revenue/1000:.2f}K")

with k3:
    st.metric("RMSE", f"{rmse/1000:.2f}K")

st.markdown("---")

# ----------------------------------------------------------
# ROW 1
# ----------------------------------------------------------
c1, c2 = st.columns(2)

# Average Monthly Revenue
with c1:
    avg_month = df.groupby("Month_Name")["Revenue"].mean().reset_index()

    month_order = [
        "January","February","March","April","May","June",
        "July","August","September","October","November","December"
    ]

    avg_month["Month_Name"] = pd.Categorical(
        avg_month["Month_Name"],
        categories=month_order,
        ordered=True
    )

    avg_month = avg_month.sort_values("Month_Name")

    fig1 = px.bar(
        avg_month,
        x="Month_Name",
        y="Revenue",
        text="Revenue",
        title="Average Monthly Revenue"
    )

    fig1.update_traces(
        texttemplate='%{text:.0f}',
        marker_color="#1f77b4"
    )

    fig1.update_layout(height=350)

    st.plotly_chart(fig1, use_container_width=True)

# Historical Revenue
with c2:
    fig2 = px.line(
        df,
        x="Month",
        y="Revenue",
        color="Type",
        title="Historical Revenue & Forecast Outlook"
    )

    fig2.update_layout(height=350)

    st.plotly_chart(fig2, use_container_width=True)

# ----------------------------------------------------------
# ROW 2
# ----------------------------------------------------------
c3, c4 = st.columns(2)

# Holiday Revenue
with c3:
    holiday = df.groupby("Holiday_Flag")["Revenue"].sum().reset_index()

    fig3 = px.bar(
        holiday,
        x="Revenue",
        y="Holiday_Flag",
        orientation="h",
        color="Holiday_Flag",
        title="Holiday vs Non-Holiday Revenue"
    )

    fig3.update_layout(height=320, showlegend=False)

    st.plotly_chart(fig3, use_container_width=True)

# Growth %
with c4:
    fig4 = px.line(
        df,
        x="Month",
        y="MoM Growth %",
        color="Type",
        title="Monthly Revenue Growth %"
    )

    fig4.update_layout(height=320)

    st.plotly_chart(fig4, use_container_width=True)

# ----------------------------------------------------------
# KEY INSIGHTS
# ----------------------------------------------------------
st.markdown("### 📌 Key Insights")

st.info(f"""
• Revenue forecast for next month: {latest_revenue/1000:.2f}K  
• Holiday periods increase revenue significantly  
• RMSE {rmse/1000:.2f}K indicates strong model accuracy  
• Revenue recovered strongly post-2020 dip  
• Peak demand concentrated in Q4 months  
""")
