import dash_html_components as html
import dash_core_components as dcc
from components import Header, HalfRowCard, Table, FullRowCard, TextArea, EPGraph, TIVBarGraph

#variables
def overview_page():
    # def overview_page(summary, key_info, key_losses, ep_curves, exposure):
    page = html.Div([
        
        # this is a header, we want to include it in every page
        Header(),
        
        # this is a row
        html.Div([
        ],className="row"),

    ], className="page")
    return page