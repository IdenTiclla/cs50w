from par import es_par

def prueba_par(n, expected):
    if es_par(n) != expected:
        print(f"ERROR on es_par({n}), expected: {expected}")
