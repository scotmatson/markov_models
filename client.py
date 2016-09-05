#!/usr/bin/env python
# -*- coding: utf-8 -*-

import itertools
from markov import Markov
import algorithms

def display_help():
    ''' Displays the help menu '''
    print('Please make a selection from the following list of options:')
    print('(Q) - Set a distinct list of states for the Markov Process')
    print('(V) - Set a list of possible observations')
    print('(A) - Set state transition probabilities')
    print('(B) - Set observation probabilities')
    print('(P) - Set initial state distribution')
    print('(O) - Set observation sequence')
    print('(X) - Set state sequence permutations')
    print('(S) - Select algorithm')
    print('(R) - Run algorithm')
    print('(H) - Display help')
    print('(E) - Terminate execution')

def display_algorithms():
    print('Select one of the following algorithms:')
    print('(1) - Direct Method')
    print('(2) - Alpha Pass')

def create_probability_matrix(header_states, row_states):
    '''
    Creates a probability distribution matrix
    '''
    matrix = dict()
    for row_state in row_states:
        for header_state in header_states:
            matrix[(row_state, header_state)] = input(
                '%s -> %s = ' % (row_state, header_state))
    return matrix

def main():
    ''' Application entry point '''

    model = Markov()
    algorithm = None

    display_help()
    while True:
        action = input('>> ').lower()

        if action == 'q':
            print('Enter states of the Markov Process [comma delimited]')
            states = [state.strip() for state in input().split(',')]
            model.set_states(states)
        elif action == 'v':
            print('Enter possible observations [comma delimited]')
            observations = [observation.strip() for observation in input().split(',')]
            model.set_observations(observations)
        elif action == 'a':
            print('Enter state probability distribution')
            # Transition probabilities
            matrix = create_probability_matrix(
                model.get_states(),
                model.get_states())
            model.set_state_transition_probabilities(matrix)
        elif action == 'b':
            print('Enter observation probability distribution')
            matrix = create_probability_matrix(
                model.get_observations(),
                model.get_states())
            model.set_observation_probabilities(matrix)
        elif action == 'p':
            print('Enter initial state distribution')
            initial_state_distribution = dict()
            states = model.get_states()
            for state in states:
                initial_state_distribution[state] = input('%s -> ' % (state))
            model.set_initial_state_distribution(initial_state_distribution)
        elif action == 'o':
            action = input('Would you like all permutations? [y/n] >> ').lower()
            if action == 'y':
                sequence_length = int(input('Enter the sequence length >> '))
                observations = model.get_observations()
                observation_sequence = list(itertools.product(
                    observations, repeat=int(sequence_length)))
            elif action == 'n':
                prompt = 'Enter observation sequence [comma delimited] >> '
                observation_sequence = [sequence.strip() for sequence in input(prompt).split(',')]
                sequence_length = len(observation_sequence)
            else:
                print('Unknown input')
                continue
            model.set_observation_sequence(observation_sequence, sequence_length)
        elif action == 'x':
            states = model.get_states()
            sequence_length = input('Enter the sequence length >> ')
            state_sequence = list(itertools.product(states, repeat=int(sequence_length)))
            model.set_state_sequence(state_sequence)
        elif action == 's':
            print('Set algorithm')
            display_algorithms()
            action = input('>> ')
            if action is '1':
                algorithm = algorithms.Direct_Method(model)
            elif action is '2':
                algorithm = algorithms.Alpha_Pass(model)
            else:
                print('Unknown input')
                algorithm = None
        elif action == 'r':
            print('Executing %s' % (algorithm.name))
            algorithm.calculate_probabilities()
        elif action == 'h':
            display_help()
        elif action == 'e':
            exit(0)
        else:
            print('Unknown input')

################################################################################
if __name__ == '__main__':
    main()
