"""
Module: preprocessing, this needs some thought

    * Each modelling task has its variety & sequence of preprocessing steps
    * Tests ascertaining the existence of expected fields will be required.

"""

import collections

import pandas as pd
import sklearn.preprocessing

import risk.functions.scale


# noinspection PyUnresolvedReferences
class Preprocessing:
    """
    Class Preprocessing

    """

    def __init__(self, parameters: collections.namedtuple, scaler: sklearn.preprocessing.StandardScaler):
        """

        :param parameters:
        :param scaler:
        """

        self.extraneous = parameters.extraneous
        self.regressors = parameters.regressors
        self.target = parameters.target

        self.scaler = scaler

    def prescale_(self, blob: pd.DataFrame) -> pd.DataFrame:
        """
        Drop extraneous fields, i.e., the polytomous categorical fields that have alternative representations.

        :param blob:
        :return:
        """

        if bool(self.extraneous):
            data = blob.copy().drop(columns=self.extraneous)
        else:
            data = blob.copy()

        return data

    def scale_(self, blob: pd.DataFrame) -> pd.DataFrame:
        """

        :param blob:
        :return:
        """

        scale = risk.functions.scale.Scale()

        left = scale.apply(blob=blob.drop(columns=self.target), scaler=self.scaler)
        scaled = pd.concat((left, blob[self.target]), axis=1, ignore_index=False)

        return scaled

    def exc(self, frame: pd.DataFrame) -> (pd.DataFrame, pd.DataFrame):
        """

        :param frame:
        :return:
        """

        prescaled = self.prescale_(blob=frame)
        scaled = self.scale_(blob=prescaled)

        x_testing_ = scaled[self.regressors]
        y_testing_ = scaled[self.target]

        return x_testing_, y_testing_
