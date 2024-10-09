"""Module tags.py"""
import collections
import logging
import os

import dask.dataframe as dfr
import pandas as pd

import config
import src.functions.streams
import src.elements.text_attributes


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

        # References
        self.__streams = src.functions.streams.Streams()

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

    def __references(self, pathstr: str):

        uri = os.path.join(self.__configurations.data, pathstr)
        text = src.elements.text_attributes.TextAttributes(uri=uri, header=0)

        return self.__streams.read(text=text)

    def exc(self):
        """
        data['tagstr'].str.split(pat=',', n=-1, expand=False).map(collections.Counter)

        :return:
        """

        # The data
        data = self.__data()
        tags = self.__references(pathstr='tags.csv')
        categories = self.__references(pathstr='categories.csv')

        # Definitions
        definitions = tags[['tag', 'name']].set_index('tag').to_dict()['name']

        # The frequencies
        frequencies = data['tagstr'].str.split(pat=',', n=-1, expand=False).map(collections.Counter).sum()



        items = [[k, frequencies[k], definitions[k]] for k, v in frequencies.items()]
        frame = pd.DataFrame(data=items, columns=['tag', 'frequency', 'name'])
        frame = frame.copy().merge(tags[['tag', 'category']], on='tag', how='left')
        frame.rename(columns={'tag': 'id', 'category': 'parent', 'frequency': 'value'}, inplace=True)
        self.__logger.info(frame)
