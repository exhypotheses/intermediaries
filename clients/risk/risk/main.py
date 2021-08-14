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
    data, mappings = risk.io.instances.Instances(parameters=parameters).exc()
    logger.info('\n%s', data.info())

    # Step 1: Embeddings
    embeddings = risk.functions.embeddings.Embeddings(data=data, mappings=mappings, fields=parameters.fields)
    embeddings.exc()


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
    import risk.functions.embeddings

    # Parse Arguments
    arguments = risk.io.arguments.Arguments()
    parser = argparse.ArgumentParser()

    parser.add_argument('elements',
                        type=arguments.url,
                        help='The URL of a YAML of parameters; refer to the README notes.')
    args = parser.parse_args()
    parameters = arguments.parameters(elements=args.elements)

    main()
