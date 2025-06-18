

import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(layout="wide")

@st.cache_data
def load_data():
    benin = pd.read_csv("../data/benin-malanville_clean.csv")
    sierra = pd.read_csv("../data/sierraleone-bumbuna_clean.csv")
    togo = pd.read_csv("../data/togo-dapaong_qc_clean.csv")

    benin["Country"] = "Benin"
    sierra["Country"] = "Sierra Leone"
    togo["Country"] = "Togo"

    return pd.concat([benin, sierra, togo], ignore_index=True)

df = load_data()

st.title("🌍 Solar Radiation Dashboard")

# Widget
country_selection = st.multiselect(
    "Select Country/Countries", df["Country"].unique(), default=df["Country"].unique()
)

filtered_df = df[df["Country"].isin(country_selection)]

# Boxplot
metric = st.selectbox("Select Metric to Compare", ["GHI", "DNI", "DHI"])

fig, ax = plt.subplots(figsize=(10, 6))
sns.boxplot(x="Country", y=metric, data=filtered_df, ax=ax)
ax.set_title(f"{metric} Distribution by Country")
st.pyplot(fig)

# Summary Table
if st.checkbox("Show Summary Table"):
    st.subheader(f"{metric} Summary")
    st.dataframe(filtered_df.groupby("Country")[metric].describe()[["mean", "50%", "std"]].rename(columns={"50%": "median"}))

