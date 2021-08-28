import argparse
import os
import sys
import logging


def main():
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

    # The data
    data = risk.io.instances.Instances(parameters=data_).exc()
    logger.info('\n%s', data.info())

    pocket, mappings = risk.io.assets.Assets(assets_=assets_).exc()
    logger.info(pocket.keys())
    logger.info(mappings)

    x_testing_, y_testing_ = risk.functions.preprocessing.Preprocessing(
        pocket=pocket, mappings=mappings, fields=data_.fields).exc(data=data)
    logger.info(x_testing_.info())
    logger.info(y_testing_)


if __name__ == '__main__':

    # Paths
    root = os.getcwd()
    sys.path.append(root)
    sys.path.append(os.path.join(root, 'risk'))

    # Logging
    logging.basicConfig(level=logging.INFO, format='%(message)s\n%(asctime)s.%(msecs)03d', datefmt='%Y-%m-%d %H:%M:%S')
    logger = logging.getLogger(__name__)

    # Classes
    import risk.io.arguments
    import risk.io.instances
    import risk.io.assets
    import risk.functions.preprocessing

    # Parse Arguments
    arguments = risk.io.arguments.Arguments()
    parser = argparse.ArgumentParser()

    parser.add_argument('elements',
                        type=arguments.url,
                        help='The URL of a YAML of parameters; refer to the README notes.')
    args = parser.parse_args()
    data_, assets_ = arguments.parameters(elements=args.elements)

    main()
