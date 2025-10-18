from streamlit import *
from pandas import *

df = read_excel("Klasbzetting KADE - 2025-2026.xlsx")
df_selection = df

set_page_config(page_title="Klasbezetting KADE",
                page_icon=":bar_chart:",
                layout="wide")

title = "Klasbezetting TEST TOOL"


dataframe(df)
