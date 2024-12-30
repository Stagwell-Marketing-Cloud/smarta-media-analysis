

from app.xgboost_adapter import XGBoostAdapter


class XGBoostService:
    xgboost_adapter: XGBoostAdapter = None

    def __init__(self, xgboost_adapter: XGBoostAdapter): 
        self.xgboost_adapter  = xgboost_adapter 

    def perform_regression(self, input_data): 
        return self.xgboost_adapter.regression(input_data)
    