from flask import Flask, render_template, request
import graph
import route
import pandas as pd
import numpy as np
import param
from tsp_ga import TSP_GA
import fol


cls_graph = graph.Graph()
        
# cls_graph.main_graph(aleatoire=False)

# heuristique de départ : 
route, distance = cls_graph.heuristique()

distance = round(distance, 2)


fol.carte()   # créer la carte heuristique



app = Flask(__name__)



@app.route('/', methods = ['GET','POST'])
def home():

    global route
    global distance
    iframe2 = False
    distance2 = ""
    distance_in = ""
    

    

    if request.form:
        # recalculer une meilleure route
        res = request.form['test']

        with open('route.txt', 'r') as f:
            route_enr = f.readlines()[0]
        with open('distance.txt', 'r') as f:
            distance_enr = float(f.readlines()[0])
        
        route_enr_liste = []
        for i in route_enr.split(','):
            if i != "":
                route_enr_liste.append(int(i))

        cls_ga = TSP_GA(route_enr_liste, distance_enr)
        reponse = cls_ga.run(10)               
        distance2 = reponse[0]
        distance_in = reponse[1]                  # distance
        route_heuristique = reponse[3]         # route
        df = reponse[2]      
        fol.carte_opt()
        iframe2 = True

        route_string = str(route_heuristique[0])
        for i in range(1,len(route_heuristique)):
            route_string = route_string + ',' + str(route_heuristique[i])
        with open('route.txt', 'w') as f:
            f.write(route_string)
        with open('distance.txt', 'w') as f:
            f.write(str(distance2))



    else:
        # créer une première route optimisée
        cls_ga = TSP_GA(route, distance)
        reponse = cls_ga.run(10)               
        distance2 = reponse[0]
        distance_in = reponse[1]                  # distance
        route_heuristique = reponse[3]         # route
        df = reponse[2]      
        fol.carte_opt()
        iframe2 = True

        route_string = str(route_heuristique[0])
        for i in range(1,len(route_heuristique)):
            route_string = route_string + ',' + str(route_heuristique[i])
        with open('route.txt', 'w') as f:
            f.write(route_string)
        with open('distance.txt', 'w') as f:
            f.write(str(distance2))

       
    distance2 = round(((float(distance2)/float(distance*100))),4)

    return render_template('index.html', iframe2=iframe2, distance=str(distance), distance2=str(distance2))


@app.route('/carte')
def carte():

    
    return render_template('maCarte.html')
    


@app.route('/carteopt')
def carteopt():

    
    return render_template('maCarte2.html')
    
