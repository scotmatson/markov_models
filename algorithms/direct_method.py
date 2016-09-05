#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Direct_Method(object):
    def __init__(self, markov_model):
        self.name = 'Direct Method'
        self.model = markov_model
        self.probability_expressions = None
        self.desired_probability = None

    def build_expressions(self):
        self.probability_expressions = dict()
        # Gets a permutation of X
        for x in self.model.get_state_sequence():
            expression = list()
            t = 0 # Time

            current_state = x[t]
            current_observation = self.model.get_observation_sequence()[t]

            pi = self.model.get_initial_state_distribution()[current_state]
            b  = self.model.get_observation_probability(
                current_state, current_observation)
            expression += [float(pi), float(b)]

            t += 1
            for i in range(t, self.model.get_sequence_length()):
                previous_state = current_state
                current_state = x[i]
                current_observation = self.model.get_observation_sequence()[i]

                a = self.model.get_state_transition_probability(previous_state, current_state)
                b  = self.model.get_observation_probability(
                    current_state, current_observation)
                expression += [float(a), float(b)]
            self.probability_expressions[x] = expression

    def calculate_probabilities(self):
        self.desired_probability = 0
        for o, x in self.probability_expressions.items():
            if x:
                product = x[0]
            for multiplicand in x[1:]:
                product *= multiplicand

            self.desired_probability += product
            print(o, '=', product)
        print('Desired Probability: ', self.desired_probability)
