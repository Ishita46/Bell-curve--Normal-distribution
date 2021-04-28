import pandas as pd
import csv
import plotly.figure_factory as ff

df = pd.read_csv("heightweight.csv")

fig = ff.create_distplot([df["Height(Inches)"].tolist()],["height"],show_hist=False)
#if you dont want to see the histogram/bargraph in the output,then we can give extra instruction in the above line that is show_hist=False.
fig.show()
