# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 13:40:51 2024

@author: SCHMIDTC18
"""

'''Runs the python scripts'''

import argparse
from simulation import Simulation
from stats import Stats
from plotting import Plot


def main(): 
    parser= argparse.ArgumentParser(description= 'Redox Proteoform Simulation')
    parser.add_argument('--sumulate', action= 'store_true', help='run the simulation subprogram')
    parser.add_argument('--stats', action= 'store_true', help='run the stats subprogram')
    parser.add_argument('--plotting', action= 'store_true', help= 'run the plotting subprogram')
    args=  parser.parse_args()
    
    if args.simulate: # is True
        print('Running simulation.py ...')
        sim= Simulation()
        sim.generate_random_walk()
        sim.save_to_csv()
    
    if args.stats: 
        print('Running stats.py ...')
        stats= Stats()
        stats.load_data()
        
    if args.plotting:
        print('Running plotting.py ...')
        plot= Plot()
        plot.load_data()
        plot.plot_data()
        
if __name__ == '__main__':
    main()