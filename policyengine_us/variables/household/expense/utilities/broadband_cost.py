from policyengine_us.model_api import *


class broadband_cost(Variable):
    value_type = float
    entity = Household
    label = "Broadband cost"
    unit = USD
    definition_period = YEAR
