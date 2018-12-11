import math
import sys
import plotly
import plotly.graph_objs as go
from scipy import stats

def parse(file):
    f = open(file,"r")

    FIELD_TIME = 0
    FIELD_STATUSCODE = 1
    FIELD_RESPONSE = 2
    FIELD_ELAPSE = 3

    start = 9999999999
    times = []
    responses = []
    fl = f.readlines()
    for line in fl:
        fields = line.split(",")
        if fields[FIELD_STATUSCODE] == "200":
            time = float(fields[FIELD_TIME])
            if time < start:
                start = time
            times.append(time)
            responses.append(float(fields[FIELD_RESPONSE]))
    for i in range(len(times)):
        times[i] = times[i] - start

    return [times, responses]

def scatter(series):
    trace = go.Scatter(
        x = series[0],
        y = series[1],
        mode = "markers"
    )
    data = [trace]
    plotly.offline.plot(data, auto_open=True)

if __name__ == "__main__":
    file = None
    if len(sys.argv) > 1:
        file = sys.argv[1]

    scatter(parse(file))
