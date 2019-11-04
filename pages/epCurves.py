import dash_html_components as html
from components import Header, HalfRowCard, Table, EPGraph
from model import EPCurve

def ep_curve_page(ep_curves):
    page = html.Div([
        Header(),
        
        html.Div([
            HalfRowCard("EP all peril", Table(ep_curves.get_ep_curves(['netprecat'], ['ALL'], ['AEP', 'OEP']), display_header=True)),
            HalfRowCard("EP all peril", EPGraph(ep_curves.get_ep_curves(['netprecat'], ['ALL'], ['AEP', 'OEP'])))
        ], className="row "),

        html.Div([
            HalfRowCard("EP Windstorm", Table(ep_curves.get_ep_curves(['netprecat'], ['Windstorm'], ['AEP', 'OEP']), display_header=True)),
            HalfRowCard("EP Windstorm", EPGraph(ep_curves.get_ep_curves(['netprecat'], ['Windstorm'], ['AEP', 'OEP'])))
        ], className="row "),

        html.Div([
            HalfRowCard("EP Earthquake", Table(ep_curves.get_ep_curves(['netprecat'], ['Earthquake'], ['AEP', 'OEP']), display_header=True)),
            HalfRowCard("EP Earthquake", EPGraph(ep_curves.get_ep_curves(['netprecat'], ['Earthquake'], ['AEP', 'OEP'])))
        ], className="row "),

        ], className="container")
    return page