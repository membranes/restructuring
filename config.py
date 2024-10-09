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
        self.data = os.path.join(os.getcwd(), 'data')

        # The warehouse; for the outputs.
        self.warehouse = os.path.join(os.getcwd(), 'warehouse')

        self.definitions = {'O': 'Miscellaneous',
                            'B-geo': 'Beginning | Geographic Point', 'B-tim': 'Beginning | Time',
                            'B-org': 'Beginning | Organisation', 'B-per': 'Beginning | Person',
                            'B-gpe': 'Beginning | Geopolitical Entity',
                            'I-geo': 'Inside | Geographic Point', 'I-tim': 'Inside | Time',
                            'I-org': 'Inside | Organisation', 'I-per': 'Inside | Person',
                            'I-gpe': 'Inside | Geopolitical Entity'}
