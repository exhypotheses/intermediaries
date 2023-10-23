import os
import sys

import logging


def main():

    string = alphanumeric.numeric()
    logger.info('\n%s', string)


if __name__ == '__main__':
    root = os.getcwd()
    sys.path.append(root)
    sys.path.append(os.path.join(root, 'structures'))

    logging.basicConfig(level=logging.INFO, format='%(message)s\n%(asctime)s.%(msecs)03d', datefmt='%Y-%m-%d %H:%M:%S')
    logger = logging.getLogger(__name__)

    import structures.functions.alphanumeric

    alphanumeric = structures.functions.alphanumeric.AlphaNumeric()

    main()