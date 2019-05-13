import pandas as pd
class Exposure:

    exposure = pd.DataFrame

    def __init__(self, loc_exposure):
        loc_exposure = self.get_exposure_subset(loc_exposure)
        loc_exposure = self.enrich_with_occupancy(loc_exposure)
        loc_exposure = self.enrich_with_construction(loc_exposure)
        self.exposure = loc_exposure

    def tiv_by_state(self):
        tiv_by_state = self.exposure.groupby('STATECODE').sum().sort_values('TIV', ascending=False)
        tiv_by_state['State'] = tiv_by_state.index
        tiv_by_state = tiv_by_state[['State', 'TIV']]
        return tiv_by_state

    def tiv_by_construction(self):
        tiv_by_construction= self.exposure.groupby('ConsDesc').sum().sort_values('TIV', ascending=False)
        tiv_by_construction['Construction'] = tiv_by_construction.index
        tiv_by_construction = tiv_by_construction[['Construction', 'TIV']]
        return tiv_by_construction

    def tiv_by_occupancy(self):
        tiv_by_occupancy = self.exposure.groupby('OccDesc').sum().sort_values('TIV', ascending=False)
        tiv_by_occupancy['Occupancy'] = tiv_by_occupancy.index
        tiv_by_occupancy = tiv_by_occupancy[['Occupancy', 'TIV']]
        return tiv_by_occupancy

    def get_exposure_subset(self, loc):
        exposureSubset = loc[['LOCNUM', 'STATECODE', 'BLDGSCHEME', 'BLDGCLASS', 'OCCSCHEME', 'OCCTYPE', 'EQCV1VAL', 'EQCV2VAL', 'EQCV3VAL', 'EQCV4VAL', 'WSCV4VAL', 'WSCV6VAL', 'WSCV7VAL']]
        exposureSubset = exposureSubset.fillna(value=0)
        exposureSubset['EQTOTAL'] = exposureSubset.apply(lambda row: row.EQCV1VAL + row.EQCV2VAL + row.EQCV3VAL + row.EQCV4VAL, axis=1)
        exposureSubset['WSTOTAL'] = exposureSubset.apply(lambda row: row.WSCV4VAL + row.WSCV6VAL + row.WSCV7VAL, axis=1)
        exposureSubset['TOTAL'] = exposureSubset.apply(lambda row: row.EQTOTAL + row.WSTOTAL, axis=1)
        exposureSubset.rename(columns={'TOTAL': 'TIV'}, inplace=True)
        return exposureSubset

    def enrich_with_occupancy(self, dataframe):
        occType = pd.read_csv('data/occtype.csv')
        merged = pd.merge(dataframe, occType, how='left', on='OCCTYPE')
        return merged

    def enrich_with_construction(self, dataframe):
        consClass = pd.read_csv('data/consclass.csv')
        merged = pd.merge(dataframe, consClass, how='left', on='BLDGCLASS')
        return merged