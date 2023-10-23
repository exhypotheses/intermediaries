import os


class Config:

    def __init__(self):
        """
        Constructor
        self.root = os.path.abspath(__package__)
        """

        # Paths
        self.warehouse = os.path.join(os.getcwd(), 'warehouse')

        # Seed
        self.SEED = 5
