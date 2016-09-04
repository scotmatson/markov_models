#!/usr/bin/env python
# -*- coding: utf-8 -*-

import itertools
from markov import Markov
from direct_method import Direct_Method

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
            print('Enter observation sequence [comma delimited]')
            observation_sequence = [sequence.strip() for sequence in input().split(',')]
            model.set_observation_sequence(observation_sequence)
        elif action == 'x':
            states = model.get_states()
            sequence_length = input('Enter the sequence length [integer]\n')
            state_sequence = list(itertools.product(states, repeat=int(sequence_length)))
            model.set_state_sequence(state_sequence)
        elif action == 's':
            print('Set algorithm')
            display_algorithms()
            action = input('>> ')
            if action is '1':
                algorithm = Direct_Method(model)
            else:
                print('Unknown input')
                algorithm = None
        elif action == 'h':
            display_help()
        elif action == 'r':
            #try:
            print('Executing %s' % (algorithm.name))
            algorithm.calculate_probability()
            #except:
            #    print('An algorithm has not yet been selected!\n')
        elif action == 'e':
            exit(0)
        else:
            print('Unknown input')

################################################################################
if __name__ == '__main__':
    main()
