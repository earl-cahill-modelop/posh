import math
import time

# modelop.init
def init():
    return

# modelop.metrics
def metrics():
    yield {}

# modelop.score
def score(data):
    begin = time.time() * 1000

    print(begin)
    print(data, flush=True)
    start = 1
    max = 10000000

    if data is not None and (type(data) is dict):
        if 'start' in data:
            start = data['start']

        if 'max' in data:
            max = data['max']

    print("max=" + str(max) + ", start=" + str(start), flush=True)

    total = 0

    for i in range(start, max):
        total += math.sqrt(math.fabs(math.cos(i) * math.sin(i) / math.tan(i) * i**2 / i**3))

    print('about to yield', flush=True)

    yield {
        'start' : start,
        'max' : max,
        'score' : total / max,
        'milliseconds' : (time.time() * 1000) - begin
    }

#print(score({'start' : 17, 'max' : 10}))
#print(score({'start' : 17}))
