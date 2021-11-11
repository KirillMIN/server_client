import logging
import os

from logging import handlers
p_path = os.path.abspath(__file__).split('\\')[:-2]
p_path.append('logs_files')
p_path = '\\'.join(p_path)
p_path = os.path.join(p_path, 'clients.log')
server_format = logging.Formatter("%(levelname)-10s %(asctime)s %(module)s %(message)s %(funcName)s")
stream_handler = logging.FileHandler(p_path, encoding='utf-8')
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