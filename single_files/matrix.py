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
                    matrix.loc[poi_prec, poi_succ] += 1
        return matrix
    
    def get_GED_matrix_from_csv(filename):
        df = pd.read_csv(filename)
        dates = sorted(df.iloc[:, 0].unique())
        matrix = pd.DataFrame(0, dates, dates)

        for row, i in df.iterrows():
            date1 = df.iloc[row, 0]
            date2 = df.iloc[row, 1]
            value = round(df.iloc[row, 2])
            matrix.loc[date1, date2] = value
            matrix.loc[date2, date1] = value
        return matrix
    
    def get_WEIGHT_matrix_from_csv(filename):
        df = pd.read_csv(filename)
        dates = sorted(df.iloc[:, 0].unique())
        matrix = pd.DataFrame(0, dates, dates)
        min = df.iloc[:, 3].min()
        max = df.iloc[:, 3].max()
        for row, i in df.iterrows():
            date1 = df.iloc[row, 0]
            date2 = df.iloc[row, 1]
            #x_norm = (df.iloc[row, 3] - min) / (max - min)
            matrix.loc[date1, date2] = df.iloc[row, 3]
            matrix.loc[date2, date1] = df.iloc[row, 3]
        return matrix
    
    def get_GED_WEIGHT_matrix_from_csv(filename):
        df = pd.read_csv(filename)
        dates = sorted(df.iloc[:, 0].unique())
        matrix = pd.DataFrame(0, dates, dates)
        minWeight = df.iloc[:, 3].min()
        maxWeight = df.iloc[:, 3].max()
        minGed = df.iloc[:, 2].min()
        maxGed = df.iloc[:, 2].max()
        for row, i in df.iterrows():
            date1 = df.iloc[row, 0]
            date2 = df.iloc[row, 1]
            weight_norm = (df.iloc[row, 3] - minWeight) / (maxWeight - minWeight)
            ged_norm = (df.iloc[row, 2] - minGed) / (maxGed - minGed)
            value = weight_norm + ged_norm
            matrix.loc[date1, date2] = value
            matrix.loc[date2, date1] = value
        return matrix