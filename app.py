# ACC102 Track 4 Interactive Data Analysis Tool
# Student Name: An Jiechen
# Student ID: 2473444
# Data Source: WRDS Compustat North America

import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

# Your Financial Data (Apple 2019-2023)
data = {
    "fyear": [2019, 2020, 2021, 2022, 2023],
    "revt": [260174, 274515, 365817, 394328, 383285],
    "cogs": [162564, 169559, 212951, 223546, 214131],
    "ni": [55256, 57411, 94680, 99803, 96995]
}

df = pd.DataFrame(data)
df["profit"] = df["revt"] - df["cogs"]

# Streamlit Interface
st.title("Apple Inc. Financial Performance Analysis")
st.subheader("2019-2023")

st.subheader("Financial Data")
st.dataframe(df)

st.subheader("Revenue and Net Income Trend")
plt.figure(figsize=(10,5))
plt.plot(df["fyear"], df["revt"], marker="o", label="Revenue (REVT)")
plt.plot(df["fyear"], df["ni"], marker="s", label="Net Income (NI)")
plt.xlabel("Fiscal Year")
plt.ylabel("Million USD")
plt.legend()
plt.grid(True)
st.pyplot(plt)

st.subheader("Key Insights")
st.write("""
1. Revenue grew from 2019 to 2022.
2. Net income increased steadily over the period.
3. Apple maintained strong financial performance.
""")
