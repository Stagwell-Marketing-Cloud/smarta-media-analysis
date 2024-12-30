

import json
from sklearn.base import BaseEstimator
from datetime import datetime
import os
import uuid
import joblib
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import GridSearchCV, cross_val_score, train_test_split
from xgboost import XGBRegressor
import numpy as np

### fit, predict, gs, load hp,

RANDOM_SEED = 42

parameters = {'nthread':[4], #when use hyperthread, xgboost may become slower
            'objective':['reg:linear'],
            'learning_rate': [.03, 0.05, .07], #so called `eta` value
            'max_depth': [5, 6, 7],
            'min_child_weight': [4],
            'silent': [1],
            'subsample': [0.7],
            'colsample_bytree': [0.7],
            'n_estimators': [500]}

default_params = {
            'random_state': RANDOM_SEED,
            'reg_lambda': 1.5,
            'reg_alpha': 0.3,
            'max_depth': 4,
            'subsample': 0.85,
            'learning_rate': 0.03,
            'min_child_weight': 3,
            'n_estimators': 200
        }




class XGBoostHandler(BaseEstimator):
    def __init__(self, target):
        self.hyperparameters=None
        self.target = target
        self.df = None
        self.x = None
        self.y = None
        self.scaled_y = None
        self.model_path = None
        self.model = XGBRegressor()


    def update_hyperparameters(self, hp):
        self.hyperparameters = hp

    def preprocess_df(self, df):
        self.df = df
        self.x = df.drop(columns=self.target)
        self.y = df[self.target]

    def grid_search(self):

        self.gs_model = GridSearchCV(self.model,
                        self.hyperparameters,
                        cv = 2,
                        n_jobs = 5,
                        verbose=True)

        self.gs_model.fit(self.x, self.y)
        self.hyperparameters = self.gs_model.best_params_
    
    def fit(self, gs=False):
        if gs == True:
            self.gs_model.fit(self.x, self.y)
        else:
            self.model.fit(self.x, self.y)

        
    def load_model(self, model_path):
        self.model = joblib.load(model_path)



    def train_xgboost_model(self,
        test_size=0.2,
        random_seed=RANDOM_SEED,
        save_model=False,
        model_name='',
        base_dir='trained_models'
    ):
        """
        Train XGBoost model with specified parameters and return model and metrics.
        
        Args:
            df: pandas DataFrame
            target_col: target column name (default: 'likes')
            model_params: dict of XGBoost parameters (default: None)
            test_size: validation split ratio (default: 0.2)
            random_seed: random state (default: 123)
            save_model: whether to save model (default: False)
            model_prefix: prefix for saved model name (default: '')
            save_dir: directory to save model (default: 'trained_models')
        
        Returns:
            dict: Contains model, parameters, and metrics
        """
        
        model_id = str(uuid.uuid4())
        timestamp = datetime.now().isoformat()
        run_id = f"{timestamp}_{model_id[:8]}"


        
        # model_params = model_params or default_params
        
        # self.x = df.drop(columns=self.target)
        self.scaled_y = np.log1p(self.y)
        
        X_train, X_val, y_train, y_val = train_test_split(
            self.x, self.scaled_y, test_size=test_size, random_state=random_seed
        )
        
        self.model = XGBRegressor(**self.hyperparameters)
        cv_scores = cross_val_score(self.model, X_train, y_train, cv=5, scoring='neg_mean_absolute_error')
        
        self.model.fit(X_train, y_train)
        
        y_pred = np.expm1(self.model.predict(X_val))
        y_val_original = np.expm1(y_val)
        
        metrics = {
            'cv_mae_mean': float(-cv_scores.mean()),
            'cv_mae_std': float(cv_scores.std() * 2),
            'mae': float(mean_absolute_error(y_val_original, y_pred)),
            'rmse': float(np.sqrt(mean_squared_error(y_val_original, y_pred))),
            'r2': float(r2_score(y_val_original, y_pred)),
            'percentile_90': float(np.percentile(abs(y_val_original - y_pred), 90))
        }
        predictions = {
            'y_val': y_val_original,
            'y_pred': y_pred
        }

        data = {
            'X_train': X_train, 
            'X_val': X_val, 
            'y_train': y_train, 
            'y_val': y_val, 

        }
        
        if save_model:
            model_dir = os.path.join(base_dir, model_name, run_id)
            model_path = os.path.join(model_dir, 'model', 'model.joblib')
            metadata_path = os.path.join(model_dir, 'metadata', 'metadata.json')
            
            os.makedirs(os.path.join(model_dir, 'model'), exist_ok=True)
            os.makedirs(os.path.join(model_dir, 'metadata'), exist_ok=True)
            
            joblib.dump(self.model, model_path)
            
            metadata = {
                'run_id': run_id,
                'model_id': model_id,
                'timestamp': timestamp,
                'parameters': self.hyperparameters,
                'metrics': metrics,
                'model_path': model_path
            }
            
            with open(metadata_path, 'w') as f:
                json.dump(metadata, f, indent=4)

        self.model_path = model_path if save_model else None
        
        return {
            'run_id': run_id,
            'model_id': model_id,
            'timestamp': timestamp,
            'model': self.model,
            'parameters': self.hyperparameters,
            'metrics': metrics,
            'data': data,
            'predictions': predictions,
            'model_path': model_path if save_model else None
        }

    def predict(self, X):
        return self.model.predict(X)


