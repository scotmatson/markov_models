#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
An alpha pass (forward) algorithm to calculate a Markov Process.
'''
from decimal import Decimal

class Alpha_Pass(object):
    def __init__(self, markov_model):
        self.name = 'Alpha Pass'
        self.model = markov_model

    def calculate_probabilities(self):
        '''
        '''
        probability_sum = 0
        for observation_sequence in self.model.get_observation_sequence():
            print('Observation Sequence: ', observation_sequence)
            #desired_probability = 0
            t = 0
            alphas = dict()
            for i in range(self.model.get_number_of_states()):

                pi = self.model.get_initial_state_distribution()[self.model.get_states()[i]]
                print('pi', pi)
                b = self.model.get_observation_probability(
                    self.model.get_states()[i],
                    observation_sequence[t])
                print('b', b)
                product = float(pi) * float(b)
                alphas[(t, i)] = product
                #desired_probability += product
                print((t, i), '=', Decimal(product).quantize(Decimal('1e-6')))

            t += 1
            for t in range(t, self.model.get_sequence_length()):
                for i in range(self.model.get_number_of_states()):
                    alpha = 0
                    for j in range(self.model.get_number_of_states()):
                        a = self.model.get_state_transition_probability(
                            self.model.get_states()[j],
                            self.model.get_states()[i])
                        alpha += (float(a) * alphas[(t-1, j)])

                    b = self.model.get_observation_probability(
                        self.model.get_states()[i],
                        observation_sequence[t])

                    product = float(b) * alpha
                    alphas[(t, i)] = product
                    #desired_probability += product
                    print((t, i), '=', Decimal(product).quantize(Decimal('1e-6')))

            desired_probability = 0
            for i in range(self.model.get_number_of_states()):
                desired_probability += alphas[(self.model.get_sequence_length()-1 , i)]

            probability_sum += desired_probability
            print('Desired Probability: ',
                Decimal(desired_probability).quantize(Decimal('1e-6')))
        print('Probability Sum: ',
            Decimal(probability_sum).quantize(Decimal('1e-6')))
