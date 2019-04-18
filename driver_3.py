#!/usr/bin/env python
#coding:utf-8
import time
import sys
"""
Each sudoku board is represented as a dictionary with string keys and
int values.
e.g. my_board['A1'] = 8
"""

ROW = "ABCDEFGHI"
COL = "123456789"


def print_board(board):
    """Helper function to print board in a square."""
    print("-----------------")
    for i in ROW:
        row = ''
        for j in COL:
            row += (str(board[i + j]) + " ")
        print(row)


def board_to_string(board):
    """Helper function to convert board dictionary to string for writing."""
    ordered_vals = []
    for r in ROW:
        for c in COL:
            ordered_vals.append(str(board[r + c]))
    return ''.join(ordered_vals)


def checkconstrains(var,value,constrains):
    for c in COL:
        try:
            temp = constrains[var[0] + c][:]
            temp.remove(value)
            constrains[var[0] + c] = temp
        except:
            pass
    for r in ROW:
        try:
            temp = constrains[r + var[1]][:]
            temp.remove(value)
            constrains[r + var[1]] = temp
        except:
            pass
    if var[0] in 'ABC123' and var[1] in 'ABC123':
        for i in 'ABC':
            for j in '123':
                try:
                    temp = constrains[i + j][:]
                    temp.remove(value)
                    constrains[i + j] = temp
                except:
                    pass
    if var[0] in 'ABC456' and var[1] in 'ABC456':
        for i in 'ABC':
            for j in '456':
                try:
                    temp = constrains[i + j][:]
                    temp.remove(value)
                    constrains[i + j] = temp
                except:
                    pass
    if var[0] in 'ABC789' and var[1] in 'ABC789':
        for i in 'ABC':
            for j in '789':
                try:
                    temp = constrains[i + j][:]
                    temp.remove(value)
                    constrains[i + j] = temp
                except:
                    pass
    if var[0] in 'DEF123' and var[1] in 'DEF123':
        for i in 'DEF':
            for j in '123':
                try:
                    temp = constrains[i + j][:]
                    temp.remove(value)
                    constrains[i + j] = temp
                except:
                    pass
    if var[0] in 'DEF456' and var[1] in 'DEF456':
        for i in 'DEF':
            for j in '456':
                try:
                    temp = constrains[i + j][:]
                    temp.remove(value)
                    constrains[i + j] = temp
                except:
                    pass
    if var[0] in 'DEF789' and var[1] in 'DEF789':
        for i in 'DEF':
            for j in '789':
                try:
                    temp = constrains[i + j][:]
                    temp.remove(value)
                    constrains[i + j] = temp
                except:
                    pass
    if var[0] in 'GHI123' and var[1] in 'GHI123':
        for i in 'GHI':
            for j in '123':
                try:
                    temp = constrains[i + j][:]
                    temp.remove(value)
                    constrains[i + j] = temp
                except:
                    pass
    if var[0] in 'GHI456' and var[1] in 'GHI456':
        for i in 'GHI':
            for j in '456':
                try:
                    temp = constrains[i + j][:]
                    temp.remove(value)
                    constrains[i + j] = temp
                except:
                    pass
    if var[0] in 'GHI789' and var[1] in 'GHI789':
        for i in 'GHI':
            for j in '789':
                try:
                    temp = constrains[i + j][:]
                    temp.remove(value)
                    constrains[i + j] = temp
                except:
                    pass

def select_unassigned_variable(constrains):
    min = ('',10)
    for index, value in constrains.items():
        if 0 < len(value) < min[1]:
            min = (index, len(value))
    return min

def inference(var,value,constrains):
    del constrains[var]
    checkconstrains(var,value,constrains)
    for key, value in constrains.items():
        if len(value) == 0:
            return False
    return True

def backtracking(board):
    """Takes a board and returns solved board."""
    # TODO: implement this
    domain = [1,2,3,4,5,6,7,8,9]
    constrains = {}
    for key, value in board.items():
        if value == 0:
            constrains[key] = domain

    for key, value in board.items():
        if value != 0:
            checkconstrains(key,value,constrains)

    return backtracking_search(board,domain,constrains)


def backtracking_search(board,domain,constrains):
    flag = 0
    for index, value in board.items():
        if value == 0:
            flag += 1
    if flag == 0:
        return board
    var = select_unassigned_variable(constrains)[0]
    for value in domain:
        #print(var, value, constrains)
        #print_board(board)
        temp_constrains = constrains.copy()
        if value in constrains[var]:
            board[var] = value

            inferences = inference(var,value,constrains)
            if inferences != False:
                result = backtracking_search(board,domain,constrains)
                if result != None:
                    return result

        for k, v in temp_constrains.items():
            constrains[k] = temp_constrains[k]
        board[var] = 0

    return None

if __name__ == '__main__':
    #  Read boards from source.
    src_filename = sys.argv[1]
    # line_number = 0
    try:
        srcfile = open(src_filename, "r")
        sudoku_list = srcfile.read()
    except:
        print("Error reading the sudoku file %s" % src_filename)
        exit()

    # Setup output file
    out_filename = 'output.txt'
    outfile = open(out_filename, "w")

    # Solve each board using backtracking
    for line in sudoku_list.split("\n"):
        # start_time = time.time()
        if len(line) < 9:
            continue

        # Parse boards to dict representation, scanning board L to R, Up to Down
        board = { ROW[r] + COL[c]: int(line[9*r+c])
                  for r in range(9) for c in range(9)}

        # Print starting board. TODO: Comment this out when timing runs.
        #print_board(board)

        # Solve with backtracking
        solved_board = backtracking(board)

        # Print solved board. TODO: Comment this out when timing runs.
        #print_board(solved_board)

        # Calculate processing time
        # line_number += 1
        # process_time = time.time() - start_time
        # Write board to file
        # outfile.write(str(line_number))
        # outfile.write('\t')
        # outfile.write(str(process_time))
        # outfile.write('\t')
        outfile.write(board_to_string(solved_board))
        outfile.write('\n')

    print("Finishing all boards in file.")