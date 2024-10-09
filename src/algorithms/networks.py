import logging
import os

import pandas as pd

import config
import src.elements.text_attributes
import src.functions.objects
import src.functions.streams


class Networks:

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

        :return:
        """

        text = src.elements.text_attributes.TextAttributes(uri=uri, header=0)

        return src.functions.streams.Streams().read(text=text)

    def __persist(self, blob: pd.DataFrame, name: str) -> str:
        """

        :param blob:
        :param name:
        :return:
        """

        # Save
        return src.functions.objects.Objects().write(
            nodes=blob.to_dict(orient='tight'),
            path=os.path.join(self.__configurations.warehouse, f'{name}.json'))

    def exc(self, filename_stem: str):
        """

        :return:
        """

        # The data file
        uri = os.path.join(self.__configurations.data, f'{filename_stem}.csv')

        # The data
        data: pd.DataFrame = self.__read(uri=uri)
        self.__logger.info(data.head())

        # Dictionary
        message = self.__persist(blob=data, name=filename_stem)
        self.__logger.info(message)
