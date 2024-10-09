"""Module tags.py"""
import collections
import json
import logging
import os

import dask.dataframe as dfr
import numpy as np
import pandas as pd

import config
import src.elements.text_attributes
import src.functions.objects
import src.functions.streams


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
        """

        :param pathstr:
        :return:
        """

        uri = os.path.join(self.__configurations.data, pathstr)
        text = src.elements.text_attributes.TextAttributes(uri=uri, header=0)

        return self.__streams.read(text=text)

    def __frequencies(self, data: pd.DataFrame):
        """

        :param data:
        :return:
        """

        # Tags: tag/annotation/category/parent/name
        tags = self.__references(pathstr='tags.csv')
        descriptions = tags[['tag', 'name']].set_index('tag').to_dict()['name']

        # The frequencies
        frequencies = data['tagstr'].str.split(pat=',', n=-1, expand=False).map(collections.Counter).sum()
        items = [[k, frequencies[k], descriptions[k]] for k, v in frequencies.items()]

        # Hence
        frame = pd.DataFrame(data=items, columns=['tag', 'frequency', 'name'])
        frame = frame.copy().merge(tags[['tag', 'parent']], on='tag', how='left')
        frame.rename(columns={'tag': 'id', 'frequency': 'value'}, inplace=True)

        return frame

    def __addendum(self):
        """

        :return:
        """

        # Categories: category/name/parent
        # Exclude _Miscellaneous_
        categories = self.__references(pathstr='categories.csv')
        categories: pd.DataFrame = categories.copy().loc[categories['category'] != 'O', :]

        # Set all values to Null/NaN
        categories['value'] = None
        categories.rename(columns={'category': 'id'}, inplace=True)

        return categories

    def __persist(self, blob: pd.DataFrame, name: str):
        """

        :param blob: The data being saved as structurally required
        :param name: The name of the file; including the extension
        :return:
        """

        path = os.path.join(self.__configurations.warehouse, name)
        nodes = blob.to_dict(orient='records')

        try:
            with open(file=path, mode='w', encoding='utf-8') as disk:
                json.dump(obj=nodes, fp=disk, ensure_ascii=False, indent=4)
            logging.info('%s: succeeded', name)
        except IOError as err:
            raise err from err

    def exc(self):
        """
        data['tagstr'].str.split(pat=',', n=-1, expand=False).map(collections.Counter)

        :return:
        """

        # The data, frequencies, and addendum
        data = self.__data()
        frequencies = self.__frequencies(data=data)
        addendum = self.__addendum()

        bursts = pd.concat((frequencies, addendum))
        self.__persist(blob=bursts, name='bursts.json')
