from streamlit import *
from pandas import *
import json

# SETUP DATAFRAME
data = read_json("Klasbezetting.json")
df = DataFrame(data)
updated_df = df

# SETUP APP
set_page_config(page_title="Klasbezetting KADE",
                page_icon=":bar_chart:",
                layout="wide")

title = "Klasbezetting TEST TOOL"

sidebar.header("Selecteer")

# SETUP SETTINGS
alle_data = sidebar.toggle(label = "Alle data", value = True)
if alle_data:
  datum = list(df["Datum"].unique())
else:
  datum = date_input(
    label = "Datum",
    format = "DD/MM/YYYY",
    value = "today")

alle_weekdagen = sidebar.toggle(label = "Alle weekdagen", value = True)
if alle_weekdagen:
  weekdag = list(df["Weekdag"].unique())
else:
  weekdag = multiselect(
    label = "Weekdag",
    options = df["Weekdag"].unique())

alle_lkr = sidebar.toggle(label = "Alle leerkrachten", value = True)
if alle_lkr:
  lkr = list(df["Leerkracht"].unique())
else:
  lkr = multiselect(
    label = "Leerkracht",
    options = df["Leerkracht"].unique())

alle_lokalen = sidebar.toggle(label = "Alle lokalen", value = True)
if alle_lokalen:
  lokaal = list(df["Lokaal"].unique())
else:
  lokaal = multiselect(
    label = "Lokaal",
    options = df["Lokaal"].unique())


updated_df = df.query("Datum == @datum & Weekdag == @weekdag & Leerkracht == @lkr & Lokaal == @lokaal")
dataframe(updated_df)
