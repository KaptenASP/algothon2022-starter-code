import numpy as np
from strategies import Strategies

nInst = 100
currentPos = np.zeros(nInst)


def getMyPosition(prcSoFar):
    global currentPos
    #
    if len(prcSoFar[0]) % 5 != 0:
        return currentPos

    for num, i in enumerate(prcSoFar):
        if currentPos[num] != 0:
            continue

        head_and_shoulders_pattern = Strategies(i, 5)
        head_and_shoulders_pattern.extract_min_max()
        if head_and_shoulders_pattern.find_head_shoulders_pattern():
            currentPos[num] = -100
        if head_and_shoulders_pattern.find_double_top():
            currentPos[num] = -100

    return currentPos
