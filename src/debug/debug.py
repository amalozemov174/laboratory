import logging
logging.basicConfig(filename='debug.log', level=logging.INFO)
logger = logging.getLogger(__name__)
logger.info('Started')
first = int(input("Первое число: "))
assert first >= 0
second = int(input("Второе число: "))
assert first >= 0
logger.info(f'Первое число: {first}')
logger.info(f'Второе число: {second}')
sum = first + second
diff = first - second
multiplication = first * second
assert second != 0
quotient = first / second
print("Сумма: ", sum)
print("Разница: ", diff)
print("Произведение: ", multiplication)
print("Частное: ", quotient)
logger.info('Finished')