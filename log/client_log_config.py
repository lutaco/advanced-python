import logging
from os import sys
from client.settings import ENCODING

# Создаем объект-логгер
logger = logging.getLogger('client.main')

# Создаем объект форматирования:
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s ")

# Создаем файловый обработчик логирования (можно задать кодировку):
fh = logging.FileHandler("client.info.log", encoding=ENCODING)
fh.setLevel(logging.DEBUG)
fh.setFormatter(formatter)

# Потоковый обработчик
std_hand = logging.StreamHandler(sys.stdout)
std_hand.setLevel(logging.DEBUG)
std_hand.setFormatter(formatter)

# Добавляем в логгер новый обработчик событий и устанавливаем уровень логирования
logger.addHandler(fh)
logger.addHandler(std_hand)
logger.setLevel(logging.DEBUG)

if __name__ == '__main__':
    # Создаем потоковый обработчик логирования (по умолчанию sys.stderr):
    console = logging.StreamHandler()
    console.setLevel(logging.DEBUG)
    console.setFormatter(formatter)
    logger.addHandler(console)
    logger.info('Тестовый запуск логирования')