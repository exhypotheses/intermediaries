import collections
import pandas as pd


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

    def exc(self) -> (pd.DataFrame, dict):

        return self.__data()
