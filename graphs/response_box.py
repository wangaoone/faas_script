import sys
import plotly
import plotly.graph_objs as go

from parsers.response import Response

def box(response):
    data = go.Box(
        y = response.series(Response.FIELD_RESPONSE),
        x = map(lambda time: int(time), response.series(Response.FIELD_TIME)),
        marker = dict( color = 'rgb(107,174,214)'),
        line = dict( color = 'rgb(7,40,89)')
    )

    plotly.offline.plot([data], auto_open = True)

if __name__ == "__main__":
    file = None
    if len(sys.argv) > 1:
        file = sys.argv[1]

    box(Response.parse(file).filter(lambda record: record[Response.FIELD_STATUSCODE] == 200))
