import dash_core_components as dcc
import plotly.graph_objs as go

def EPGraph(dataframe):
        
    graph = dcc.Graph(
        figure = go.Figure(
            data=[
                go.Scatter(
                    x=dataframe['Return Period'],
                    y=dataframe.iloc[:,1],
                    name='AEP'
                ),
                go.Scatter(
                    x=dataframe['Return Period'],
                    y=dataframe.iloc[:,2],
                    name='OEP'
                )
            ],
            layout={
                'template': 'plotly_white'
            }
        )
    )
    return graph

def TIVBarGraph(dataframe, facet):
    graph = dcc.Graph(
        figure = go.Figure(
            data=[
                go.Bar(
                    x=dataframe[facet],
                    y=dataframe['TIV'], 
                    marker={'color': '#197BBD'}
                )
            ],
            layout={
                'template': 'plotly_white'
            }
        )
    )
    return graph