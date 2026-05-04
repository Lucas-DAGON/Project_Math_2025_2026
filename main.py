# -*- coding: utf-8 -*-
"""
Created on Tue Oct 14 09:50:57 2025

@author: JDION
"""

import numpy as np
import matplotlib.pyplot as plt
from simulateur import SimulateurTraitement
from strategies import StrategieAleatoire, StrategieCyclique

def simulation(strategie, simulateur):
    """
    Exécute une simulation complète d'une stratégie sur un simulateur
    """
    N = simulateur.n_patients
    K = simulateur.n_traitements
    mapping = {i: chr(65+i) for i in range(K)}
    X = np.zeros(N)
    strategie.initialiser()
    for n in range(N):
        t = strategie.choisir_traitement()
        x = simulateur.administrer_traitement(mapping[t])
        strategie.mettre_a_jour(t, x)
        X[n] = x
    return X

def affiche_resultats(X, noms):
    """
    Affiche les courbes cumulées de patients guéris pour chaque stratégie.
    """
    plt.figure()
    for i, nom in enumerate(noms):
        plt.plot(np.cumsum(X[i]), label=nom)
    plt.legend()
    plt.xlabel("Patients")
    plt.ylabel("Nombre cumulé de guérisons")
    plt.title("Cumul de patients guéris")
    plt.grid(True, alpha=0.3)
    plt.show()

if __name__ == "__main__":
    repetitions = 5 # changé pour l'évaluation
    seed = 2025 # changé pour l'évaluation
    seeds = range(seed, seed + repetitions)
    
    sim_tmp = SimulateurTraitement(seed)
    N = sim_tmp.n_patients
    K = sim_tmp.n_traitements

    strategies = [
        StrategieAleatoire(K),
        StrategieCyclique(K)
    ]
    noms = ["Stratégie aléatoire", "Stratégie cyclique"]
    
    X = np.zeros((len(noms), N))

    for s in seeds:
        for i, strat in enumerate(strategies):
            sim = SimulateurTraitement(seed=s)
            X[i] += simulation(strat, sim)

    X /= len(seeds)

    affiche_resultats(X, noms)
    for i, nom in enumerate(noms):
        score = np.sum(X[i])
        print(f"{nom} : {score:.1f} / {N} patients guéris en moyenne")
        
        # Calcul l'esperance et la variance des strategie
        esperance = np.mean(X[i])
        variance = np.var(X[i])
        print(f"esperance {nom} = {esperance}\nvariance {nom} = {variance}")
    

            


