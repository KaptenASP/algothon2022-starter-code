import numpy as np
import statistics

nInst = 100
currentPos = np.zeros(nInst)


# stochastic:
def stochastic(prices):
    return 100 * (prices[-1] - min(prices)) / (max(prices) - min(prices))


def stochastic_avg(prices):
    curr_sum = stochastic(prices[-14:])

    for i in range(1, 3):
        curr_sum += stochastic(prices[-14 - i:-i])

    return curr_sum / 3


# Bollinger Bands:
def moving_average(prices):
    return sum(prices[-14:]) / len(prices[-14:])


def standard_dev(prices):
    return statistics.stdev(prices[-14:])


def bollinger_band_upper(prices):
    return moving_average(prices) + 2 * standard_dev(prices)


def bollinger_band_lower(prices):
    return moving_average(prices) - 2 * standard_dev(prices)


def getMyPosition(prcSoFar):
    global currentPos

    day = len(prcSoFar[0])

    if day < 17:
        return currentPos
    elif day == 250:
        for num, i in enumerate(prcSoFar):
            currentPos[num] = 0
        return currentPos

    # Build your function body here
    for num, i in enumerate(prcSoFar):
        k_line = stochastic(i[-14:])
        d_line = stochastic_avg(i)
        bbu = bollinger_band_upper(i)
        bbl = bollinger_band_lower(i)

        if i[-1] <= bbl and 20 > k_line > d_line:
            currentPos[num] = 100

        if i[-1] >= bbu and 80 < k_line:
            currentPos[num] = 0

    return currentPos
