import dash_html_components as html
from components import Table, Header, TIVBarGraph, HalfRowCard
import pandas as pd

def exposure_summary_page(exposure):    
    page = html.Div([
        Header(),

        html.Div([
            HalfRowCard("TIV by State", Table(exposure.tiv_by_state(), display_header=True)),
            HalfRowCard("TIV by State", TIVBarGraph(exposure.tiv_by_state(), "State"))
        ], className="row "),

        html.Div([
            HalfRowCard("TIV by Occupancy", Table(exposure.tiv_by_occupancy(), display_header=True)),
            HalfRowCard("TIV by Occupancy", TIVBarGraph(exposure.tiv_by_occupancy(), "Occupancy"))
        ], className="row "),

        html.Div([
            HalfRowCard("TIV by State", Table(exposure.tiv_by_construction(), display_header=True)),
            HalfRowCard("TIV by State", TIVBarGraph(exposure.tiv_by_construction(), "Construction"))
        ], className="row "),
        
    ], className="container")
    return page