#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
An alpha pass (forward) algorithm to calculate a Markov Process.
'''
class Alpha_Pass(object):
    def __init__(self, markov_model):
        self.name = 'Alpha Pass'
        self.model = markov_model

    def calculate_probabilities(self):
        '''
        '''
        desired_probability = 0
        t = 0
        alphas = dict()
        for i in range(self.model.get_number_of_states()):

            pi = self.model.get_initial_state_distribution()[self.model.get_states()[i]]
            b = self.model.get_observation_probability(
                self.model.get_states()[i],
                self.model.get_observation_sequence()[t])
            product = float(pi) * float(b)
            alphas[(t, i)] = product
            desired_probability += product
            print((t, i), '=', product)

        t += 1
        for t in range(t, self.model.get_sequence_length()):
            for i in range(self.model.get_number_of_states()):
                alpha = 0
                for j in range(self.model.get_number_of_states()):
                    a = self.model.get_state_transition_probability(
                        self.model.get_states()[j],
                        self.model.get_states()[i])
                    #print('alphas',alphas[(t-1, j)])
                    #print('a',a)
                    alpha += (float(a) * alphas[(t-1, j)])
                    #print('alpha',alpha)

                b = self.model.get_observation_probability(
                    self.model.get_states()[i],
                    self.model.get_observation_sequence()[t])

                product = float(b) * alpha
                alphas[(t, i)] = product
                desired_probability += product
                print((t, i), '=', product)
        print('Desired Probability: ', desired_probability)
