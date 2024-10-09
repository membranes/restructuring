import src.algorithms.networks


class Interface:

    def __init__(self):
        self.__networks = src.algorithms.networks.Networks()

    def exc(self):
        networks = ['classes', 'details']

        for network in networks:
            self.__networks.exc(filename_stem=network)
