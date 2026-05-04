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
        

class Bayesienne:
    """
    À compléter : définir votre propre algorithme de recommandation en fonction des succès/échecs précédents.
    Merci de ne pas modifier structure et noms !
    """

    def __init__(self, K):
        self.K = K
        self.m = 0
        self.n = 0
        self.index = 0

    def initialiser(self):
        self.index = 0

    def choisir_traitement(self):
        if (self.index == 0):
            pass
        else:
            pass

    def mettre_a_jour(self, traitement, succes):
        pass
