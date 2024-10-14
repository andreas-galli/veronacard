import numpy as np     # type: ignore

class Haversine:
    @staticmethod
    # Funzione per calcolare la distanza in km tra due coordinate
    def haversine(poi_coords, poi1, poi2): 
        R = 6371
        
        # Lat e long da gradi a radianti
        lat1, long1, lat2, long2 = map(np.radians, [poi_coords[poi1][0], poi_coords[poi1][1], poi_coords[poi2][0], poi_coords[poi2][1]])
    
        d_lat = lat2 - lat1
        d_long = long2 - long1
        
        # Formula Haversine
        a = np.sin(d_lat / 2)**2 + np.cos(lat1) * np.cos(lat2) * np.sin(d_long / 2)**2
        c = 2 * np.arcsin(np.sqrt(a))

        return R * c