#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Direct_Method(object):
    def __init__(self, markov_model):
        self.name = 'Direct Method'
        self.model = markov_model

    def calculate_probability(self):

        # Gets a permutation of X
        for x in self.model.get_state_sequence():
            # Time
            t = 0

            state = x[t]
            observation = self.model.get_observation_sequence()[t]

            pi = self.model.get_initial_state_distribution()[state]
            b  = self.model.get_observation_probability(state, observation)

            t += 1
            while t < 

            #for observation in model.get_observation_sequence:
