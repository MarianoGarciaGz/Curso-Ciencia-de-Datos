# Crear un programa para crear una lista de marcas de coches, solicitarlos al usuario y guardarlos en una lista. 
# Por ultimo imprimir la lista completa.

array_autos = []

while True:
    print("Opciones:")
    print("1. Añadir nuevos usuarios")
    print("2. Listar IDs de usuarios registrados")
    print("3. Salir")

    opcion = input("Selecciona una opción (1, 2, 3, 4 o 5): ")

    if opcion == "1":
      name = input("Ingresar marca: ")
      # Almacenar la información en un diccionario
      auto = {
          'Name': name,
      }
      array_autos.append(auto)

    elif opcion == "2":
        for i, _ in enumerate(array_autos):
            print(array_autos[i])

    elif opcion == "5":
        print("Saliendo...")
        break

    else:
        print("Opción no válida. Inténtalo nuevamente.")
