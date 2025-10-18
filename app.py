from streamlit import *
from pandas import *
import json

df = read_json("Klasbzetting.json")


set_page_config(page_title="Klasbezetting KADE",
                page_icon=":bar_chart:",
                layout="wide")

title = "Klasbezetting TEST TOOL"


dataframe(df)
