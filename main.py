import streamlit as st
import pandas as pd
import plotly.express as px

# Page settings
st.set_page_config(
    page_title="EV Battery & BMS Simulator",
    page_icon="🔋",
    layout="wide"
)

st.title("🔋 EV Battery & BMS Simulator")
st.subheader("Battery Monitoring Dashboard")

# Read battery data
df = pd.read_csv("battery_data.csv")

# Latest battery values
latest = df.iloc[-1]

soc = latest["SOC (%)"]
voltage = latest["Voltage (V)"]
current = latest["Current (A)"]
temperature = latest["Temperature (°C)"]

# BMS Status
if voltage > 52:
    status = "⚠️ OVER-VOLTAGE"
elif voltage < 48:
    status = "⚠️ UNDER-VOLTAGE"
elif current > 30:
    status = "⚠️ OVER-CURRENT"
elif temperature > 60:
    status = "⚠️ OVERHEATING"
else:
    status = "🟢 NORMAL"

# Battery values
col1, col2, col3, col4 = st.columns(4)

col1.metric("🔋 SOC", f"{soc:.0f}%")
col2.metric("⚡ Voltage", f"{voltage:.2f} V")
col3.metric("🔌 Current", f"{current:.0f} A")
col4.metric("🌡️ Temperature", f"{temperature:.1f} °C")

st.divider()

# BMS Status
st.subheader("BMS Status")
st.info(status)

st.divider()

# Graphs
st.subheader("📊 Battery Parameters")

col1, col2 = st.columns(2)

with col1:
    fig_soc = px.line(
        df,
        y="SOC (%)",
        title="SOC",
        markers=True
    )
    st.plotly_chart(fig_soc, use_container_width=True)

with col2:
    fig_voltage = px.line(
        df,
        y="Voltage (V)",
        title="Voltage",
        markers=True
    )
    st.plotly_chart(fig_voltage, use_container_width=True)

col3, col4 = st.columns(2)

with col3:
    fig_current = px.line(
        df,
        y="Current (A)",
        title="Current",
        markers=True
    )
    st.plotly_chart(fig_current, use_container_width=True)

with col4:
    fig_temperature = px.line(
        df,
        y="Temperature (°C)",
        title="Temperature",
        markers=True
    )
    st.plotly_chart(fig_temperature, use_container_width=True)

st.divider()

st.subheader("📋 Battery Data")

st.dataframe(df, use_container_width=True)