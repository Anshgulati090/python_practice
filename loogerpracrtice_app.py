import logging

#basic configuration for the logging
logging.basicConfig(
    level = logging.DEBUG,
    format='%(asctime)s -%(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        logging.FileHandler('app.log'), #file name
        logging.StreamHandler()  #used for addingg logs in the file
    ]
)
logger = logging.getLogger("ArithmeticApp")
def add(a,b):
    result = a+b
    logger.debug(f"Additon of number:{a}+{b} {result}")
    return result
def subtract(a,b):
    result = a-b
    logger.debug(f"SUbtraction of numbers:{a}+{b} {result}")
    return result
def multiplication(a,b):
    result = a*b
    logger.debug(f"Multipication of numbers: {a}*{b} {result}")
    return result
def division(a,b):
    try:
        result = a/b
        logger.debug(f"division of numbers:{a}/{b} {result}")
        return result
    except ZeroDivisionError:
        logger.error(f"Division of number by zero")
        return None
add(5,6)
subtract(6,7)
multiplication(2,5)
division(0,2)
division(2,0)