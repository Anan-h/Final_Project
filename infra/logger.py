import logging


class Logger:
    logging.basicConfig(filename="../Trello.log",
                        level=logging.INFO, format='%(asctime)s: %(levelname)s: %(message)s ',
                        force=True)
