"""
Author: Senan Warnock
I acknowledge DCU's academic integrity policy.

"""

import sys
from functions import *


def main():
    
    inputData = getData()
    calcWaitTime(inputData)
    calcTurnAroundTime(inputData)

    for line in inputData:
        print(f'Process: {line[0]} arrived at time: 0 and ran for {line[2]} ms. It had a turn around time of {line[4]}.')

    print(getAvgTurnAround(inputData))
if __name__ == "__main__":
    main()