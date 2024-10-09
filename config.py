"""config.py"""
import os


class Config:
    """
    Config
    """

    def __init__(self) -> None:
        """
        Constructor
        """

        # The raw data store
        self.data = os.path.join(os.getcwd(), 'data', 'text')

        # The warehouse; for the outputs.
        self.warehouse = os.path.join(os.getcwd(), 'warehouse')
