from streamlit import *
from pandas import *
import json

data = read_json("Klasbezetting.json")
df = DataFrame(data)

def update_df():
  updated_df = df.querry("Weekdag"==@weekdag)

set_page_config(page_title="Klasbezetting KADE",
                page_icon=":bar_chart:",
                layout="wide")

title = "Klasbezetting TEST TOOL"

sidebar.header("Selecteer")

alle_data = toggle(label = "Alle data", value = True)
if alle_data:
  pass
else:
  datum = date_input(
    label = "Datum",
    format = "DD/MM/YYYY",
    value = "today")

weekdag = sidebar.multiselect(
  label = "Weekdag",
  options = df["Weekdag"].unique()
  )

lkr = sidebar.multiselect(
  label = "Leerkracht(en)",
  options = df["Leerkracht(en)"].unique())

lokaal = sidebar.multiselect(
  label = "Lokaal",
  options = df["Lokaal"].unique())



dataframe(updated_df)
