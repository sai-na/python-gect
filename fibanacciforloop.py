import time

def fibonacci(n):
    if n <= 1:
        return n
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

# Number of terms in the Fibonacci series
terms = int(input("Enter the number of terms: "))

if terms <= 0:
    print("Please enter a positive integer.")
else:
    print("Fibonacci sequence:")
    for i in range(terms):
        start_time = time.time()
        fib_number = fibonacci(i)
        end_time = time.time()
        print(f"F({i}) = {fib_number}, Time taken: {end_time - start_time:.6f} seconds")
