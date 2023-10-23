import os

import config


class Developer:

    def __init__(self):
        """

        """

        configurations = config.Config()

        self.path = os.path.join(configurations.warehouse, 'preface')

    def __write(self, schema: dict):
        """

        :return:
        """

    def exc(self, model_id: int):

        schema = {'modelId': model_id,
                  'modelArchitecture': 'model.gv',
                  'modelType': 'Bayesian Logistic Regression',
                  'modelReferences': 'references.csv',
                  'modelLicence': '',
                  'modelQueryAddress': '@',
                  'dataBucketString': ''}

        self.__write(schema=schema)
