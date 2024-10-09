"""Module interface.py"""
import src.algorithms.networks


class Interface:
    """
    The interface to the data package's classes
    """

    def __init__(self):
        """
        Constructor
        """

        self.__networks = src.algorithms.networks.Networks()

    def exc(self):
        """

        :return:
        """

        # Network Graphs
        networks = ['classes', 'details']

        for network in networks:
            self.__networks.exc(filename_stem=network)
