# ACC102 Track 4: Interactive Financial Analysis Tool
# Full English, Streamlit Interactive App
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

# --------------------------
# 1. Page Config (professional layout)
# --------------------------
st.set_page_config(page_title="Company Sales Analysis", layout="wide")

# --------------------------
# 2. Load Dataset (your data from notebook)
# --------------------------
st.title("Interactive Company Sales & Industry Analysis")
st.markdown("### ACC102 Mini Assignment | Track 4")

# You can replace this with your actual data
# Example data (same logic as your notebook)
data = {
    "company_name": ["Apple", "Microsoft", "Google", "Amazon", "Meta"],
    "industry": ["Technology", "Technology", "Technology", "Retail", "Technology"],
    "sales": [383, 211, 303, 514, 134]
}
df = pd.DataFrame(data)

# --------------------------
# 3. Basic Dataset Info (matches your notebook)
# --------------------------
st.subheader("1. Dataset Information")
st.write(f"Rows: {df.shape[0]}, Columns: {df.shape[1]}")
st.dataframe(df)

# --------------------------
# 4. Interactive Filter 1: Industry Selection (CORE INTERACTIVE FEATURE)
# --------------------------
st.subheader("2. Filter by Industry (Interactive)")
industry_option = st.selectbox("Select Industry", df["industry"].unique())
filtered_data = df[df["industry"] == industry_option]

st.write(f"Companies in **{industry_option}** industry:")
st.dataframe(filtered_data)

# --------------------------
# 5. Visualization (same chart as your notebook)
# --------------------------
st.subheader("3. Total Sales by Company")
plt.figure(figsize=(10, 5))
plt.bar(df["company_name"], df["sales"], color="#4CAF50")
plt.title("Total Sales Performance")
plt.xticks(rotation=45)
plt.tight_layout()
st.pyplot(plt)

# --------------------------
# 6. Key Insights (required for high mark)
# --------------------------
st.subheader("4. Key Insights")
st.write("✅ Technology companies dominate the dataset.")
st.write("✅ Amazon has the highest total sales among all firms.")
st.write("✅ This tool allows users to filter industries dynamically.")
