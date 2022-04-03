"""
Author: Senan Warnock
I acknowledge DCU's academic integrity policy.

"""

from functions import *

inputData = getData()
inputData = sortOnBurst(inputData)
calcWaitTime(inputData)
calcTurnAroundTime(inputData)
for line in inputData:
    print(f'Process: {line[0]} arrived at time: 0 and ran for {line[2]} ms. It had a turn around time of {line[4]}.')

print(getAvgTurnAround(inputData))