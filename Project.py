def generate_fibonacci(n):
    fibonacci = [0, 1]
    if n == 0:
        return []
    if n == 1:
        return [0]
    while len(fibonacci) < n:
        next_number = fibonacci[-1] + fibonacci[-2]
        fibonacci.append(next_number)
    return fibonacci
print(generate_fibonacci(int(input("Enter the number of Fibonacci numbers to generate: "))))