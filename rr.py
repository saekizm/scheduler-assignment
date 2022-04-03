"""
Author: Senan Warnock
I acknowledge DCU's academic integrity policy.

"""

from functions import *

timeQuantum = 0.01
time = 0
waitingTime = []
remainingBurst = []

def roundRobinWaitingTime(data, time):
    
    for i in range(len(data)):
        remainingBurst.append(int(data[i][1]))

    while(True):
        complete = True
        for i in range(len(data)):
            if remainingBurst[i] > 0:
                complete = False
                if remainingBurst[i] > timeQuantum:
                    time += timeQuantum
                    remainingBurst[i] -= timeQuantum
                else:
                    time += int(data[i][2])
                    waitingTime.append(time - int(data[i][2]))
                    remainingBurst[i] = 0
        if complete == True:
            break

def appendWaitTime(data):
    for i in range(len(data)):
        data[i].append(waitingTime[i])

input = getData()
roundRobinWaitingTime(input, time)
appendWaitTime(input)
calcTurnAroundTime(input)
for line in input:
    print(f'Process: {line[0]} arrived at time: 0 and ran for {line[2]} ms. It had a turn around time of {line[4]}.')

print(getAvgTurnAround(input))