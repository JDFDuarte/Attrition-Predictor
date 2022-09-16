import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
from urllib.request import urlopen
import json
from copy import deepcopy
import seaborn as sns
from collections import Counter
import numpy as np
from PIL import Image

st.set_page_config(page_title="IBM Employee Attrition", page_icon="chart_with_upwards_trend",
        layout="wide")

@st.cache
def load_data(path):
    df = pd.read_csv(path)
    return df

df_map_raw = load_data(path=r"C:\Users\Study\Desktop\outmap.csv")
df_map = deepcopy(df_map_raw)

df_ibm_raw = load_data(path=r"C:\Users\Study\Desktop\WA_Fn-UseC_-HR-Employee-Attrition.csv")
df_ibm = deepcopy(df_ibm_raw)



st.sidebar.title("Dataframe overview")
if st.sidebar.checkbox('Show first 10 lines'):
  st.success('The first 10 lines were loaded')
  st.write(df_ibm[:11])


#st.dataframe(df_ibm)

st.title("IBM HR Analytics Employee Attrition")
st.header("Office Distribution")

kaggle_url = "https://www.kaggle.com/datasets/pavansubhasht/ibm-hr-analytics-attrition-dataset"
st.write("Dataset used. Check it out: ", kaggle_url)

df_map = pd.read_csv(r"C:\Users\Study\Desktop\outmap.csv")

st.map(data = df_map, zoom = 1)


left_column, middle_column, right_column = st.columns([3, 1, 1])

st.header("Select one variable:")
play_vars = ["Age", "EducationField", "Gender", "JobRole", "YearsWithCurrManager"]

var_select = st.selectbox("Show variables", play_vars)

colors = {"Age":"orange",
          "EducationField":"teal",
          "EnvironmentSatisfaction":"brown",
          "Gender":"blue",
          "JobRole":"purple",
          "YearsWithCurrManager":"green"}

fig1 = go.Figure()
fig1.add_trace(go.Bar(x=df_ibm[var_select],
                      y=df_ibm["Attrition"],
                      name=var_select,
                      marker_color=colors[var_select]
                      ))


fig1.update_layout(hovermode="x")
fig1.update_layout(
    title={"text": "Attrition / Variable of choice", "font": {"size": 24}},
    xaxis={"title": {"text": "Attrition", "font": {"size": 18}}},
    xaxis_tickfont_size = 18,
    yaxis={"title": {"text": "Variable", "font": {"size": 18}}},
)

st.plotly_chart(fig1, use_container_width=True)

# fig6 = go.Figure()
# df_agg = df_ibm[["Age", "EducationField", "Gender", "JobRole", "YearsWithCurrManager", "Attrition"]].groupby(["Attrition"]).agg('sum').reset_index()
#
# fig6.add_traces(
#     data=[
#         go.Bar(y=df_agg[df_agg['Attrition']=='Yes']['Attrition'], x = df_agg[df_agg['Attrition']=='Yes'][var_select]),
#         go.Bar(y=df_agg[df_agg['Attrition']=='No']['Attrition'], x = df_agg[df_agg['Attrition']=='No'][var_select])])
#
# fig6.update_layout(hovermode="x")
#
# fig6.update_layout(
#     title={"text": "Attrition / Variable of choice", "font": {"size": 24}},
#     xaxis={"title": {"text": "Attrition", "font": {"size": 18}}},
#     xaxis_tickfont_size = 18,
#     yaxis={"title": {"text": "Variable", "font": {"size": 18}}},
# )
#
# st.plotly_chart(fig6, use_container_width=True)


confution = pd.read_csv(r"C:\Users\Study\Desktop\fancy_graph.csv")

fig2 = go.Figure()
for col in confution.columns:
    fig2.add_trace(
        go.Scatter(x=confution.index, y=confution[col], mode="lines+markers", name=col)
    )
fig2.update_layout(hovermode="x unified")

fig2.update_layout(
    title={"text": "Accuracy of the Model vs Treshold", "font": {"size": 24}},
    xaxis={"title": {"text": "Treshold", "font": {"size": 16}}},
    yaxis={"title": {"text": "Accuracy", "font": {"size": 16}}},
    paper_bgcolor="lightgrey",
    plot_bgcolor="lightgrey",
)

st.plotly_chart(fig2, use_container_width=True)