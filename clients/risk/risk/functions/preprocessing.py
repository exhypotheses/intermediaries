"""
Module: preprocessing, this needs some thought
    * Tests ascertaining the existence of expected fields will be required.
"""

import collections

import pandas as pd
import sklearn.preprocessing

import risk.functions.scale
import risk.functions.embeddings


# noinspection PyUnresolvedReferences
class Preprocessing:
    """
    Class Preprocessing

    """

    def __init__(self, pocket: dict, mappings: dict, fields: dict):
        """

        :param pocket:
        """

        self.fields = fields
        self.target = fields['target']

        self.mappings = mappings

        self.regressors = pocket['regressors']
        self.scaler: sklearn.preprocessing.StandardScaler = pocket['scaler']

    def embed_(self, blob: pd.DataFrame):
        """
        Step 1: Embeddings

        :param blob:
        :return:
        """

        embeddings = risk.functions.embeddings.Embeddings(
            data=blob, mappings=self.mappings, fields=self.fields)
        return embeddings.exc()

    def scale_(self, blob: pd.DataFrame) -> pd.DataFrame:
        """
        Step 2: Scaling

        :param blob:
        :return:
        """

        scale = risk.functions.scale.Scale()
        transform = scale.apply(blob=blob.drop(columns=self.target), scaler=self.scaler)
        scaled = pd.concat((transform, blob[self.target]), axis=1, ignore_index=False)

        return scaled

    def exc(self, data: pd.DataFrame) -> (pd.DataFrame, pd.DataFrame):
        """

        :param data:
        :return:
        """

        embedded = self.embed_(blob=data)
        scaled = self.scale_(blob=embedded)
        x_testing_ = scaled[self.regressors.split(',')]
        y_testing_ = scaled[self.target]

        return x_testing_, y_testing_
