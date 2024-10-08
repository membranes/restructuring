import os
import logging

import pandas as pd

import config

import src.elements.text_attributes
import src.functions.streams


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

    def exc(self):
        """

        :return:
        """

        # The data
        data: pd.DataFrame = self.__read()
        self.__logger.info(data.head())

        # Dictionary
        self.__logger.info(data.to_dict(orient='tight'))
