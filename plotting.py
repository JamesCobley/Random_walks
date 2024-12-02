# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 13:46:01 2024

@author: cameron schmidt
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

class Plot: 
    def __init__(self, filename= 'positions.csv', save_dir= 'plots'):
        self.filename= filename
        self.df= pd.read_csv(filename) # Specified in main()
        self.msd= None
        self.rmsd= None
        self.save_dir= save_dir
        self.plot_style = 'dark_background' # See matplotlib docs for other styles
        
        # Check for save directory
        if not os.path.exists(self.save_dir):
            os.makedirs(self.save_dir)
            
    def plot_positions(self, save=True):
        plt.style.use(self.plot_style)
        plt.figure(figsize=(8,8))
        plt.plot(self.df['time'], self.df['position'], linewidth=1) 
        plt.title('Positions V. Time')
        plt.xlabel('Time (s)')
        plt.ylabel('Position')
        if save: 
            plt.savefig(os.path.join(self.save_dir, 'positions.png'))
        plt.show()