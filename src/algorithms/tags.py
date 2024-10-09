"""Module tags.py"""
import collections
import logging
import os

import dask.dataframe as dfr
import pandas as pd

import config


class Tags:
    """
    Class Tags
    """

    def __init__(self):
        """
        Constructor
        """

        self.__configurations = config.Config()

        self.__uri = os.path.join(self.__configurations.data, 'data.csv')

        # Logging
        logging.basicConfig(level=logging.INFO,
                            format='\n\n%(message)s\n%(asctime)s.%(msecs)03d',
                            datefmt='%Y-%m-%d %H:%M:%S')
        self.__logger = logging.getLogger(__name__)

    def __data(self) -> pd.DataFrame:
        """

        :return:
        """

        try:
            data: dfr.DataFrame = dfr.read_csv(path=self.__uri, header=0)
        except ImportError as err:
            raise err from err

        return data.compute()

    def exc(self):
        """

        :return:
        """

        # The data
        data = self.__data()

        # The frequencies of the tags, by sentence and overarching
        occurrences = data['tagstr'].str.split(pat=',', n=-1, expand=False).map(collections.Counter)
        frequencies = data['tagstr'].str.split(pat=',', n=-1, expand=False).map(collections.Counter).sum()

        self.__logger.info(data.head())
        self.__logger.info(occurrences)
        self.__logger.info(frequencies)

        # Definitions
        definitions = self.__configurations.definitions

        items = [[k, frequencies[k], definitions[k]] for k, v in frequencies.items()]
        self.__logger.info(items)

        frame = pd.DataFrame(data=items, columns=['tag', 'frequency', 'name'])
        self.__logger.info(frame)
