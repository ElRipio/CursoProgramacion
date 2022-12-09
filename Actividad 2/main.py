def cargar_productos() -> list:
    # COMPLETAR
    # Esta función debe cargar los productos en "original.txt"
    # y guardarlos en una lista de tuplas con formato ('producto', 'precio').
    # Finalmente, debes retornar esta lista. EJ: [(pan, 250), (huevo, 200)]

    pass  # "pass" permite que el código se ejecute. Puedes borrar esta linea.


def escribir_archivo(lista_productos: list):
    # COMPLETAR
    # Esta función debe guardar los productos en el archivo "nuevo.txt".
    # Debes seguir el formato en el ejemplo.
    pass


if __name__ == "__main__":
    # NO MODIFICAR
    print('Cargando productos...')
    lista_productos = cargar_productos()
    print('Escribiendo nueva lista...')
    escribir_archivo(lista_productos)
    print('¡Programa finalizado!')
