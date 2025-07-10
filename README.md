# Analisi Dataset VeronaCard
Questo progetto analizza i dati degli spostamenti dei turisti a Verona tra i vari punti di interesse e si basa sull'analisi del dataset **veronacard**, che tiene traccia delle strisciate dei turisti presso i punti di interesse della città di Verona.  
La scelta è stata quella di rappresentare le giornate sottoforma di grafi, che come nodi hanno i punti di interesse, come archi il numero di spostamenti tra i punti di interesse.
La versione finale introduce l'embedding dei grafi mediante l'utilizzo della libreria PyTorch Geometric e di una Graph Neural Network, che trasforma un grafo in un embedding, per poi procedere al clustering, con il tentativo di ottenere dei cluster che godono di una buona separazione.  
Il Jupyter Notebook descrive il lavoro eseguito in modo dettagliato.
## Di seguito la struttura del progetto e le funzionalità dei vari file:

```
veronacard/
├── csv_files/                                         # Dataset veronacard e altri file utili
│
├── results+distance/2018                              # Risultati dei clustering, embeddings e timelines del 2018
│
├── results/2018                                       # Come i precedenti, senza considerare la distanza tra POI nell'embedding
│
├── saved_graphs/                                      # Grafi salvati in formato .pkl per evitare la loro ripetuta generazione 
│
├── single_files/                                      # Immagini e file .py importati all'interno del Jupyter Notebook
│
├── vc_embedding_GNN_+POIdistance.ipynb                # Jupyter Notebook con accurata descrizione di ogni operazione eseguita
│
├── versione_precedente.zip                            # Versione precedente del progetto, che non prevedeva l'embedding dei grafi
│ 
└── README.md                                          # Questo file
```
## Autore
Progetto sviluppato da Andreas Galli, valido come progetto di tesi presso l'Università di Verona (2025).  

Email istituzionale: **andreas.galli@studenti.univr.it**

Email personale: **andreasgll2003@gmail.com**



