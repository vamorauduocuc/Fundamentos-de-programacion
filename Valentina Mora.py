# ============================================================
# Sistema de administración de cartelera - CineMax (Versión 1)
# ============================================================

peliculas = {
    'P101': ['Luz de Otoño', 'drama', 110, 'B', 'Español', False],
    'P102': ['Noche Neón', 'acción', 125, 'C', 'Ingles', True],
    'P103': ['Planeta Agua', 'documental', 90, 'A', 'Español', False],
    'P104': ['Risa Total', 'comedia', 105, 'A', 'Español', True],
    'P105': ['Código Zero', 'thriller', 118, 'C', 'Ingles', True],
    'P106': ['Viaje Lunar', 'ciencia ficción', 132, 'B', 'Ingles', False],
}

cartelera = {
    'P101': [5990, 40],
    'P102': [7990, 0],
    'P103': [4990, 25],
    'P104': [6990, 12],
    'P105': [8990, 8],
    'P106': [7490, 3],
}


# ---------- FUNCIONES DE VALIDACIÓN ----------

def validar_texto(valor):
    return valor.strip() != ""


def validar_entero_positivo(valor):
    return valor > 0


def validar_entero_no_negativo(valor):
    return valor >= 0


def validar_clasificacion(valor):
    return valor in ('A', 'B', 'C')


def validar_codigo_nuevo(codigo):
    return validar_texto(codigo) and codigo.upper() not in peliculas


# ---------- FUNCIONES DEL SISTEMA ----------

def leer_opcion():
    while True:
        try:
            opcion = int(input("Ingrese opción: "))
            if 1 <= opcion <= 6:
                return opcion
            print("Debe seleccionar una opción válida")
        except ValueError:
            print("Debe seleccionar una opción válida")


def cupos_genero(genero):
    total = 0
    for codigo, datos in peliculas.items():
        if datos[1].lower() == genero.lower():
            total += cartelera[codigo][1]
    print(f"El total de cupos disponibles es: {total}")


def busqueda_precio(p_min, p_max):
    resultados = []
    for codigo, datos in cartelera.items():
        precio, cupos = datos
        if p_min <= precio <= p_max and cupos != 0:
            titulo = peliculas[codigo][0]
            resultados.append(f"{titulo}--{codigo}")
    resultados.sort()
    if resultados:
        print(f"Las películas encontradas son: {resultados}")
    else:
        print("No hay películas en ese rango de precios.")


def actualizar_precio(codigo, nuevo_precio):
    codigo = codigo.upper()
    if codigo not in cartelera:
        return False
    cartelera[codigo][0] = nuevo_precio
    return True


def agregar_pelicula(codigo, titulo, genero, duracion, clasificacion, idioma, es_3d, precio, cupos):
    codigo = codigo.upper()
    if codigo in peliculas:
        return False
    peliculas[codigo] = [titulo, genero, duracion, clasificacion, idioma, es_3d]
    cartelera[codigo] = [precio, cupos]
    return True


def eliminar_pelicula(codigo):
    codigo = codigo.upper()
    if codigo not in peliculas:
        return False
    del peliculas[codigo]
    del cartelera[codigo]
    return True


# ---------- PROGRAMA PRINCIPAL ----------

def main():
    while True:
        print("\n========== MENÚ PRINCIPAL ==========")
        print("1. Cupos por género")
        print("2. Búsqueda de películas por rango de precio")
        print("3. Actualizar precio de película")
        print("4. Agregar película")
        print("5. Eliminar película")
        print("6. Salir")
        print("=====================================")

        opcion = leer_opcion()

        if opcion == 1:
            genero = input("Ingrese género a consultar: ")
            cupos_genero(genero)

        elif opcion == 2:
            while True:
                try:
                    p_min = int(input("Ingrese precio mínimo: "))
                    p_max = int(input("Ingrese precio máximo: "))
                    if p_min < 0 or p_max < 0 or p_min > p_max:
                        print("Debe ingresar valores enteros")
                        continue
                    break
                except ValueError:
                    print("Debe ingresar valores enteros")
            busqueda_precio(p_min, p_max)

        elif opcion == 3:
            respuesta = "s"
            while respuesta == "s":
                codigo = input("Ingrese código de película: ")
                try:
                    nuevo_precio = int(input("Ingrese nuevo precio: "))
                except ValueError:
                    print("Debe ingresar un valor entero")
                    respuesta = input("¿Desea actualizar otro precio (s/n)?: ").lower()
                    continue
                if actualizar_precio(codigo, nuevo_precio):
                    print("Precio actualizado")
                else:
                    print("El código no existe")
                respuesta = input("¿Desea actualizar otro precio (s/n)?: ").lower()

        elif opcion == 4:
            codigo = input("Ingrese código de película: ")
            titulo = input("Ingrese título: ")
            genero = input("Ingrese género: ")
            try:
                duracion = int(input("Ingrese duración (minutos): "))
            except ValueError:
                duracion = -1
            clasificacion = input("Ingrese clasificación: ")
            idioma = input("Ingrese idioma: ")
            es_3d = input("¿Es 3D? (s/n): ").lower() == "s"
            try:
                precio = int(input("Ingrese precio: "))
                cupos = int(input("Ingrese cupos: "))
            except ValueError:
                precio = -1
                cupos = -1

            if not validar_codigo_nuevo(codigo):
                print("El código ya existe")
            elif not validar_texto(titulo):
                print("El título no es válido")
            elif not validar_texto(genero):
                print("El género no es válido")
            elif not validar_entero_positivo(duracion):
                print("La duración no es válida")
            elif not validar_clasificacion(clasificacion):
                print("La clasificación no es válida")
            elif not validar_texto(idioma):
                print("El idioma no es válido")
            elif not validar_entero_positivo(precio):
                print("El precio no es válido")
            elif not validar_entero_no_negativo(cupos):
                print("Los cupos no son válidos")
            else:
                if agregar_pelicula(codigo, titulo, genero, duracion, clasificacion,
                                     idioma, es_3d, precio, cupos):
                    print("Película agregada")
                else:
                    print("El código ya existe")

        elif opcion == 5:
            codigo = input("Ingrese código de película: ")
            if eliminar_pelicula(codigo):
                print("Película eliminada")
            else:
                print("El código no existe")

        elif opcion == 6:
            print("Programa finalizado.")
            break


main()
