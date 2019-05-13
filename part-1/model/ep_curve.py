import pandas as pd

class EPCurve:
    ep_curves = pd.DataFrame()

    def __init__(self, ep_curves):
        self.ep_curves = ep_curves

    def get_ep_curves(self, positions, perils, ep_types):
        columns = ['Return Period']
        for column in self.ep_curves.columns:
            if self.filter_ep(column, positions, perils, ep_types) == True:
                columns.append(column)
        return self.ep_curves[columns]

    def filter_ep(self, curve, positions, types, perils):
        for position in positions:
            for type in types:
                for peril in perils:
                    if position in curve and type in curve and peril in curve:
                        return True
        return False