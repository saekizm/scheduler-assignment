"""
Author: Senan Warnock
I acknowledge DCU's academic integrity policy.

"""

import sys
from operator import itemgetter

def calcWaitTime(d):
    d[0].append('0')
    wt = 0
    for i in range(1, len(d)):
        wt += int(d[i - 1][2])
        d[i].append(str(wt))

def calcTurnAroundTime(d):
    ta = 0
    for i in range(len(d)):
        ta = int(d[i][2]) + int(d[i][3])
        d[i].append(str(ta))

def getAvgTurnAround(d):
    sum = 0
    for line in d:
        sum += int(line[4])
    return sum / len(d)

def getData():
    data = sys.argv[1]
    f = open(data, 'r')
    inputData = []
    for line in f.readlines():
        line = line.rstrip()
        line = line.split(", ")
        inputData.append(line)
    return inputData

def sortOnBurst(d):
    burstSort = sorted(d, key=itemgetter(2))
    return burstSort

def sortOnPriority(d):
    prioritySort = sorted(d, key=itemgetter(1))
    return prioritySort
