#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
An direct method algorithm to calculate a Markov Process.
'''
from decimal import Decimal

class Direct_Method(object):
    def __init__(self, markov_model):
        self.name = 'Alpha Pass'
        self.model = markov_model

    def calculate_probabilities(self):
        probability_sum = 0
        for observation_sequence in self.model.get_observation_sequence():
            print('Observation Sequence: ', observation_sequence)
            desired_probability = 0
            for x in self.model.get_state_sequence():
                expression = list()
                t = 0

                current_state = x[t]
                current_observation = observation_sequence[t]

                pi = self.model.get_initial_state_distribution()[current_state]
                b  = self.model.get_observation_probability(
                    current_state, current_observation)
                product = float(pi) * float(b)

                t += 1
                for i in range(t, self.model.get_sequence_length()):
                    previous_state = current_state
                    current_state = x[i]
                    current_observation = observation_sequence[i]

                    a = self.model.get_state_transition_probability(
                        previous_state, current_state)
                    b  = self.model.get_observation_probability(
                        current_state, current_observation)
                    product *= float(a) * float(b)
                desired_probability += product
                print(x, '=', Decimal(product).quantize(Decimal('1e-6')))
            probability_sum += desired_probability
            print('Desired Probability: ',
                Decimal(desired_probability).quantize(Decimal('1e-6')))
        print('Probability Sum: ',
            Decimal(probability_sum).quantize(Decimal('1e-6')))
