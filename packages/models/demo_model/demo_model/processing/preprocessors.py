"""Pipeline preprocessors for feature selection.
"""
import numpy as np
import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin

class DropUnecessaryFeatures(BaseEstimator, TransformerMixin):
    """Transformer designed to drop unnecessary features.
    """
    def __init__(self, variables_to_drop=None):
        self.variables = variables_to_drop

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        # encode labels
        X = X.copy()
        X = X.drop(self.variables, axis=1)
        
        return X