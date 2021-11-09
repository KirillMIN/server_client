import logging
import os
server_format = logging.Formatter("%(levelname)-10s %(asctime)s %(module)s %(message)s %(funcName)s")
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(server_format)
stream_handler.setLevel(logging.DEBUG)


logger = logging.getLogger('client')
logger.addHandler(stream_handler)
logger.setLevel(logging.DEBUG)
if __name__ == '__main__':
    logger.critical('критическая ошибка')
    logger.error('ошибка')
    logger.info('информация')
    logger.debug('отладка')