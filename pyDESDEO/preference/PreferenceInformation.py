# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

# Copyright (c) 2016  Vesa Ojalehto <vesa.ojalehto@gmail.com>
'''
Module description
'''

from abc import ABCMeta, abstractmethod
import numpy as np

class PreferenceInfomration(object):
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
    __metaclass__ = ABCMeta


    def __init__(self, params):
        '''
        Constructor
        '''
    def weights(self):
        ''' Return weight vector corresponding to the given preference information
        '''

class Direction(object):
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

class DirectSpecification(Direction):
    '''
     '''

    def __init__(self, direction):
        '''
        Constructor
        '''

        self.direction = direction

    def weights(self):
        return 1. / np.array(self.direction)


class RelativeRanking(Direction):
    '''
     '''

    def __init__(self, ranking):
        '''
        Constructor
        '''

        self.ranking = ranking

    def weights(self):
        return 1. / np.array(self.ranking)


class PreferredPoint(object):
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