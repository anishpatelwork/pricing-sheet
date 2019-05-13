import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
from dash.dependencies import Output, Input
from pages import no_page, overview_page
from css import load_css
from model import Exposure, EPCurve
from helper import read_text_file

# This is some boilerplate for the basic shell of the app
app = dash.Dash(__name__)
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])

# Put any data loading here
# summary = read_text_file('data/summary.txt')
# key_info = pd.read_csv('data/facts.csv')
# key_losses = pd.read_csv('data/keylosses.csv')
# ep_curves = pd.read_csv('data/ep_curves.csv')
# ep_curve = EPCurve(ep_curves)
# loc = pd.read_csv('data/loc.csv')
# exposure = Exposure(loc)

# This is just some boilerplate that lets you have multiple tabs in the page
# Pass in any data to pages from here
@app.callback(Output('page-content', 'children'),
            [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/' or pathname == '/overview':
        return overview_page()
    else:
        return no_page()

load_css(app)

if __name__ == '__main__':
    app.run_server(debug=True, port=8000)