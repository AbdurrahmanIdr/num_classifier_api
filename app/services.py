import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def is_perfect(n):
    return sum(i for i in range(1, n) if n % i == 0) == n

def is_armstrong(n):
    digits = [int(d) for d in str(n)]
    return sum(d ** len(digits) for d in digits) == n

def get_number_properties(n):
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
