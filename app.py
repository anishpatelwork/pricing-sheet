import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import pandas as pd
import dash_table
import os
from css import load_css, load_scripts
from helper import read_text_file
from model import Exposure, EPCurve
from pages import no_page, overview_page, exposure_summary_page, ep_curve_page

css = load_css()
scripts = load_scripts()
app = dash.Dash(__name__, external_stylesheets=css, external_scripts=scripts)
server=app.server
server.secret_key = os.environ.get('secret_key', 'secret')
app.config['suppress_callback_exceptions']=True

company_facts = pd.read_csv('data/facts.csv')
ep_curves = EPCurve(pd.read_csv('data/ep_curves.csv'))
exposure = Exposure(pd.read_csv('data/loc.csv'))
key_losses = pd.read_csv('data/keylosses.csv')
summary = read_text_file('data/summary.txt')


app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])

@app.callback(dash.dependencies.Output('page-content', 'children'),
            [dash.dependencies.Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/' or pathname == '/overview':
        return overview_page(summary, company_facts, key_losses)
    if pathname == '/exposure-summary':
        return exposure_summary_page(exposure)
    if pathname == '/ep-curves':
        return ep_curve_page(ep_curves)
    else:
        return no_page()

if __name__ == '__main__':
    app.run_server(debug=True, port=8050)