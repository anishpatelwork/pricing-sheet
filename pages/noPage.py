import dash_html_components as html

def no_page():
    return  html.Div([  # 404

    html.P(["404 Page not found"])

    ], className="no-page")