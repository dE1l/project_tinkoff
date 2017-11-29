import logging
from os import path


def logger_conf():
    return {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "simple": {
                "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
            }
        },

        "handlers": {
            "console": {
                "class": "logging.StreamHandler",
                "level": "DEBUG",
                "formatter": "simple",
                "stream": "ext://sys.stdout"
            },

            "info_file_handler": {
                "class": "logging.handlers.RotatingFileHandler",
                "level": "DEBUG",
                "formatter": "simple",
                "filename": path.join(path.dirname(path.realpath(__file__)), "logs", "info.log"),
                "maxBytes": 10485760,
                "backupCount": 3,
                "encoding": "utf8"
            },

            "error_file_handler": {
                "class": "logging.handlers.RotatingFileHandler",
                "level": "ERROR",
                "formatter": "simple",
                "filename": path.join(path.dirname(path.realpath(__file__)), "logs", "errors.log"),
                "maxBytes": 10485760,
                "backupCount": 20,
                "encoding": "utf8"
            }
        },

        "loggers": {
            'my_app': {
                'handlers': ['console'],
                'level': logging.DEBUG
            }
        },

        "root": {
            "level": "DEBUG",
            "handlers": ["console", "info_file_handler", "error_file_handler"]
        }
    }