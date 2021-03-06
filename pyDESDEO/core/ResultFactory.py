# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
#
# Copyright (c) 2016  Vesa Ojalehto 
'''
'''
from optimization.OptimizationProblem import AchievementProblem

class ResultFactory(object):
    '''
    Brief Description


    Attributes
    ----------
    attr : type
        Descrption

    Methods
    -------
    method(c='rgb')
        Brief description, methods only for larger classes

    '''


    def __init__(self, params):
        '''
        Constructor
        '''

class BoundsFactory(ResultFactory):
    def __init__(self, optimization_method):
        '''
        '''
        self.optimization_method = optimization_method
    def result(self, prev_point,max=False):
        Phr = []
        for fi, fr in enumerate(prev_point):
            self.optimization_method.optimization_problem.obj_bounds = list(prev_point)
            self.optimization_method.optimization_problem.obj_bounds[fi] = None
            bound=self.optimization_method.search(max)
            if bound is None:
                Phr.append(prev_point[fi])
            else:
                Phr.append(bound[fi])

        return  Phr


class IterationPointFactory(ResultFactory):
    '''
    Brief Description


    Attributes
    ----------
    attr : type
        Descrption

    Methods
    -------
    method(c='rgb')
        Brief description, methods only for larger classes
    '''

    def __init__(self, optimization_method):
        '''
        '''
        self.optimization_method = optimization_method

    def result(self, preferences, q):
        self.optimization_method.optimization_problem.weights = preferences.weights()
        self.optimization_method.optimization_problem.reference = q
        self.last_solution = self.optimization_method.search()
        return  self.last_solution
