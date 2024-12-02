# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 13:40:51 2024

@author: SCHMIDTC18
"""

'''Runs the model'''

import argparse
from simulation import Simulation
#from stats import Stats
from plotting import Plot


def main(): 
    parser= argparse.ArgumentParser(description= 'Redox Proteoform Simulation')
    parser.add_argument('--run-simulate', action= 'store_true', help='run the simulation subprogram')
    parser.add_argument('--run-stats', action= 'store_true', help='run the stats subprogram')
    parser.add_argument('--run-plotting', action= 'store_true', help= 'run the plotting subprogram')
    args=  parser.parse_args()
    
    if args.run_simulate: # is True
        print('Running simulation.py ...')
        sim= Simulation(num_steps=1000)
        sim.random_walk()
        print('Running random walk ...')
        sim.save_positions()
        print('Saving positions ...')
        
    '''
    if args.run_stats: 
        print('Running stats.py ...')
        stats= Stats()
        stats.load_data()
    '''    
    if args.run_plotting:
        print('Running plotting.py ...')
        plot= Plot()
        plot.plot_positions()
        print('Plotting positions ...')

    print('Done!')

if __name__ == '__main__':
    main()