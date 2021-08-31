import collections
import io
import json
import os
import pickle
import zipfile

import pymc3
import requests


class Assets:

    def __init__(self, assets_: collections.namedtuple):
        """

        :param assets_:
        """

        self.assets_ = assets_
        self.path = os.path.join(os.getcwd(), 'data')

    def __pocket(self):
        """

        :return:
        """

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

        return pickle.loads(pickled, fix_imports=True, encoding='bytes')

    def __trace(self, lm):
        """

        :param lm:
        :return: pymc3.backends.base.MultiTrace
        """

        try:
            req = requests.get(url=self.assets_.trace)
            req.raise_for_status()
        except requests.exceptions.RequestException as err:
            raise Exception(err)
        zipped_object = zipfile.ZipFile(io.BytesIO(req.content))

        try:
            zipped_object.extractall(path=self.path)
        except OSError as err:
            raise Exception(err)

        with lm:
            return pymc3.backends.ndarray.load_trace(directory=os.path.join(self.path, 'trace'))

    def __definitions(self):
        """

        :return:
        """

        try:
            req = requests.get(url=self.assets_.definitions)
            req.raise_for_status()
        except requests.exceptions.RequestException() as err:
            raise Exception(err)

        return json.loads(req.content)

    def __mappings(self) -> dict:
        """

        :return:
        """

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

        pocket = self.__pocket()
        mappings = self.__mappings()
        trace = self.__trace(lm=pocket['lm'])
        definitions = self.__definitions()

        return pocket, mappings, trace, definitions
