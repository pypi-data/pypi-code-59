import logging.config

# "114198773012" is our test account
AWS_TEST_ACCOUNT = "114198773012"

# setup logging
d = {
    "version": 1,
    "formatters": {
        "detailed": {
            "class": "logging.Formatter",
            "format": "%(asctime)s: %(levelname)s: %(module)s.%(funcName)s():%(lineno)d: %(message)s",
        }
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "level": "INFO",
            "formatter": "detailed",
        },
    },
    "root": {"level": "DEBUG", "handlers": ["console"], "propagate": True},
}
logging.config.dictConfig(d)
