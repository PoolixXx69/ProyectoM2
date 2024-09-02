def verificar_longitud_palabra():
    MIN_LONGITUD = 4
    MAX_LONGITUD = 8

    while True:
        palabra = input("Introduce una palabra: ")

        if palabra.lower() == "salir":
            break

        longitud = len(palabra)

        if MIN_LONGITUD <= longitud <= MAX_LONGITUD:
            print("La palabra es correcta.")
        elif longitud < MIN_LONGITUD:
            print(f"Hacen falta letras, mínimo {MIN_LONGITUD} letras. Solo tiene {longitud} letras.")
        else:
            print(f"Sobran letras, máximo {MAX_LONGITUD} letras. Tiene {longitud} letras.")

if __name__ == "__main__":
    verificar_longitud_palabra()