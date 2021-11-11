import logging
import os
from logging import handlers
p_path = os.path.abspath(__file__).split('\\')[:-2]
p_path.append('logs_files')
p_path = '\\'.join(p_path)
p_path = os.path.join(p_path, 'servers.log')
server_format = logging.Formatter("%(levelname)-10s %(asctime)s %(module)s %(message)s %(funcName)s")
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(server_format)
stream_handler.setLevel(logging.DEBUG)
log_file = handlers.TimedRotatingFileHandler(p_path, encoding='utf-8', interval=1, when='midnight')
log_file.setFormatter(server_format)
log_file.setLevel(logging.DEBUG)

logger = logging.getLogger('server')
logger.addHandler(stream_handler)
logger.addHandler(log_file)
logger.setLevel(logging.DEBUG)

if __name__ == '__main__':
    logger.critical('критическая ошибка')
    logger.error('ошибка')
    logger.info('информация')
    logger.debug('отладка')