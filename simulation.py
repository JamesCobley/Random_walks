# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 13:38:40 2024

@author: SCHMIDTC18
"""

'''Class for simulating Cysteine Oxidation States Using Random Walks'''

import pandas as pd
import numpy as np
 
class Simulation:
    def __init__(self, steps= 100, output_file= 'data/random_walk.csv'):
        self.steps= steps
        self.output_file= output_file
        self.data= []
         
         
