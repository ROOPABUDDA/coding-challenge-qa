import logging


class LogHelper(logging.Filter):
    def filter(self, record):
        record.prefix = ":: "
        if not hasattr(record, "transaction_data"):
            record.transaction_data = ""
            record.prefix = ""
        return True


formatter = logging.Formatter('%(levelname)s :: %(message)s %(prefix)s%(transaction_data)s')
handler = logging.StreamHandler()
handler.setLevel(level=logging.DEBUG)
handler.setFormatter(formatter)


def getLogger(name="default"):
    logger = logging.getLogger(name)
    logger.setLevel(level=logging.DEBUG)
    logger.addFilter(LogHelper())
    logger.addHandler(handler)
    return logger
