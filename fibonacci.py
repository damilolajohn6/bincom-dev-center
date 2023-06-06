def fibonacci_sum(n):
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        next_number = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_number)
    return sum(fib_sequence)

result = fibonacci_sum(50)
print("Sum of the first 50 Fibonacci numbers:", result)
