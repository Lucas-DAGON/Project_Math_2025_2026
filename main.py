# -*- coding: utf-8 -*-
"""
Created on Tue Oct 14 09:50:57 2025

@author: JDION
"""

import numpy as np
import matplotlib.pyplot as plt
from simulateur import SimulateurTraitement
from strategies_gp10 import StrategieAleatoire, StrategieCyclique

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

        # Strategie 1 et 2
        # Calcul l'esperance et la variance des strategie
        esperance = np.mean(X[i])
        variance = np.var(X[i])
        print(f"esperance {nom} = {esperance}\nvariance {nom} = {variance}")

        # Strategie 3
        # Peut etre expliquer avec la loi student
        if nom == "Stratégie cyclique":
            # Extract first 30 results for each treatment (every K-th element starting from position j)
            x_A = X[i][0:30*K:K]  # Treatment A: first 30 values at positions 0, K, 2K, ...
            x_B = X[i][1:30*K:K]  # Treatment B: first 30 values at positions 1, K+1, 2K+1, ...
            x_C = X[i][2:30*K:K]  # Treatment C: first 30 values at positions 2, K+2, 2K+2, ...
            x_D = X[i][3:30*K:K]  # Treatment D: first 30 values at positions 3, K+3, 2K+3, ...
            x_E = X[i][4:30*K:K]  # Treatment E: first 30 values at positions 4, K+4, 2K+4, ...
            
            print(f"esperance {nom} A = {np.mean(x_A)}\nvariance {nom} A = {np.var(x_A)}")
            print(f"esperance {nom} B = {np.mean(x_B)}\nvariance {nom} B = {np.var(x_B)}")
            print(f"esperance {nom} C = {np.mean(x_C)}\nvariance {nom} C = {np.var(x_C)}")
            print(f"esperance {nom} D = {np.mean(x_D)}\nvariance {nom} D = {np.var(x_D)}")
            print(f"esperance {nom} E = {np.mean(x_E)}\nvariance {nom} E = {np.var(x_E)}")
            

            


