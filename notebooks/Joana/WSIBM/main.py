import pandas as pd
import warnings
warnings.filterwarnings('ignore')
import streamlit as st


df_despair = pd.read_csv(r"C:\Users\Study\Desktop\outmap.csv")
print(df_despair["latitude"])

st.map(data=df_despair, zoom = 3)