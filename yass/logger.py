# YASS, Yet Another Subdomainer Software
# Copyright 2015 Francesco Marano (@mrnfrancesco) and individual contributors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


import inspect
import logging
from logging.config import dictConfig
from colorama import Style, Back, Fore
import colorama

__all__ = {'MODULE_DEPTH', 'CLASS_DEPTH', 'METHOD_DEPTH', 'logger'}

MODULE_DEPTH = 1
CLASS_DEPTH = 2
METHOD_DEPTH = 3


def logger(depth=3):
    """
    Provide a logger instance with no need to specify the name, cause it will get it automagically.
    To use it just import the method at module level with

    >>> from logger import logger

    Then use it in whatever level you want (module, function, class or method), e.g.:

    >>> if __name__ == '__main__':
    >>>     logger().info('info message')

    Remember **NOT** to call `logging.basicConfig()`! It should be done once by main function.

    :param depth: the depth level of the provided logger (1: module only, 2: module.class, 3: module.class.method)
    :type depth: int
    :return: a logger object
    :rtype: logging.Logger

    *Thanks to Zaar Hai answer to* `logger chain in python <http://stackoverflow.com/a/3060995/3549503>`_
    *question on stackoverflow!*
    """
    caller_frame = inspect.stack(context=False)[1]
    caller = caller_frame[0]
    lname = '__hierlogger_{depth}__'.format(depth=depth)
    if lname not in caller.f_locals:
        logger_name = str()
        if depth >= 1:
            try:
                logger_name = inspect.getmodule(caller).__name__
            except:
                pass
        if depth >= 2 and 'self' in caller.f_locals:
            logger_name += ('.' if logger_name else '') + caller.f_locals['self'].__class__.__name__
        if depth >= 3 and caller_frame[3] and caller_frame[3] != '<module>':
            logger_name += ('.' if logger_name else '') + caller_frame[3]
        logger = logging.getLogger(logger_name)
        logger.addHandler(logging.NullHandler())
        caller.f_locals[lname] = logger
    return caller.f_locals[lname]


def config(colored=True, debugging=False, level='info'):
    level = str(level)  # to avoid error if level is None

    dictConfig({
        # the version of the logging configuration dictionary
        'version': 1,
        # whether the configuration is to be interpreted as incremental to the existing configuration.
        'incremental': False,
        # whether any existing loggers are to be disabled.
        'disable_existing_loggers': True,
        'formatters': {
            'debugging': {
                'format': "[%(asctime)s]\t%(levelname)-8s\t%(name)s:%(lineno)d -> %(message)s",
                'datefmt': "%H:%M:%S"
            },
            'default': {
                'format': "[%(levelname)-8s]\t%(message)s",
            }
        },
        'handlers': {
            'custom': {
                'formatter': 'debugging' if debugging else 'default',
                'class': 'yass.logger._ColorStreamHandler' if colored else 'logging.StreamHandler',
                'stream': 'ext://sys.stdout'
            }
        },
        'root': {
            'propagate': True,
            'level': getattr(logging, level.upper(), logging.INFO),
            'handlers': ['custom'] if level != str(None) else []
        }
    })


class _ColorStreamHandler(logging.StreamHandler):
    DEFAULT = Style.RESET_ALL
    CRITICAL = Back.RED
    ERROR = Fore.RED
    WARNING = Fore.YELLOW
    INFO = Fore.GREEN
    DEBUG = Fore.MAGENTA

    colorama.init(autoreset=True)

    def format(self, record):
        text = logging.StreamHandler.format(self, record)
        color = getattr(_ColorStreamHandler, record.levelname, _ColorStreamHandler.DEFAULT)
        return color + text + _ColorStreamHandler.DEFAULT