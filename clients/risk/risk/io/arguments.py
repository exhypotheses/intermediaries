import requests
import yaml
import collections

class Arguments:

    def __init__(self):
        """

        """

    def url(self, urlstring: str) -> requests.models.Response:
        """
        Ascertains that the URL argument is valid

        :param urlstring: A URL string (to a YAML file)
        :return: The URL string if it is a valid URL, otherwise raise an error
        """

        print(urlstring)

        try:
            req = requests.get(url=urlstring)
            req.raise_for_status()
        except requests.exceptions.RequestException as err:
            raise err

        return req

    @staticmethod
    def parameters(elements: requests.models.Response):
        """
        :param elements: The content of the input YAML file
        :return: A dot map of the parameters in the YAML file; and supplementary parameters
        """

        text = yaml.safe_load(elements.text)

        DataParameters = collections.namedtuple(
            typename='DataParameters',
            field_names=['data_url', 'basename', 'data_sources_dictionary', 'definitions_of_categories',
                         'fields', 'types'])