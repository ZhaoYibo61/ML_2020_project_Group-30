
import numpy as np
import pickle

with open('input/datasets_from_paper/ele_1096.npy', 'rb') as file:
      dataset_ele_1096 = pickle.load(file).T

hyperparam_ele_1096 = {

  'BHTARIMA':

  {
        'dataset': 'ele_1096',
        'p': 3,
        'd': 2,
        'q': 1,
        'taus': [321, 20],
        'Rs': [5, 5],
        'k': 15,
        'tol': 0.001,
        'testsize': 0.1,
        'loop_time': 5,
        'info': 'v2',
        'Us_mode': 1,

    },


  'ARIMA':

    {  
        'testsize': 0.1,
        'order': [3, 1, 1]
    },

 'Prophet':

    {

        'testsize': 0.1,
        'start' : '2012-1',
        'freq' : 'D'

    }
    




}