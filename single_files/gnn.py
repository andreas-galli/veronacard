import torch.nn as nn
import torch
import torch.nn.functional as F
from torch_geometric.data import Data, Batch
from torch_geometric.nn import GATConv, global_add_pool, global_mean_pool, global_max_pool
import networkx as nx


class GraphEmbeddingModel(nn.Module):
    def __init__(self, in_dim, hidden_dim, out_dim, heads=4):
        super().__init__()
        self.conv1 = GATConv(in_dim, hidden_dim, heads=heads, concat=True, edge_dim=1)
        self.conv2 = GATConv(hidden_dim * heads, hidden_dim, heads=heads, concat=True, edge_dim=1)
        self.conv3 = GATConv(hidden_dim * heads, hidden_dim, heads=heads, concat=True, edge_dim=1)
        self.conv4 = GATConv(hidden_dim * heads, out_dim, heads=1, concat=False, edge_dim=1)
        self.pool = global_add_pool  # Usiamo global_add_pool invece della media

    def forward(self, data):
        # Calcoliamo un "peso" per ogni arco in base alla differenza
        edge_weight = data.edge_attr
        edge_weight = edge_weight / edge_weight.max()  # Normalizzazione
        edge_weight_attention = torch.exp(-torch.abs(edge_weight - edge_weight.mean()))  # Attenzione basata sulla differenza dei flussi

        x = self.conv1(data.x, data.edge_index, edge_attr=edge_weight * edge_weight_attention)
        x = F.leaky_relu(x)
        x = self.conv2(x, data.edge_index, edge_attr=edge_weight * edge_weight_attention)
        x = F.leaky_relu(x)
        x = self.conv3(x, data.edge_index, edge_attr=edge_weight * edge_weight_attention)
        x = F.leaky_relu(x)
        x = self.conv4(x, data.edge_index, edge_attr=edge_weight * edge_weight_attention)
        x = self.pool(x, data.batch)
        return x


def graph_to_pyg_data(graph, structure_weight):
    # Rinumeriamo i nodi per garantire indici continui
    graph = nx.convert_node_labels_to_integers(graph)

    # Estrai edge_index (arcs) e edge_weight (pesi sugli archi)
    edge_index = torch.tensor(list(graph.edges)).t().contiguous()
    edge_weight = torch.tensor([graph[u][v]["weight"] for u, v in graph.edges], dtype=torch.float)

    # Normalizzazione dei pesi sugli archi (se necessario)
    #edge_weight = edge_weight / edge_weight.max()  # Normalizza tra 0 e 1

    # Aggiungi il peso della struttura (1 per gli archi esistenti)
    structure_weight_tensor = torch.ones(edge_weight.shape)  # Peso struttura (1 per ogni arco)
    structure_weight_tensor = structure_weight_tensor * (1 - structure_weight)  # Rende il peso della struttura inversamente proporzionale

    # Modifica combinazione pesi: evidenzia la differenza di flusso
    diff_weight = torch.abs(edge_weight - edge_weight.mean())  # Differenza assoluta tra flusso e media
    combined_weight = structure_weight_tensor + (diff_weight * structure_weight)

    # Creare un embedding dummy per i nodi
    x = torch.ones((graph.number_of_nodes(), 1))

    return Data(x=x, edge_index=edge_index, edge_attr=combined_weight, num_nodes=graph.number_of_nodes())


