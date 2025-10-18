from streamlit import *
from pandas import *
import json

# SET DATAFRAME
data = read_json("Klasbezetting.json")
df = DataFrame(data)
updated_df = df

# SET VARIABLES





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

alle_weekdagen = sidebar.toggle(label = "Alle weekdagen", value = True)
if alle_weekdagen:
  weekdag = df["Weekdag"].unique()
  return weekdag
else:
  weekdag = sidebar.multiselect(
    label = "Weekdag",
    options = df["Weekdag"].unique())

lkr = sidebar.multiselect(
  label = "Leerkracht(en)",
  options = df["Leerkracht(en)"].unique())

lokaal = sidebar.multiselect(
  label = "Lokaal",
  options = df["Lokaal"].unique())


updated_df = df.query("Weekdag == @weekdag")
dataframe(updated_df)
