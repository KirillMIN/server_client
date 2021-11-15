import logging
import inspect
import logs.logs_configure.client_logs
import logs.logs_configure.server_logs


logger_server = logging.getLogger('server')


def log1(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        logger_server.debug(
            f'функция {func.__name__}, ее аргументы {args}, {kwargs} \n'
            f'модуль из которой вызвана исходная функция {func.__module__} \n'
            f'функция из которой вызвана исходная функция {inspect.stack()[1][3]}', stacklevel=2
        )
        """
        for elem in inspect.stack():
            print(elem)
        """
        return res

    return wrapper

