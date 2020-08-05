from autoplotter import run_app # Importing the autoplotter for GUI Based EDA

import plotly.express as px # Importing plotly express to load dataset
df = px.data.tips() # Getting the   Restaurant data

run_app(df) # Calling the autoplotter.run_app