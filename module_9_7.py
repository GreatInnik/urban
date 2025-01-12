def is_prime(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if result <= 1:
            return f"{result} - Составное"
        for i in range(2, int(result ** 0.5) + 1):
            if result % i == 0:
                return f"{result} - Составное"
        return f"{result} - Простое"
    return wrapper

@is_prime
def sum_three(first, second, third):
    result = first + second + third
    return result

result = sum_three(2, 3, 6)

print(result)