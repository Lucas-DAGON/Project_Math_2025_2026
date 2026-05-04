# -*- coding: utf-8 -*-
"""
Created on Tue Oct 14 09:49:57 2025

@author: JDION
"""

import numpy as np

class SimulateurTraitement:
    """
    Simule l'effet de plusieurs traitements sur un ensemble de patients.
    Chaque traitement a une certaine probabilité de succès (inconnue en théorie).
    """

    def __init__(self, seed, n_patients=1000):
        self.traitements = ['A', 'B', 'C', 'D', 'E']
        self.probabilites = {  # valeurs qui seront changées pour l'évaluation
            'A': 0.60,
            'B': 0.75,
            'C': 0.80,
            'D': 0.65,
            'E': 0.70
        }
        self.seed = seed
        self.n_patients = n_patients
        self.n_traitements = len(self.traitements)
        self.tirages = self.generer_tirages(seed)
        self.index = 0

    def generer_tirages(self, seed):
        """
        Génère à l'avance les résultats de tous les traitements pour tous les patients pour un seed donné (reproductibilité parfaite).
        """
        rng = np.random.default_rng(seed)
        n = self.n_patients
        k = self.n_traitements
        tirages = np.zeros((n, k), dtype=bool)
        for j, t in enumerate(self.traitements):
            tirages[:, j] = rng.random(n) < self.probabilites[t]
        return tirages

    def administrer_traitement(self, t):
        """
        Retourne le résultat (0 ou 1) du traitement t pour le patient courant.
        """
        if self.index >= self.n_patients:
            raise IndexError("Tous les patients ont déjà été traités.")
        idx = self.traitements.index(t)
        resultat = self.tirages[self.index, idx]
        self.index += 1
        return resultat
