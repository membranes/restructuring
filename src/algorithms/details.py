import os
import logging

import pandas as pd

import config

import src.elements.text_attributes
import src.functions.streams
import src.functions.objects


class Details:

    def __init__(self):
        """
        Constructor
        """

        # Configurations
        self.__configurations = config.Config()

        # The data file
        self.__filepath = os.path.join(self.__configurations.data, 'details.csv')

        # Logging
        logging.basicConfig(level=logging.INFO,
                            format='\n\n%(message)s\n%(asctime)s.%(msecs)03d',
                            datefmt='%Y-%m-%d %H:%M:%S')
        self.__logger = logging.getLogger(__name__)

    def __read(self) -> pd.DataFrame:
        """

        :return:
        """

        text = src.elements.text_attributes.TextAttributes(uri=self.__filepath, header=0)

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

    def exc(self):
        """

        :return:
        """

        # The data
        data: pd.DataFrame = self.__read()
        self.__logger.info(data.head())

        # Dictionary
        message = self.__persist(blob=data, name='details')
        self.__logger.info(message)
