def fibonacci_iterative(n):
    fib_sequence = []
    a, b = 0, 1
    while len(fib_sequence) < n:
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence

# Example: Generate the first 10 Fibonacci numbers
print(fibonacci_iterative(10))

def fibonacci_recursive(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_sequence = fibonacci_recursive(n - 1)
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
        return fib_sequence
    

# Example: Generate the first 10 Fibonacci numbers
print(fibonacci_recursive(10))



def fib(n):
    seq = []
    a, b = 0, 1
    while len(seq) < n:
        seq.append(a)
        a, b = b, a + b
    return seq

print(fib(10))
