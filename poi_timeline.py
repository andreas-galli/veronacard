import pandas as pd
import plotly.express as px
from matrix import *
from graph import *

df = pd.read_csv("log_veronaCard.csv")

# M
clustering_data = pd.read_csv("results_v3/2017/flussi/5_clusters/2017_WEIGHT_clustering.csv")

POIs = list(map(int, sorted(pd.read_csv("poi_info.csv").iloc[:, 0].values)))

# M
cluster_colors = {
    0: "lightblue",
    1: "orange",
    2: "green",
    3: "yellow",
    4: "red" 
}

clustering_data["COLOR"] = clustering_data.apply(lambda row: cluster_colors[row["CLUSTER"]], axis=1)

clustering_data["POI"] = ""

for index, row in clustering_data.iterrows():
    print(row["DATE"])
    matrix = Matrix.get_matrix(df[df.iloc[:, 0] == row["DATE"]], POIs)
    graph = Graph.get_graph(matrix, df[df.iloc[:, 0] == row["DATE"]])
    poi_list = sorted(list(map(int, graph.nodes)))
    clustering_data.at[index, "POI"] = ", ".join(map(str, poi_list))
    clustering_data.at[index, "HOLIDAY"] = "YES" if row["HOLIDAY"] == "YES" else "NO"
    
fig = px.scatter(
    clustering_data, x="DATE", y="CLUSTER", color="COLOR",
    title="2017 - Timeline Cluster e POI per ogni data - Flussi", # M
    labels={"DATE": "Data", "CLUSTER": "Cluster"},
    hover_data={"DATE": True, "CLUSTER": False, "POI": True, "HOLIDAY": True},
    color_discrete_map="identity"
)

fig.update_traces(marker=dict(size=8, opacity=0.7, line=dict(width=1, color="black")))
fig.update_xaxes(dtick="M1") 

# M:
fig.update_yaxes(
    tickmode="linear", tick0=0, dtick=1,         
    range=[-0.2, 4.2],                           
    fixedrange=True                              
)
fig.update_layout(showlegend=False)

fig.show()