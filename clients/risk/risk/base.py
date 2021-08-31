import logging
import requests

import risk.io.arguments
import risk.io.instances
import risk.io.assets
import risk.functions.preprocessing


class Base:

    def __init__(self, urlstring):
        """

        :param urlstring:
        """

        self.urlstring = urlstring

        # Logging
        logging.basicConfig(level=logging.INFO, format='%(message)s\n%(asctime)s.%(msecs)03d', datefmt='%Y-%m-%d %H:%M:%S')
        self.logger = logging.getLogger(__name__)

    def __arguments(self):
        """
        Parse Arguments

        :return:
        """

        arguments = risk.io.arguments.Arguments()
        req: requests.models.Response = arguments.url(urlstring=self.urlstring)

        data_, assets_ = arguments.parameters(elements=req)

        return data_, assets_

    def exc(self):

        """
        embed -> scale -> structure

        From model developer:
            pocket.pkl (model),
            trace.zip (of model),
            definitions.json (of categorical fields)
            mappings.json (t-SNE embeddings of polytomous categorical fields)

        From the client:
            testing.csv

        :return:
        """

        data_, assets_ = self.__arguments()

        # The data
        data = risk.io.instances.Instances(parameters=data_).exc()
        self.logger.info('\nTesting Data: %s', data.shape)

        pocket, mappings, trace, definitions = risk.io.assets.Assets(assets_=assets_).exc()
        self.logger.info('\nPocket:\n %s', pocket.keys())
        self.logger.info('\nMappings Keys:\n %s', mappings.keys())
        self.logger.info('\nTrace Variables:\n %s', trace.varnames)
        self.logger.info('\nCategorical Fields:\n %s', definitions.keys())

        x_testing_, y_testing_ = risk.functions.preprocessing.Preprocessing(
            pocket=pocket, mappings=mappings, fields=data_.fields).exc(data=data)
        self.logger.info('\nRegressors:\n %s', x_testing_.info())
        self.logger.info('\nOutcomes:\n %s', y_testing_.tail())

        return pocket, mappings, trace, definitions, x_testing_, y_testing_, data
