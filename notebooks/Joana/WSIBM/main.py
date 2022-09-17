import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
from urllib.request import urlopen
from PIL import Image
from copy import deepcopy

# ________________________________________________________________________________________
st.set_page_config(page_title="IBM Employee Attrition", page_icon=":muscle:",
        layout="wide")
# _________________________________________________________________________________________
@st.cache
def load_data(path):
    df = pd.read_csv(path)
    return df

df_map_raw = load_data(path=r"C:\Users\Study\Desktop\outmap.csv")
df_map = deepcopy(df_map_raw)

df_ibm_raw = load_data(path=r"C:\Users\Study\Desktop\WA_Fn-UseC_-HR-Employee-Attrition.csv")
df_ibm = deepcopy(df_ibm_raw)

# ___________Display sidebar________________________________________________
st.sidebar.metric("Date", value = "16.09.2022")
image = Image.open(r"C:\Users\Study\Desktop\sit_logo.png")
st.sidebar.image(image)
st.sidebar.title("**SiT Academy** Group Challenge")

st.sidebar.header("")
st.sidebar.header("")
st.sidebar.subheader("Data Science Consulting Team:")
url_betka = "https://www.linkedin.com/in/al%C5%BEbeta-bohinikov%C3%A1-904260132/"
st.sidebar.write("Betka Bohinikova", url_betka)
url_eva = "https://www.linkedin.com/in/eva-polakova-6ba5a330/"
st.sidebar.write("Eva Polakova", url_eva)
url_joana = "www.linkedin.com/in/joanaduartesantos"
st.sidebar.write("Joana Duarte", url_joana)
url_ella = "https://www.linkedin.com/in/mihaela-cucui-642789b5/"
st.sidebar.write("Mihaela Cucui", url_ella)


# _________Titles___________________________________________________________
st.title("IBM HR Analytics Employee Attrition")

# _________Dataframe________________________________________________________
st.title("Dataframe overview")
if st.checkbox('Show entire dataframe'):
    st.success('Show entire dataframe')
    st.write(df_ibm)
if st.checkbox('Show first 10 lines'):
    st.success('The first 10 lines were loaded')
    st.write(df_ibm[:11])


# _________Map of office locations__________________________________________
kaggle_url = "https://www.kaggle.com/datasets/pavansubhasht/ibm-hr-analytics-attrition-dataset"
st.write("Dataset used. You can also check it out here: ", kaggle_url)

ibm_url = "https://www.ibm.com/planetwide/"
st.title("")
st.header("Office distribution")
st.write("Source: ", ibm_url)
df_map = pd.read_csv(r"C:\Users\Study\Desktop\outmap.csv")
st.map(data = df_map, zoom = 1)


# _______Selection box________________________________________________________
st.header("")
st.header("Plot your variable of choice")
st.subheader("Please, select one variable:")
play_vars = ["Age", "BusinessTravel", "DistanceFromHome", "EducationField", "Gender", "JobRole", "YearsWithCurrManager"]

var_select = st.selectbox("Show variables", play_vars)


# ____________Plot based on Selection_________________________________________

fig_test = go.Figure()

yes = df_ibm[var_select][df_ibm.Attrition == "Yes"].value_counts(ascending=False)
no = df_ibm[var_select][df_ibm.Attrition == "No"].value_counts(ascending=False)

fig_test.add_bar(y=yes, x=df_ibm[var_select], marker={'color':'darkorange'}, showlegend=True, name = "Yes")
fig_test.add_bar(y=no, x=df_ibm[var_select], marker={'color':'darkblue'}, showlegend=True, name = "No")

fig_test.update_layout(hovermode="x")
fig_test.update_layout(
    title={"text": "Attrition / Variable of choice", "font": {"size": 24}},
    xaxis={"title": {"text": "Attrition", "font": {"size": 18}}},
    xaxis_tickfont_size = 18
)

st.plotly_chart(fig_test, use_container_width=True)

# ______________Fancy graph____________________________________________________________

st.title("")

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