"""Module networks.py"""
import logging
import os

import pandas as pd

import config
import src.elements.text_attributes
import src.functions.objects
import src.functions.streams


class Networks:
    """
    Prepares data structures for network graphs
    """

    def __init__(self):
        """
        Constructor
        """

        # Configurations
        self.__configurations = config.Config()

        # Logging
        logging.basicConfig(level=logging.INFO,
                            format='\n\n%(message)s\n%(asctime)s.%(msecs)03d',
                            datefmt='%Y-%m-%d %H:%M:%S')
        self.__logger = logging.getLogger(__name__)

    @staticmethod
    def __read(uri: str) -> pd.DataFrame:
        """

        :param uri: The path & file name string of the source data file
        :return:
        """

        text = src.elements.text_attributes.TextAttributes(uri=uri, header=0)

        return src.functions.streams.Streams().read(text=text)

    def __persist(self, blob: pd.DataFrame, filename_stem: str) -> str:
        """

        :param blob: The data being saved as structurally required
        :param filename_stem: The name of the file name's stem
        :return:
        """

        # Save
        return src.functions.objects.Objects().write(
            nodes=blob.to_dict(orient='tight'),
            path=os.path.join(self.__configurations.warehouse, f'{filename_stem}.json'))

    def exc(self, filename_stem: str):
        """

        :param filename_stem:
        :return:
        """

        # The data file
        uri = os.path.join(self.__configurations.data, f'{filename_stem}.csv')

        # The data
        data: pd.DataFrame = self.__read(uri=uri)
        self.__logger.info(data.head())

        # Dictionary
        message = self.__persist(blob=data, filename_stem=filename_stem)
        self.__logger.info(message)
