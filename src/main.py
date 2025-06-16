import math
from typing import Union


class Calculator:
    """
    Сложение +
    Вычитание -
    Умножение *
    Деление /
    Возведение в степень ^
    Извлечение квадратного корня √
    Проценты %
    """

    def add(self, x: Union[int, float], y: Union[int, float]) -> int | float:
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise TypeError("Both arguments should be numeric")
        return x + y

    def minus(self, x: Union[int, float], y: Union[int, float]) -> int | float:
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise TypeError("Both arguments should be numeric")
        return x - y

    def multiplication(self, x: Union[int, float], y: Union[int, float]) -> int | float:
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise TypeError("Both arguments should be numeric")
        return x * y

    def divide(self, x: Union[int, float], y: Union[int, float]) -> int | float:
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise TypeError("Both arguments should be numeric")
        if y == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return x / y

    def exponentiation(self, x: Union[int, float], y: Union[int, float]) -> int | float:
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise TypeError("Both arguments should be numeric")
        return x**y

    def square_root(self, x: Union[int, float]) -> int | float:
        if not isinstance(x, (int, float)):
            raise TypeError("Argument should be numeric")
        return math.sqrt(x)

    def percent(self, x: Union[int, float]) -> int | float:
        if not isinstance(x, (int, float)):
            raise TypeError("Argument should be numeric")
        return x / 100


if __name__ == "__main__":
    calculator = Calculator()
