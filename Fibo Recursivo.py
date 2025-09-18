#Miguel Ángel Borges Borges
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Ejemplo: primeros 10 términos
n = 10
serie = [fibonacci(i) for i in range(n)]
print(f"Serie de Fibonacci con {n} términos (recursiva):")
print(serie)

