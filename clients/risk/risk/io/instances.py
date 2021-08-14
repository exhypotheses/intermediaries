import collections
import pandas as pd
import requests
import json


class Instances:

    def __init__(self, parameters: collections.namedtuple):
        """

        """
        self.parameters = parameters

    def __data(self) -> pd.DataFrame:

        try:
            return pd.read_csv(filepath_or_buffer=self.parameters.initial, header=0, encoding='utf-8')
        except OSError as err:
            raise Exception(err.strerror)

    def __mappings(self) -> dict:

        try:
            req = requests.get(url=self.parameters.mappings)
            req.raise_for_status()
        except requests.exceptions.RequestException() as err:
            raise Exception(err)

        return json.loads(req.content)

    def exc(self) -> (pd.DataFrame, dict):

        return self.__data(), self.__mappings()
