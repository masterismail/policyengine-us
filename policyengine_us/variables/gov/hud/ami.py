from policyengine_us.model_api import *


class ami(Variable):
    value_type = float
    entity = Household
    label = "Area median income"
    documentation = "Area median income"
    definition_period = YEAR

    def formula(household, period, parameters):
        # Only calculate for LA County for now. Otherwise zero.
        in_la = household("in_la", period)
        # https://www.hcd.ca.gov/sites/default/files/docs/grants-and-funding/income-limits-2023.pdf
        LA_COUNTY_AMI = 98_200
        return in_la * LA_COUNTY_AMI
