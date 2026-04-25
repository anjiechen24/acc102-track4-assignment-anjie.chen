# ACC102 Track 4: Interactive Data Analysis Tool
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

st.set_page_config(page_title="Sales Analysis", layout="wide")
st.title("Interactive Corporate Sales & Industry Analysis")
st.caption("ACC102 Mini Assignment | Track 4")

# Dataset
df = pd.DataFrame({
    "company_name": ["Apple", "Microsoft", "Google", "Amazon", "Meta"],
    "industry": ["Technology", "Technology", "Technology", "Retail", "Technology"],
    "sales": [383285, 211413, 303368, 514000, 134902]
})

# 1. Dataset Overview
st.subheader("1. Dataset Overview")
st.write(f"Rows: {df.shape[0]}, Columns: {df.shape[1]}")
st.dataframe(df)

# 2. Missing Values Check
st.subheader("2. Missing Values Check")
st.dataframe(df.isnull().sum())

# 3. Descriptive Statistics
st.subheader("3. Descriptive Statistics")
st.dataframe(df.describe())

# 4. Interactive Industry Filter
st.subheader("4. Filter by Industry")
selected_industry = st.selectbox("Select Industry", df["industry"].unique())
filtered_by_industry = df[df["industry"] == selected_industry]
st.dataframe(filtered_by_industry)

# 5. Interactive Sales Range Filter
st.subheader("5. Filter by Sales Range")
min_sales = int(df["sales"].min())
max_sales = int(df["sales"].max())
sales_range = st.slider("Select Sales Range", min_sales, max_sales, (min_sales, max_sales))
filtered_data = df[(df["sales"] >= sales_range[0]) & (df["sales"] <= sales_range[1])]
st.dataframe(filtered_data)

# 6. Sales Visualization
st.subheader("6. Sales Visualization")
plt.figure(figsize=(10, 5))
plt.bar(filtered_data["company_name"], filtered_data["sales"])
plt.title("Total Sales by Company")
plt.xticks(rotation=90)
plt.tight_layout()
st.pyplot(plt)

# 7. Industry Distribution
st.subheader("7. Industry Distribution")
fig, ax = plt.subplots()
ax.pie(df["industry"].value_counts(), labels=df["industry"].unique(), autopct='%1.1f%%')
ax.set_title("Industry Proportion")
st.pyplot(fig)
