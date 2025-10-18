from streamlit import *
from pandas import *
import json

df = read_json("Klasbezetting.json")


set_page_config(page_title="Klasbezetting KADE",
                page_icon=":bar_chart:",
                layout="wide")

title = "Klasbezetting TEST TOOL"

jaar = sidebar.multiselect(
  label = "Data",
  options = df[jaar].unique())



dataframe(df)
