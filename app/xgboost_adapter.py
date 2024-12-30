

from app.xgboost_handler import XGBoostHandler


class XGBoostAdapter:
    xgboost_model_handler: XGBoostHandler = None

    def __init__(self, xgboost_model_handler: XGBoostHandler):
        self.xgboost_model_handler = xgboost_model_handler
        self.x = None

    def regression(self, x):
        self.x = x
        return self.xgboost_model_handler.predict(self.x)