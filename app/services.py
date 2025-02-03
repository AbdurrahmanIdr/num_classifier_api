"""
This module provides various utility functions to determine the properties of numbers.

It includes functions to check if a number is prime, perfect, or an Armstrong number,
and a function to get a dictionary of these properties for a given number.
"""

import math

def is_prime(n):
    """
    Check if a number is prime.

    Args:
        n (int): The number to check.

    Returns:
        bool: True if the number is prime, False otherwise.
    """
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def is_perfect(n):
    """
    Check if a number is perfect.

    Args:
        n (int): The number to check.

    Returns:
        bool: True if the number is perfect, False otherwise.
    """
    return sum(i for i in range(1, n) if n % i == 0) == n

def is_armstrong(n):
    """
    Check if a number is an Armstrong number.

    Args:
        n (int): The number to check.

    Returns:
        bool: True if the number is an Armstrong number, False otherwise.
    """
    digits = [int(d) for d in str(n)]
    return sum(d ** len(digits) for d in digits) == n

def get_number_properties(n):
    """
    Get various properties of a number.

    Args:
        n (int): The number to check.

    Returns:
        dict: A dictionary containing the properties of the number.
    """
    return {
        "is_prime": is_prime(n),
        "is_perfect": is_perfect(n),
        "properties": (
            ["armstrong", "odd"] if is_armstrong(n) and n % 2 != 0 else
            ["armstrong", "even"] if is_armstrong(n) else
            ["odd"] if n % 2 != 0 else
            ["even"]
        ),
        "digit_sum": sum(int(d) for d in str(n))
    }
