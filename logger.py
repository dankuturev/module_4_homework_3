from datetime import datetime, date
from functools import wraps


def logger(path):
    def _logger(function_to_log):
        @wraps(function_to_log)
        def surrogate(*args, **kwargs):
            with open(path + f'\log {date.today()}.txt', mode='a') as f:
                f.write(f'[{datetime.now()}] Вызвана функция: {function_to_log} с аргументами: {args} и {kwargs}\n')
                result = function_to_log(*args, **kwargs)
                f.write(f'[{datetime.now()}] Возвращено значение: {result}\n')
            return result
        return surrogate
    return _logger
