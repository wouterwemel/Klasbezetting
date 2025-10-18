from streamlit import *
from pandas import *
import json

data = read_json("Klasbezetting.json")
df = DataFrame(data)


set_page_config(page_title="Klasbezetting KADE",
                page_icon=":bar_chart:",
                layout="wide")

title = "Klasbezetting TEST TOOL"

sidebar.header("Instellingen")

alle_data = sidebar.toggle(label = "Alle data", value = True)
if alle_data:
  pass
else:
  datum = sidebar.date_input(
    label = "Datum",
    format = "DD/MM/YYYY",
    value = "today")

weekdag_options = df["Weekdag"].unique()
print(weekdag_options)
weekdag = sidebar.multiselect(
  label = "Weekdag",
  options = weekdag_options)

lkr = sidebar.multiselect(
  label = "Leerkracht(en)",
  options = df["Leerkracht(en)"].unique())

lokaal = sidebar.multiselect(
  label = "Lokaal",
  options = df["Lokaal"].unique())




dataframe(df)
