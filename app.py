from streamlit import *
from pandas import *
import json

df_excel = read_excel("Klasbzetting KADE - 2025-2026.xlsx")
df_json = df_excel.to_json()
print(df_json)

set_page_config(page_title="Klasbezetting KADE",
                page_icon=":bar_chart:",
                layout="wide")

title = "Klasbezetting TEST TOOL"


dataframe(df_json)
