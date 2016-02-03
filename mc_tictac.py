#!/usr/bin/env python

"""
Monte Carlo Tic-Tac-Toe Player
"""

import random
#import poc_ttt_gui
import poc_ttt_provided as provided

# Constants for Monte Carlo simulator
# You may change the values of these constants as desired, but
#  do not change their names.
NTRIALS = 20        # Number of trials to run
SCORE_CURRENT = 1.0 # Score for squares played by the current player
SCORE_OTHER = 1.0   # Score for squares played by the other player

# Add your functions here.

def mc_trial(board, player):
    """
    Function that runs the random game.
    """
    dim = board.get_dim()
    winner = None
    while winner == None:
        rand_row = random.randint(0, dim)
        rand_col = random.randint(0, dim)
        if (rand_row, rand_col) in board.get_empty_squares():
            #print "trial on " + str(rand_row) + str(rand_col)
            board.move(rand_row, rand_col, player)
            winner = board.check_win()
            player = provided.switch_player(player)
    print board

def mc_update_scores(scores, board, player):
    """
    Function that updates the scores based on the board status.
    """
    print "got"
    print scores
    winner = board.check_win()
    print winner
    if winner == provided.DRAW:
        return scores
    dim = board.get_dim()
    for dummy_i in range(dim):
        for dummy_j in range(dim):
            if board.square(dummy_i, dummy_j) is winner:
                scores[dummy_i][dummy_j] += SCORE_CURRENT
            elif board.square(dummy_i, dummy_j) is provided.switch_player(winner):
                scores[dummy_i][dummy_j] -= SCORE_CURRENT
    return scores

def get_key(item):
    """
    Key function for sorted..
    """
    return item[2]

def get_best_move(board, scores):
    """
    Function that gets the best move.
    """
    dim = board.get_dim()
    print "working on"
    print board
    print scores
    out = [[[] for dummy_i in range(dim)] for dummy_j in range(dim)]

    for dummy_i in range(dim):
        for dummy_j in range(dim):
            out[dummy_i][dummy_j].append(dummy_i)
            out[dummy_i][dummy_j].append(dummy_j)
            out[dummy_i][dummy_j].append(scores[dummy_i][dummy_j])

    flat_out = [item for sublist in out for item in sublist]

    # print flat_out

    flat_out = sorted(flat_out, reverse=True, key=get_key)

    # print flat_out
    empty = board.get_empty_squares()
    # print "GGGGGGG"
    # print empty
    for ele in flat_out:
        # print (ele[0], ele[1])
        if (ele[0], ele[1]) in empty:
            print "best move " + str(ele[0]) + str(ele[1])
            return ele[0], ele[1]
    return -1, -1

def mc_move(board, player, trials):
    """
    Function that makes a move on the board.
    """
    dim = board.get_dim()
    scores = [[0 for dummy_i in range(dim)] for dummy_j in range(dim)]
    for dummy_i in range(trials):
        b_clone = board.clone()
        mc_trial(b_clone, player)
        scores = mc_update_scores(scores, b_clone, player)
    return get_best_move(board, scores)


# Test game with the console or the GUI.  Uncomment whichever
# you prefer.  Both should be commented out when you submit
# for testing to save time.

# print provided.play_game(mc_move, NTRIALS, False)
# poc_ttt_gui.run_gui(3, provided.PLAYERX, mc_move, NTRIALS, False)

#mc_move(provided.TTTBoard(3, False, [[provided.PLAYERX, provided.EMPTY, provided.EMPTY], [provided.PLAYERO, provided.PLAYERO, provided.EMPTY], [provided.EMPTY, provided.PLAYERX, provided.EMPTY]]), provided.PLAYERX, NTRIALS)
