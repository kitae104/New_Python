from autoplotter import run_app
import pandas as pd

df = pd.read_csv('car_design.csv')
run_app(df)