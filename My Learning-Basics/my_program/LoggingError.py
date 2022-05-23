# Reference Link https://stackoverflow.com/questions/3383865/how-to-log-error-to-file-and-not-fail-on-exception -> Logging module. https://docs.python.org/3/library/logging.html#module-logging
import logging

logging.basicConfig(filename="/Users/aravindv/Documents/Programming/Python/myapp.log", level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(name)s %(message)s')
logger = logging.getLogger(__name__)

try:
    a = 1 / 0
    print(a)
    b = [1, 2, 3]
    print(b[2])
except ZeroDivisionError as err:
    logger.error(err)
except IndexError as err:
    logger.error(err)
else:
    print ("No exceptions found")
finally:
    print("Thank You")