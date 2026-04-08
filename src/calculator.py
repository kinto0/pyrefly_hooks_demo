from typing import Sequence


def add(a: float, b: float) -> float:
    return a + b


def subtract(a: float, b: float) -> float:
    return a - b


def multiply(a: float, b: float) -> float:
    return a * b


def divide(a: float, b: float) -> float:
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b


def power(base: float, exponent: int) -> float:
    return base ** exponent


def average(numbers: Sequence[float]) -> float:
    if not numbers:
        raise ValueError("Cannot compute average of empty sequence")
    return sum(numbers) / len(numbers)


def clamp(value: float, min_val: float, max_val: float) -> float:
    if min_val > max_val:
        raise ValueError("min_val must be <= max_val")
    return max(min_val, min(max_val, value))


def factorial(n: int) -> int:
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n <= 1:
        return 1
    result: int = 1
    for i in range(2, n + 1):
        result *= i
    return result
