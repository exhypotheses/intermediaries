import logging
import pandas as pd
import dask


class Embeddings:

    def __init__(self, data: pd.DataFrame, mappings: dict):
        """

        :param data:
        :param mappings:
        """

        self.data = data
        self.mappings = mappings

        # Logging
        logging.basicConfig(level=logging.INFO, format='%(message)s\n%(asctime)s.%(msecs)03d',
                            datefmt='%Y-%m-%d %H:%M:%S')
        self.logger = logging.getLogger(__name__)

    @dask.delayed
    def map(self, series: pd.Series, dictionary: dict, field: str):
        """
        Equivalent:
            elements = series.apply(lambda x: dictionary[x])
            elements = series.map(dictionary)

        :param series:
        :param dictionary:
        :param field:
        :return:
        """

        elements = series.map(dictionary)
        lists = elements.tolist()
        frame = pd.DataFrame(data=lists, columns=['{}_01'.format(field), '{}_02'.format(field)])
        return frame

    def exc(self):
        """

        :return:
        """

        computations = []
        for k, v in self.mappings.items():
            frame = self.map(series=self.data[k], dictionary=v, field=k)
            computations.append(frame)

        dask.visualize(computations, filename='computations', format='pdf')
        calculations = dask.compute(computations, scheduler='processes')[0]
        transform = pd.concat(calculations, axis=1)
        self.logger.info(transform)
