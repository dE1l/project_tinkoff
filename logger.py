import logging
from os import getcwd, path


def logger_conf():
    pass
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
                "level": "INFO",
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
            "my_module": {
                "level": "ERROR",
                "handlers": ["console"],
                "propagate": "no"
            },
            'requests.packages.urllib3': {
                'handlers': ['info_file_handler', 'console'],
                'level': logging.DEBUG
            }
        },

        "root": {
            "level": "INFO",
            "handlers": ["console", "info_file_handler", "error_file_handler"]
        }
    }
