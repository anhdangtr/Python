import logging

#tạo logger
logger = logging.getLogger("test_logger")
logger.setLevel(logging.DEBUG)

#tạo handler
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)

#format log
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
console_handler.setFormatter(formatter)

#thêm handler vào logger
logger.addHandler(console_handler)

#log message
logger.debug("This is a debug message.")
logger.info("This is an info message.")
logger.warning("This is a warning message.")
logger.error("This is an error message.")
logger.critical("This is a critical message.")
