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

alle_jaren = sidebar.toggle(
  label = "alle jaren",
  value = True)
if alle_jaren:
  pass
else:
  jaar = sidebar.multiselect(
    label = "jaar",
    options = df["Jaar"].unique())

datum = sidebar.date_input(
  label = "Datum",
  format = "DD/MM/YYYY"
)


maand = sidebar.multiselect(
  label = "Maand",
  options = df["Maand"].unique())

dag = sidebar.multiselect(
  label = "Dag",
  options = df["Dag"].unique())

weekdag = sidebar.multiselect(
  label = "Weekdag",
  options = df["Weekdag"].unique())

lkr = sidebar.multiselect(
  label = "Leerkracht(en)",
  options = df["Leerkracht(en)"].unique())

lokaal = sidebar.multiselect(
  label = "Lokaal",
  options = df["Lokaal"].unique())




dataframe(df)
