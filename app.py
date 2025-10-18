from streamlit import *
from pandas import *
import sorted
import json

df = read_json("Klasbezetting.json")


set_page_config(page_title="Klasbezetting KADE",
                page_icon=":bar_chart:",
                layout="wide")

title = "Klasbezetting TEST TOOL"

jaar = sidebar.multiselect(
  label = "jaar",
  options = df["Jaar"].sort_values().unique()

lkr = sidebar.multiselect(
  label = "Leerkracht(en)",
  options = df["Leerkracht(en)"].unique()

lokaal = sidebar.multiselect(
  label = "Lokaal",
  options = df["Lokaal"].unique()




dataframe(df)
