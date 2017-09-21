import logging
logging.basicConfig(level=logging.DEBUG)

logger = logging.getLogger(__name__)

def tests():
    logger.info('Starting nose test')
    logger.info('Finished nose test')

def train():
    logger.info('Started training')
    logger.info('Finished training')
