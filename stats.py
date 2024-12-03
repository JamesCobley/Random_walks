# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 13:46:01 2024

@author: cameron schmidt
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

class Stats: 
    def __init__ (self, filename= 'positions.csv'):
        self.filename= filename
        self.df= pd.read_csv(filename)
        self.msd= None
        self.rmsd= None
        
    def calculate_msd(self):
        squared_displacement= self.df['position'] ** 2
        self.msd= np.cumsum(squared_displacement / self.df['time'])
        
    def calculate_rmsd(self):
        self.rmsd= np.sqrt(self.msd)

class Plot: 
    '''Generates plots of desired features from the dataframe in the Stats class'''
    '''Stats class instantiated as stat_calc'''
    def __init__(self, stat_calc, save_dir= 'plots'):
        self.stat_calc= stat_calc
        self.save_dir= save_dir
        self.plot_style = 'dark_background' # See matplotlib docs for other styles
        
        # Check for save directory
        if not os.path.exists(self.save_dir):
            os.makedirs(self.save_dir)
            
    def plot_positions(self, save=True):
        plt.style.use(self.plot_style)
        plt.figure(figsize=(8,8))
        plt.plot(self.stat_calc.df['time'], self.stat_calc.df['position'], linewidth=1) 
        plt.title('Positions V. Time')
        plt.xlabel('Time (s)')
        plt.ylabel('Position')
        if save: 
            plt.savefig(os.path.join(self.save_dir, 'positions.png'))
        plt.show()
        
    def plot_msd(self, save=True):
        plt.style.use(self.plot_style)
        plt.figure(figsize=(8,8))
        plt.plot(self.stat_calc.df['time'], self.stat_calc.msd, linewidth=1) 
        plt.title('MSD V. Time')
        plt.xlabel('Time (s)')
        plt.ylabel('MSD (um^2)')
        if save: 
            plt.savefig(os.path.join(self.save_dir, 'msd.png'))
        plt.show()
        
    def plot_rmsd(self, save=True):
        plt.style.use(self.plot_style)
        plt.figure(figsize=(8,8))
        plt.plot(self.stat_calc.df['time'], self.stat_calc.rmsd, linewidth=1) 
        plt.title('RMSD V. Time')
        plt.xlabel('Time (s)')
        plt.ylabel('RMSD (um)')
        if save: 
            plt.savefig(os.path.join(self.save_dir, 'rmsd.png'))
        plt.show()