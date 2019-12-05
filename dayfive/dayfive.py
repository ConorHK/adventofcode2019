# Program for dayfive of advent of code
# by Conor Knowles
# ------------------------------------

import sys # for using sys.exit() function
import math
input_lis = [] # declaration of master list

# reading in input from text file 
with open("input.txt") as file:
    input_lis = file.read().split(',')
file.close()
print(len(input_lis))
# converting contents of master list to integers
input_lis = list(map(int, input_lis))

# function for carrying out multiplication/addition instructions
def instructions(lis, inc, OP, C, B, A, input_param):
    integer_one = lis[lis[inc+1]] if C == 0 else lis[inc+1]
    integer_two = lis[lis[inc+2]] if B == 0 else lis[inc+2]

    if OP == 1: # addition
        sum_total = lis[lis[inc+1]] + lis[lis[inc+2]]
        if A == 0:
            lis[lis[inc+3]] = sum_total
        else:
            lis[inc+3] = sum_total
    elif OP == 2: # multiplcation
        product = lis[lis[inc+1]] * lis[lis[inc+2]]
        if A == 0:
            lis[lis[inc+3]] = product
        else:
            lis[inc+3] = product
    elif OP == 3:
        lis[lis[inc+1]] = input_param
    elif OP == 4:
        output_param = lis[lis[inc+1]]
        print(output_param)
    elif OP == 99: # finish
        return lis[0]
    else: # error check for invalid OPCODES
        print("Error: invalid OPCODE " + str(OP))
        sys.exit()

# function that copies the lis from the master list and assigns the 1st and 2nd position the noun and verb. It returns the answer of position 0 of the list.
def run_intcode(input_lis, input_param):
    # initializing variables and assigning noun,verb and generating copy of master list
    ans = None
    input_lis_copy = input_lis.copy()
    increment = 0

    while ans == None: # while no answer has been recieved, increment to next instruction set
        print("loop")
        # separating opcode DE from parameter values
        opcode = input_lis_copy[increment]
        DE = opcode % 10
        C = (math.trunc(opcode / 100) % 10)
        B = (math.trunc(opcode / 1000) % 10)
        A = (math.trunc(opcode / 10000) % 10)

        ans = instructions(input_lis_copy, increment, DE, C, B, A, input_param)
        if (input_lis_copy[increment] == 3 or input_lis_copy[increment] == 4):
            increment += 2
        else:
            increment += 4
    return ans

def run_day_five():
    answer = run_intcode(input_lis, 1)
    print("Answer to dayfive: " + str(answer))

run_day_five()
