#!/usr/bin/env python3

import sys

game_pieces = {'king': 2, 'queen': 2, 'rook': 4, 'bishop': 4, 'knight': 4, 'pawn': 16}
def get_peices(piece_name, num_given):
    target = game_pieces[piece_name]
    i = 0
    while num_given != target:
        if num_given < target:
            num_given += 1
            i += 1
        else:
            num_given = num_given - 1
            i = i -1
    return i

for line in sys.stdin.readlines():
    line = line.strip().split()
    totals = []
    totals.append(get_peices("king", int(line[0])))
    totals.append(get_peices("queen", int(line[1])))
    totals.append(get_peices("rook", int(line[2])))
    totals.append(get_peices("bishop", int(line[3])))
    totals.append(get_peices("knight", int(line[4])))
    totals.append(get_peices("pawn", int(line[5])))
    s = [str(i) for i in totals]
    print(' '.join(s))