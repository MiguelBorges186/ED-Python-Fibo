def fibonacci(n):
    serie = [0, 1]
    while len(serie) < n:
        serie.append(serie[-1] + serie[-2])
    return serie[:n]

# Ejemplo: primeros 10 términos
n = 10
print(f"Serie de Fibonacci con {n} términos:")
print(fibonacci(n))
