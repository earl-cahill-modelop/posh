#fastscore.slot.0: in-use
#fastscore.slot.1: in-use

import math

# modelop.init
def init():
    return

# modelop.metrics
def metrics():
    yield {}

# modelop.score
def score(data):
    print(data)
    print(type(data))
    start = 1
    max = 10000000

    if data is not None and (type(data) is dict):
        if 'start' in data:
            start = data['start']

        if 'max' in data:
            max = data['max']

    print(f"{max=}, {start=}")

    total = 0

    for i in range(1, max):
        total += math.sqrt(math.fabs(math.cos(i) * math.sin(i) / math.tan(i) * i**2 / i**3))

    return {
        total / max
    }

#print(score({'start' : 17, 'max' : 10}))
#print(score({'start' : 17}))
