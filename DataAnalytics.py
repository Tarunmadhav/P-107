import csv
import pandas as pd
import plotly.graph_objects as go
import plotly_express as px

df=pd.read_csv("data.csv")
studentdf=df.loc[df["student_id"]=="TRL_xsl"]
print("mean:" , df.groupby(["student_id", "level"], as_index=False)["attempt"].mean())
figure=go.Figure(go.Bar(
    x=df.groupby(["student_id", "level"], as_index=False)["attempt"].mean(),
    y=["level1","level2","level3","level4"],
    orientation="h"
))

figure.show()
figure1=px.scatter(
   df.groupby(["student_id", "level"], as_index=False)["attempt"].mean(),
   x="student_id",
   y="level" ,
   color="attempt"
)
figure1.show()