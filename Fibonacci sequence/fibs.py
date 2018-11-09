def fibonacciRabbits(n,k):
    if n <= 2:
        return (1)
    else:
        return (fibonacciRabbits(n-1,k) + fibonacciRabbits(n-2,k)*k)
print(fibonacciRabbits(5,3))