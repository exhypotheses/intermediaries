import os
import secrets
import numpy as np

import config


class AlphaNumeric:

    def __init__(self):
        """
        https://nitratine.net/blog/post/how-to-hash-passwords-in-python/

        """

        configurations = config.Config()
        self.rng = np.random.default_rng(configurations.SEED)

    @staticmethod
    def salt():

        return os.urandom(64)

    @staticmethod
    def secret():

        return secrets.token_bytes(nbytes=64)

    def numeric(self, low: int = (10 ** 15), high: int = (10 ** 16)):

        return self.rng.integers(low=low, high=high, size=1, dtype=np.int64)
