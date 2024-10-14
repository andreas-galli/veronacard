import numpy as np                  
import pandas as pd

class Matrix:
    def get_matrix(df, POIs):
        # Mantengo solo le tuple aventi ID che compare più di una volta nel dataset
        counter = df[df.columns[1]].value_counts()
        multiple_IDs = counter[counter > 1].index
        df = df[df[df.columns[1]].isin(multiple_IDs)]

        # Ordino il DataFrame per ID e a parità di ID per timestamp
        df = df.sort_values(by=[df.columns[1], df.columns[2]])
        
        # Per ogni POI creo un nodo
        matrix = pd.DataFrame(0, POIs, POIs)

        for id_value in multiple_IDs:
            # Itero solo su tuple aventi stesso ID
            same_ID = df[df.iloc[:, 1] == id_value]
            
            # Itero sulle righe adiacenti
            for i in range(len(same_ID) - 1):
                poi_prec = same_ID.iloc[i, 4]
                poi_succ = same_ID.iloc[i + 1, 4]
                
                # Se il POI è differente dal successivo incremento il peso dell' "arco"
                if poi_prec != poi_succ:
                    """ 1 2
                    1   0 5       5 persone da POI 1 a POI 2 
                    2   8 0       8 persone da POI 2 a POI 1
                    """
                    matrix.loc[poi_prec, poi_succ] += 1
        return matrix