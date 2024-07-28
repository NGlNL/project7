import logging

logger = logging.getLogger(__name__)
file_handler = logging.FileHandler("logs.log", "w", encoding="utf-8")
file_formater = logging.Formatter("%(asctime)s %(name)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formater)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)
