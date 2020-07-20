# import logging.config

logging_config = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
        },
    },
    'handlers': {
        'default': {
            'level': 'INFO',
            'formatter': 'standard',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': 'robot.log',
            'maxBytes': 10000000,
            'backupCount': 10
        },
    },
    'loggers': {
        '': {
            'handlers': ['default'],
            'level': 'INFO',
        }
    }
}
