#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Markov(object):
    def __init__(self):
        self.T = 0 # Length of the obsevation sequence
        self.N = 0 # Number of states in the model
        self.M = 0 # Number of observation symbols
        self.Q = list() # Distict states of the Markov process
        self.V = list() # Possible observations
        self.A = dict() # State transition probabilities
        self.B = dict() # Observation probability matrix
        self.PI = dict() # Initial state distribution
        self.O = list() # Observation sequence
        self.X = list() # State sequence (Hidden in HMM)

    def set_states(self, states):
        '''
        Set distinct states
        '''
        self.Q = states
        self.N = len(self.Q)
        return

    def get_states(self):
        '''
        Returns the distinct states
        '''
        return self.Q

    def set_observations(self, observations):
        '''
        Set possible observations
        '''
        self.V = observations
        self.M = len(self.V)
        return

    def get_observations(self):
        '''
        Returns the possible observations
        '''
        return self.V

    def set_state_transition_probabilities(self, probabilities):
        '''
        Sets the state transition probabilities.
        '''
        self.A = probabilities

    def get_state_transition_probabilities(self):
        '''
        Returns the state transition probabiliy matrix
        '''
        return self.A

    def set_observation_probabilities(self, probabilities):
        '''
        Sets the observation probabilities
        '''
        self.B = probabilities


    def get_observation_probability(self, state, observation):
        '''
        Returns the observation probabilities
        '''
        return self.B[state, observation]

    def set_initial_state_distribution(self, probabilities):
        '''
        Sets the intial state probability distribution
        '''
        self.PI = probabilities

    def get_initial_state_distribution(self):
        return self.PI

    def set_observation_sequence(self, sequence):
        '''
        Sets the observation sequence.
        '''
        self.O = sequence
        self.T = len(self.O)

    def get_observation_sequence(self):
        return self.O

    def get_sequence_length(self):
        return self.T

    def set_state_sequence(self, sequence):
        '''
        Sets the state sequence
        '''
        self.X = sequence

    def get_state_sequence(self):
        '''
        Gets the list of state sequences
        '''
        return self.X

    # DEBUGGING / PRINTING
    def display_observation_probabilities(self):
        print(self.B)
