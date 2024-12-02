# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 13:38:40 2024

@author: SCHMIDTC18
"""

'''Class for simulating Cysteine Oxidation States Using Random Walks'''

import pandas as pd
import numpy as np
 
class Simulation:
    def __init__(self, num_steps= 100):
        self.num_steps= num_steps
        self.time_step= 0.1 # time required for each step
        self.steps= [0]
        self.position= [0]
        self.time= [0]
        
    def random_walk(self): 
        '''Simple 1D random walk to start'''
        self.steps=np.random.choice([-1, 1], size=self.num_steps)
        self.time= np.arange(1, self.num_steps+1) * self.time_step
        self.position=np.cumsum(self.steps)
        
    def save_positions(self, output_file= 'positions.csv'): 
        '''store the step magnitudes/directions, time, and positions as a pandas dataframe'''
        df=pd.DataFrame({'step': self.steps, 'time': self.time, 'position': self.position})
        
        # write data to .csv
        df.to_csv(output_file, index= False)
         
