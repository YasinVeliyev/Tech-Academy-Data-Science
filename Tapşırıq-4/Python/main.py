import plotly.express as px
import pandas as pd
import numpy as np
from datetime import datetime

data = pd.read_excel(".././REKTDATABASE.xlsx")

data = data[data['Project'].notna()]
data["FundsRecovered"].fillna(0, inplace=True)
data["Category"].fillna("Other", inplace=True)
data["IsVerifiedSourceCode"].fillna(0, inplace=True)
data["IsPublicedTeam"].fillna(0, inplace=True)
data.iloc[:, 0] = data.iloc[:, 0].apply(lambda x: int(x))

data = data.loc[(data["Date"].notna()) & (data["FundLost"] > 0)]

data["Amount"] = data["FundLost"]-data["FundsRecovered"]-data["FundsReturned"]

data_monetary = data.groupby("ID").agg(Project=pd.NamedAgg(column="Project", aggfunc=lambda project: project),
                                       Monetary=pd.NamedAgg(column="Amount", aggfunc="sum")).reset_index().set_index("ID")

data_frequency = data.groupby("ID").agg(Frequency=pd.NamedAgg(
    column="Project", aggfunc="count")).reset_index().set_index("ID")

m = data["Date"].max()
data_recency = data.groupby("ID").agg(Recency=pd.NamedAgg(
    column="Date", aggfunc="max")).reset_index().set_index("ID")
data_recency["Recency"] = (m-data_recency["Recency"])
data_recency["Recency"] = data_recency["Recency"].apply(lambda d: d.days)

rfm_data = data_monetary.join(data_frequency, on="ID", how="outer")
rfm_data = rfm_data.join(data_recency, on="ID", how="outer")
print(rfm_data)

d = data.copy()
d["Year"] = data["Date"].apply(lambda d: d.year)
d = d.groupby("TypeOfIssue").agg(
    Amount=pd.NamedAgg("Amount", aggfunc="sum")).reset_index()
fig = px.pie(d, values='Amount', names='TypeOfIssue',
             title='Population of European continent')
fig.update_layout(
    autosize=False,
    width=600,
    height=600
)
fig.show()
