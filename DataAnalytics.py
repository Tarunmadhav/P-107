import csv
import pandas as pd
import plotly.graph_objects as go
df=pd.read_csv("data.csv")
studentdf=df.loc[df["student_id"]=="TRL_xsl"]
print(mean = df.groupby(["student_id", "level"], as_index=False)["attempt"].mean())
figure=go.Figure(go.Bar(
    x=df.groupby(["student_id", "level"], as_index=False)["attempt"].mean(),
    y=["level"],
    orientation="h"
))

figure.show()