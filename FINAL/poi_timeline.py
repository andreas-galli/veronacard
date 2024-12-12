import pandas as pd
import plotly.express as px
from matrices.matrix import *
from graphs.graph import *

# Generazione delle timeline dinamica rappresentante ogni giornata e il relativo cluster di appartenenza

df = pd.read_csv("log_veronaCard.csv")

clustering_data = pd.read_csv("results/2018/flussi/3_clusters/2018_WEIGHT_clustering.csv")

POIs = list(map(int, sorted(pd.read_csv("poi_info.csv").iloc[:, 0].values)))

# Da modificare in base a quanti cluster sono presenti nel file analizzato (3 cluster -> 3 colori, in questo caso specifico)
cluster_colors = {
    0: "lightblue",
    1: "orange",
    2: "green",
    #3: "yellow",
    #4: "red" 
}

clustering_data["COLOR"] = clustering_data.apply(lambda row: cluster_colors[row["CLUSTER"]], axis=1)

clustering_data["MOVEMENTS"] = ""

clustering_data["POI"] = ""

for index, row in clustering_data.iterrows():
    print(row["DATE"])
    matrix = Matrix.get_matrix(df[df.iloc[:, 0] == row["DATE"]], POIs)
    graph = Graph.get_graph(matrix, df[df.iloc[:, 0] == row["DATE"]])
    poi_list = sorted(list(map(int, graph.nodes)))
    n_mov = 0
    for (node1, node2, data) in graph.edges(data=True):
                n_mov += data['weight']
    clustering_data.at[index, "MOVEMENTS"] = n_mov
    clustering_data.at[index, "POI"] = ", ".join(map(str, poi_list))
    clustering_data.at[index, "HOLIDAY"] = "YES" if row["HOLIDAY"] == "YES" else "NO"
    
fig = px.scatter(
    clustering_data, x="DATE", y="CLUSTER", color="COLOR",
    title="2018 - Timeline Cluster e POI per ogni data - Flussi",
    labels={"DATE": "Data", "CLUSTER": "Cluster"},
    hover_data={"DATE": True, "MOVEMENTS": True, "CLUSTER": False, "POI": True, "HOLIDAY": True},
    color_discrete_map="identity"
)

fig.update_traces(marker=dict(size=8, opacity=0.7, line=dict(width=1, color="black")))
fig.update_xaxes(dtick="M1") 

fig.update_yaxes(
    tickmode="linear", tick0=0, dtick=1,         
    range=[-0.2, 2.2], # Da modificare in base al numero di cluster (3 cluster numerati da 0 a 2, in questo caso specifico)                   
    fixedrange=True                              
)
fig.update_layout(showlegend=False)

fig.show()