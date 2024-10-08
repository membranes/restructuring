"""Module main.py"""
import logging
import os
import sys


def main():
    """
    Entry point
    """

    # Logging
    logger: logging.Logger = logging.getLogger(__name__)
    logger.info('Abstracts')

    # Of interest
    src.algorithms.details.Details().exc()

    # Deleting __pycache__
    src.functions.cache.Cache().exc()


if __name__ == '__main__':

    # Setting-up
    root = os.getcwd()
    sys.path.append(root)
    sys.path.append(os.path.join(root, 'src'))

    logging.basicConfig(level=logging.INFO,
                        format='\n\n%(message)s\n%(asctime)s.%(msecs)03d',
                        datefmt='%Y-%m-%d %H:%M:%S')

    # Classes
    import config
    import src.functions.cache
    import src.functions.directories
    import src.algorithms.details

    warehouse = config.Config().warehouse
    directories = src.functions.directories.Directories()
    directories.cleanup(path=warehouse)
    directories.create(path=warehouse)

    main()
