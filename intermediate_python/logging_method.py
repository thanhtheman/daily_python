import logging

#only running this code once at the beginning
logging.basicConfig(level=logging.DEBUG, filename ='log.txt', filemode='w', format='%(asctime)s - %(levelname)s - %(message)s')

#log a variable
x = 2

# logging.debug(f'this is {x}')
# try:
#     b = 2 / 0
# except Exception as e:
#     logging.error(e, exc_info=True)

logger = logging.getLogger(__name__)

handler = logging.FileHandler('test.log')
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

logger.info('test the customer logger')

