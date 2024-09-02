def identificar_cuadrante(x, y):
    if x == 0 or y == 0:
        return "Las coordenadas no deben ser 0."
    elif x > 0 and y > 0:
        return "El punto se encuentra en el cuadrante I"
    elif x < 0 and y > 0:  # Corregido
        return "El punto se encuentra en el cuadrante II"
    elif x < 0 and y < 0:
        return "El punto se encuentra en el cuadrante III"
    else:  # Caso por defecto para x > 0 y y < 0
        return "El punto se encuentra en el cuadrante IV"

def main():
    while True:
        try:
            x = int(input("Ingrese el valor de X: "))
            y = int(input("Ingrese el valor de Y: "))
            resultado = identificar_cuadrante(x, y)
            print(resultado)
            break  # Salir del bucle si los valores son válidos
        except ValueError:
            print("Por favor, ingrese valores enteros válidos.")

if __name__ == "__main__":
    main()