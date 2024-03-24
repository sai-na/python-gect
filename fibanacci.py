def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Number of terms in the Fibonacci series
# terms = int(input("Enter the number of terms: "))

# if terms <= 0:
#     print("Please enter a positive integer.")
# else:
#     print("Fibonacci sequence:")
#     for i in range(terms):
#         print(fibonacci(i), end=" ")
print(fibonacci(40))