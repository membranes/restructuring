import os
import logging

import pandas as pd

import src.functions.streams
import src.elements.text_attributes

import config


class Tags:

    def __init__(self):

        self.__configurations = config.Config()

        self.__uri = os.path.join(self.__configurations.data, 'data.csv')

        # Logging
        logging.basicConfig(level=logging.INFO,
                            format='\n\n%(message)s\n%(asctime)s.%(msecs)03d',
                            datefmt='%Y-%m-%d %H:%M:%S')
        self.__logger = logging.getLogger(__name__)

    def __data(self) -> pd.DataFrame:

        text = src.elements.text_attributes.TextAttributes(uri=self.__uri, header=0)
        streams = src.functions.streams.Streams()

        return streams.read(text=text)

    def exc(self):

        data = self.__data()
        self.__logger.info(data.head())


