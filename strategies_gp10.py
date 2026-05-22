# -*- coding: utf-8 -*-
"""
Created on Tue Oct 14 09:50:37 2025

@author: JDION
"""

import numpy as np

class StrategieAleatoire:
    """
    Choisit un traitement au hasard.
    """
    
    def __init__(self, K): 
        self.K = K
        
    def initialiser(self):
        pass
    
    def choisir_traitement(self):
        return np.random.randint(0, self.K)
    
    def mettre_a_jour(self, k, r):
        pass
    

class StrategieCyclique:
    """
    Choisit le traitement de façon cyclique : les uns à la suite des autres.
    """
    
    def __init__(self, K):
        self.K = K
        self.index = 0

    def initialiser(self):
        self.index = 0

    def choisir_traitement(self):
        return self.index % self.K

    def mettre_a_jour(self, traitement, succes):
        self.index += 1
        

class MaStrategie:
    """
    Algorithme Thompson Sampling avec distribution Beta pour chaque traitement.
    """

    def __init__(self, K):
        self.K = K
        self.alpha = np.ones(K)
        self.beta = np.ones(K)
        self.historique_traitements = []
        self.historique_resultats = []

    def initialiser(self):
        self.alpha = np.ones(self.K)
        self.beta = np.ones(self.K)
        self.historique_traitements = []
        self.historique_resultats = []

    def choisir_traitement(self):
        theta = np.random.beta(self.alpha, self.beta)
        traitement = np.argmax(theta)
        self.historique_traitements.append(traitement)
        return traitement

    def mettre_a_jour(self, traitement, succes):
        self.historique_resultats.append(succes)
        if succes:
            self.alpha[traitement] += 1
        else:
            self.beta[traitement] += 1