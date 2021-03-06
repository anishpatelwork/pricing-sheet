import dash_html_components as html

def HalfRowCard(cardName, content):
    return html.Div([
        html.H6(cardName, className="gs-header gs-text-header padded"),
        content
    ], className="col s12 m6")
    
def FullRowCard(cardName, content):
    return html.Div([
        html.H6(cardName, className="gs-header gs-text-header padded"),
        content
    ], className="col s12 m12")