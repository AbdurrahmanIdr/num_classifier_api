"""
This module provides various utility functions to determine the properties of numbers.

It includes functions to check if a number is prime, perfect, or an Armstrong number,
and a function to get a dictionary of these properties for a given number.
"""

import requests

def fetch_fun_fact(number):
    """
    Fetch a fun fact about a given number from the Numbers API.

    Args:
        number (int): The number to fetch a fun fact for.

    Returns:
        str: A fun fact about the number, or a default message if no fact is available.
    """
    response = requests.get(f"http://numbersapi.com/{number}/math?json", timeout=5)
    if response.status_code == 200:
        return response.json().get("text", "No fact available")
    return "No fact available"
