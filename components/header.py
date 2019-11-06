import dash_html_components as html
import dash_core_components as dcc

def Header():
    return html.Div([
        html.Nav( 
            html.Div(className="nav-wrapper", children=[
                html.A("Pricing Sheet", href="/", className="brand-logo hide-on-med-and-down"),
                html.Ul(className="right hide-on-med-and-down", children=[
                    html.Li(dcc.Link('OVERVIEW', href='/overview')),
                    html.Li(dcc.Link('EXPOSURE SUMMARY', href='/exposure-summary')),
                    html.Li(dcc.Link('EP CURVES', href='/ep-curves'))
                ]),
                html.Ul(className="hide-on-large-only", children=[
                    html.Li(dcc.Link('OVERVIEW', href='/overview')),
                    html.Li(dcc.Link('EXPOSURE SUMMARY', href='/exposure-summary')),
                    html.Li(dcc.Link('EP CURVES', href='/ep-curves'))
                ]),
    ])),
    ], className="navbar-container")
