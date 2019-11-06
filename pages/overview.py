import dash_html_components as html
import dash_core_components as dcc
from components import Header, HalfRowCard, Table, TextArea, FullRowCard


def overview_page(summary, company_facts, key_losses):
    
    page = html.Div([
        Header(),

        html.Div([
            HalfRowCard("Summary", TextArea(summary, "summary")),
            HalfRowCard("Key Info", Table(company_facts))
        ], className = "row"),

        html.Div([
            FullRowCard("Key Losses", Table(key_losses, display_header=True))
        ], className="row")

        ], className="container")

        
    return page