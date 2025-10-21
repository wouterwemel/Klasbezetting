from streamlit import *
from pandas import *
import datetime
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
  datum_kort = list(df["Datum_kort"].unique())
else:
  datum = date_input(
    label = "Datum",
    format = "DD/MM/YYYY",
    value = "today")
  datum_kort = str(datum)

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

alle_type = sidebar.toggle(label = "Alle type", value = True)
if alle_type:
  type = list(df["Type"].unique())
else:
  type = multiselect(
    label = "Type",
    options = df["Type"].unique())

alleen_uitzonderlijk = sidebar.checkbox(label = "Toon alleen uitzonderlijk", value = False)
if alleen_uitzonderlijk:
  uitzonderlijk = True
else:
  uitzonderlijk = [False, True]
  
updated_df = df.query("Datum_kort == @datum_kort & Weekdag == @weekdag & Leerkracht == @lkr & Lokaal == @lokaal & Type == @type & Uitzonderlijk == @uitzonderlijk")
dataframe(data = updated_df,
         height = 600)
