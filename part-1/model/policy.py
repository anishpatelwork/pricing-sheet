import pandas as pd

class Policy:
    policies = pd.DataFrame

    def __init__(self, policies):
        self.policies = policies

    def enrich_policies_with_policy_type(self):
        policy_type = {
            1:'Earthquake', 
            2:'Windstorm',
            3:'Severe Convective Storm/Winterstorm',
            4:'Flood',
            5:'Fire',
            6:'Terrorism',
            7:'Casualty'
            }
        