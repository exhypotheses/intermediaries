import os
import pickle
import requests
import json
import collections


class Assets:

    def __init__(self, assets_: collections.namedtuple):
        """

        :param assets_:
        """

        self.assets_ = assets_
        self.path = os.path.join(os.getcwd(), 'data')

    def __pocket(self) -> dict:

        try:
            req = requests.get(url=self.assets_.pocket)
            req.raise_for_status()
        except requests.exceptions.RequestException() as err:
            raise Exception(err)

        with open(os.path.join(self.path, 'pocket.pkl'), 'wb') as f:
            f.write(req.content)
            f.close()

        with open(os.path.join(self.path, 'pocket.pkl'), 'rb') as f:
            pickled = f.read()
            f.close()

        return pickle.loads(pickled)

    def __mappings(self) -> dict:

        try:
            req = requests.get(url=self.assets_.mappings)
            req.raise_for_status()
        except requests.exceptions.RequestException() as err:
            raise Exception(err)

        return json.loads(req.content)

    def exc(self) -> (dict, dict):
        """

        :return:
        """

        if not os.path.exists(self.path):
            os.makedirs(self.path)

        return self.__pocket(), self.__mappings()
