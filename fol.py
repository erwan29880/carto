import folium
import pandas as pd
import numpy as np
import param


def carte():


    data = pd.read_csv(param.FICHIER_CSV_COOR_INSEE)
    data_heuristique = pd.read_csv(param.LIEUX_CSV_HEURISTIQUE)

    c= folium.Map(location=[46.788830, 1.997873], zoom_start=6)


    points = []

    for i in range(param.NB_LIEUX):
        texte = data.loc[i, 'name']
        latitude = data.loc[i, 'latitude']
        longitude = data.loc[i, 'longitude']
        
        folium.Marker((latitude, longitude), popup=texte).add_to(c)
        
        latitude = data_heuristique.loc[i, 'x']
        longitude = data_heuristique.loc[i, 'y']
        points.append((latitude, longitude))


    points.append((data_heuristique.loc[0, 'x'], data_heuristique.loc[0, 'y']))
    folium.PolyLine(points, color='red').add_to(c)

    c.save('./templates/maCarte.html')
    
  

def carte_opt():
    

    data = pd.read_csv(param.FICHIER_CSV_COOR_INSEE)
    df = pd.read_csv(param.ROUTE_OPTIMISEE)

    c= folium.Map(location=[46.788830, 1.997873], zoom_start=6)


    points = []

    for i in range(param.NB_LIEUX):
        texte = data.loc[i, 'name']
        latitude = data.loc[i, 'latitude']
        longitude = data.loc[i, 'longitude']
        
        folium.Marker((latitude, longitude), popup=texte).add_to(c)
        
        latitude = df.loc[i, 'x']
        longitude = df.loc[i, 'y']
        points.append((latitude, longitude))


    points.append((df.loc[0, 'x'], df.loc[0, 'y']))
    folium.PolyLine(points, color='red').add_to(c)

    c.save('./templates/maCarte2.html')
    