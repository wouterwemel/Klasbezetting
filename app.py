from streamlit import *
from pandas import *
import json

data = read_json("Klasbezetting.json")
df = DataFrame(data)


set_page_config(page_title="Klasbezetting KADE",
                page_icon=":bar_chart:",
                layout="wide")

title = "Klasbezetting TEST TOOL"


jaar = sidebar.multiselect(
  label = "jaar",
  options = df["Jaar"].sorted())

lkr = sidebar.multiselect(
  label = "Leerkracht(en)",
  options = df["Leerkracht(en)"].unique())

lokaal = sidebar.multiselect(
  label = "Lokaal",
  options = df["Lokaal"].unique())




dataframe(df)
