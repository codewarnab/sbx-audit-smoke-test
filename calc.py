"""Tiny calculator library (clean baseline)."""


def add(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("add expects numbers")
    return a + b


def divide(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("divide expects numbers")
    if b == 0:
        raise ValueError("division by zero")
    return a / b
