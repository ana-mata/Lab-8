#   Author: Ana Luisa Mata Sanchez
#   Course: CS2302
#   Assignment: Lab #8
#   Instructor: Olac Fuentes
#   Description: Program to find identities and partitions
#   T.A.: Anindita Nath, Maliheh Zargaran
#   Last modified: 05/09/2019
#   Purpose: Practice randomization and backtracking

import random
import numpy as np
from mpmath import *
#from math import *

#Method to find the identities of an expression
def identityTries(F,evaluatee,tries=1000,tolerance=0.0001):
    equal = True
    Identities = []
    for i in range(len(F)):
        #To not repeat the expression that is being evaluated
        if i != evaluatee:
            for j in range(tries):
                t = random.uniform(-pi, pi)
                #Evaluate the current expression
                y1 = eval(F[evaluatee])
                #Evaluate one of the other expressions
                y2 = eval(F[i])
                #Check if the results are equal, if not stop evaluating them
                if np.abs(y1-y2)>tolerance:
                    equal = False
                    break
            #If the expressions are equal, add to the identities list
            if equal:
                Identities.append(F[i])
            equal = True
    return Identities

#Method to partition S into two subsets
def partition(S,last,summ, s1, s2):
    #If one of the two sets adds up to half of the sum... This means that remaining set has the other half of the sum
    #Meaning sum(s1)==sum(s2)
    if summ == 0:
        return True, s1, s2
    #If it doesn't reach the sum or if we went through the list
    if summ<0 or last<0:
        return False, s1, s2
    
    #Take S[last]
    res, s1, s2 = partition(S,last-1,summ-S[last], s1, s2) 
    
    if res:  
        #If S[last] works, add it to the empty set
        s1.append(S[last])
        #Now remove from the full set
        if S[last] in s2:
            s2.remove(S[last])
        return True, s1, s2
    else:
        #Don't take S[last]
        return partition(S,last-1,summ, s1, s2)

F = ['sin(t)','cos(t)','tan(t)','sec(t)','-sin(t)','-cos(t)','-tan(t)',
'sin(-t)','cos(-t)','tan(-t)','sin(t)/cos(t)','2*sin(t/2)*cos(t/2)',
'sin(t)*sin(t)','1 - (cos(t)*cos(t))','(1-cos(2*t))/2','1/cos(t)']

for i in range(len(F)):
    #Find identities for each of the expressions in the array
    print(F[i], " = ", identityTries(F,i), "\n")
    
S = [2, 4, 5, 9, 12]
S1 = []
S2 = []
for j in range(len(S)):
    S2.append(S[j])

if sum(S)%2 == 0:
    res, s1, s2 = partition(S,len(S)-1,sum(S)/2, S1, S2)
    if sum(s1) == sum(s2) and res:
        print("Set 1: ", s1,"\nSet 2: ", s2)
    else:
        print("No partition exists")
else:
    print("No partition exists")

