import os
import logging.config

# 日志文件配置
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
LOG_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        'verbose': {
            'format': '%(levelname)s - [%(asctime)s] - %(message)s - %(pathname)s[line:%(lineno)d] -p%(process)s -t%(thread)s'
        },
        "simple": {
            "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        }
    },
    "handlers":
        {
            "console": {
                "class": "logging.StreamHandler",
                "level": "DEBUG",
                "formatter": "simple",
                # "formatter": "verbose",
                "stream": "ext://sys.stdout"
            },
            'file': {
                'level': 'DEBUG',
                'class': 'src.applications.utils.TimedRotatingFileHandler.MultiCompatibleTimedRotatingFileHandler',
                'filename': os.path.join(BASE_DIR, 'logs/fast_api_demo.log'),
                'when': 'midnight',
                'interval': 1,
                'formatter': 'verbose',
                'encoding': 'utf-8',
            },
        },
    "loggers": {
        "robot": {
            "level": "DEBUG",
            "handlers": ["console", "file"],
            "propagate": True
        }
    }
}

logging.config.dictConfig(LOG_CONFIG)
logger = logging.getLogger('fast_api_demo')