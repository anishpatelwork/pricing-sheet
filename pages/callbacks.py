from dash.dependencies import Output, Input
from components import Table
import dash_html_components as html

def register_callbacks(app, key_losses):
    our_losses = key_losses

    @app.callback(
        Output('our-losses-table', 'children'),
        [Input('share-slider', 'value')]
    )
    def update_our_losses(value):
        our_losses['AAL'] = our_losses['AAL (USD)'] * value/100
        return Table(our_losses[['Peril', 'AAL']], display_header=True)