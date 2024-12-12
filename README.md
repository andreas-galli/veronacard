# Analisi Dataset VeronaCard
Questo progetto analizza i dati degli spostamenti dei turisti a Verona, fornendo strumenti utili all'analisi di questi.

## Di seguito la struttura del progetto e le funzionalità dei vari file:

```
veronacard/
├── 2017_timelines/                                    # Contiene qualche timeline generata dell'anno 2017
│
├── 2018_timelines/                                    # Contiene qualche timeline generata dell'anno 2018
│
├── first3mov/                                         # Analisi primi 3 movimenti più presenti in ogni cluster
│
├── first4mov/                                         # Analisi primi 4 movimenti più presenti in ogni cluster
│
├── graphs/                                            # Funzioni per la gestione dei grafi
│   ├── graph_similarity.py                            # Funzioni per il calcolo della similarità
│   └── graph.py                                       # Funzioni per creazione e visualizzazione di grafi
│
├── matrices/                                          # Funzioni e script per la gestione delle matrici
│   ├── GED_distanceMatrix.py                          # Generazione matrice distanze, metrica Graph Edit Distance
│   ├── matrix.py                                      # Funzioni per generare matrici
│   └── WEIGHT_distanceMatrix.py                       # Generazione matrice distanze, metrica absolute_distance
│
├── results/                                           # Cartella in cui sono contenuti i csv utili al clustering
│   ├── 2017/                                           
│   │   ├── flussi/                                    # Risultati dell'anno 2017, misura di similarità absolute_distance
│   │   │   ├── 3_clusters/                            
│   │   │   │   └── 2017_WEIGHT_clustering.csv         # Risultati clustering anno 2017, absolute_distance
│   │   │   ├── 2017_WEIGHT_distanceMatrix.csv         # Matrice delle distanze, anno 2017, absolute_distance
│   │   │   └── 2017_WEIGHT_elbow.png                  # Immagine raffigurante il gomito (scelta n cluster)
│   │   ├── struttura/                                 # Risultati dell'anno 2017, misura Graph Edit Distance
│   │   │   ├── 3_clusters/                            
│   │   │   │   └── 2017_GED_clustering.csv            # Risultati clustering anno 2017, Graph Edit Distance
│   │   │   ├── 2017_GED_distanceMatrix.csv            # Matrice delle distanze, anno 2017, Graph Edit Distance
│   │   │   └── 2017_GED_elbow.png                     # Immagine raffigurante il gomito (scelta n cluster)
│   │   └── 2017_results.csv                           # Risultati confronti date anno 2017
│   ├── 2018/                                           
│       ├── flussi/                                    # Risultati dell'anno 2018, misura di similarità absolute_distance
│       │   ├── 3_clusters/                            
│       │   │   └── 2018_WEIGHT_clustering.csv         # Risultati clustering anno 2018, absolute_distance
│       │   ├── 2018_WEIGHT_distanceMatrix.csv         # Matrice delle distanze, anno 2018, absolute_distance
│       │   └── 2018_WEIGHT_elbow.png                  # Immagine raffigurante il gomito (scelta n cluster)
│       ├── struttura/                                 # Risultati dell'anno 2018, misura Graph Edit Distance
│       │   ├── 3_clusters/                            
│       │   │   └── 2018_GED_clustering.csv            # Risultati clustering anno 2018, Graph Edit Distance
│       │   ├── 2018_GED_distanceMatrix.csv            # Matrice delle distanze, anno 2018, Graph Edit Distance
│       │   └── 2018_GED_elbow.png                     # Immagine raffigurante il gomito (scelta n cluster)
│       └── 2018_results.csv                           # Risultati confronti date anno 2018
│
├── clustering.py                                      # Clustering secondo K-Means
├── firstNMovements.py                                 # Genera csv contenente i primi 3 spostamenti fatti per ogni id_vc 
├── generate_results.csv                               # Generazione file 'AAAA_results.csv'
├── log_veronaCard.csv                                 # Dataset di partenza, contenente le strisciate
├── main.py                                            # Test di alcune funzionalità ed esecuzione del clustering
├── poi_info.csv                                       # Contiene la lista dei POI e alcune informazioni su di essi
├── poi_timeline.py                                    # Generazione di una timeline, parametri da impostare
└── README.md                                          # Questo file
```
