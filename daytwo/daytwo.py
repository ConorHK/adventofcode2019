# Program for daytwo of advent of code
# by Conor Knowles
# ------------------------------------

import sys # for using sys.exit() function
input_lis = [] # declaration of master list

# reading in input from text file 
with open("input.txt") as file:
    input_lis = file.read().split(',')
file.close()

# converting contents of master list to integers
input_lis = list(map(int, input_lis))

# function for carrying out multiplication/addition instructions
def instructions(lis, m):
    if lis[m] == 1: # addition
        sum = lis[lis[m+1]] + lis[lis[m+2]]
        lis[lis[m+3]] = sum
    elif lis[m] == 2: # multiplcation
        product = lis[lis[m+1]] * lis[lis[m+2]]
        lis[lis[m+3]] = product
    elif lis[m] == 99: # finish
        return lis[0]
    else: # error check for invalid OPCODES
        print("Error: invalid OPCODE " + str(lis[m]))
        sys.exit()

# function that copies the lis from the master list and assigns the 1st and 2nd position the noun and verb. It returns the answer of position 0 of the list.
def run_intcode(noun: int, verb: int, input_lis):
    ans = None
    input_lis_copy = input_lis.copy()
    increment = 0
    input_lis_copy[1] = noun
    input_lis_copy[2] = verb
    while ans == None: # while no answer has been recieved, increment to next instruction set
        ans = instructions(input_lis_copy, increment)
        increment += 4 
    return ans

# passes appropriate noun and verb to intcode function and returns answer
def run_part_one():
    answer_part_one = run_intcode(12,2,input_lis)
    print("Answer to part 1: " + str(answer_part_one))

# checks every combination of i,j in range (0,99) until the output is found and system exits.
def run_part_two():
    for i in range(0,99):
        for j in range(0,99):
            output = run_intcode(i,j,input_lis)
            if output == 19690720:
                print("Answer to part 2: " + str((100 * i + j)))
                sys.exit()

# run part one and two
run_part_one()
run_part_two()
