# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 17:54:46 2022

@author: Adriano Vale
"""

import numpy as np

entradas = np.array([[0,0], [0,1], [1,0], [1,1]])
saídas = np.array([0, 0, 0, 1])
pesos = np.array((0.0, 0.0))
taxaAprendizagem = 0.1

def stepFunction(soma):
    if(soma >= 1):
        return 1
    return 0

def cauculaSaida(registro):
    s = registro.dot(pesos)
    return stepFunction(s)
def treinar():
    return 0