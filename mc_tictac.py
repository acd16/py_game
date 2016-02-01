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
NTRIALS = 1         # Number of trials to run
SCORE_CURRENT = 1.0 # Score for squares played by the current player
SCORE_OTHER = 1.0   # Score for squares played by the other player
    
# Add your functions here.

mc_trial(board, player):
    while board.get_empty_squares():
        rand_row = random.randint(0, 3)
        rand_col = random.randint(0, 3)
        if [rand_row][rand_col] in board.get_empty_squares():
            move(rand_row, rand_col, player)
            switch_player(player)
    


mc_update_scores(scores, board, player):
    winner = board.check_win()
    if winner == DRAW:
        return
    for i in range(board.get_dim()):
        for j in range(board.get_dim()):
            if board.square() is winner: 
                scores[i][j] += 1
            else:
                scored[i][j] -= 1
    

get_best_move(board, scores):
    max = 0
    max_r = 0
    max_c = 0
    for i in range(board.get_dim()):
        for j in range(board.get_dim()):
            if max < scores[i][j]:
                max = scores[i][j]
                max_r = i
                max_c = j
    return max_r, max_c
            
mc_move(board, player, trials):
    scores = [[0 for i in range(board.get_dim())] for i in range(board.get_dim())]
    for i in range(trials):
        b_clone = board.clone()
        mc_trial(b_clone, player)
        mc_update_scores(scores, b_clone, player)
    return get_best_move(b_clone, scores)


# Test game with the console or the GUI.  Uncomment whichever 
# you prefer.  Both should be commented out when you submit 
# for testing to save time.

print provided.play_game(mc_move, NTRIALS, False)        
# poc_ttt_gui.run_gui(3, provided.PLAYERX, mc_move, NTRIALS, False)


