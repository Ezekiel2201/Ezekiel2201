
def fibonacci_generator(n):
    """Generates the first n Fibonacci numbers."""
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

# Usage: Print the first 10 numbers
for num in fibonacci_generator(10):
    print(num)
