import os

def procesar_archivo(nombre_archivo, nombre_tabla):
    # Ruta al escritorio
    ruta_escritorio = os.path.join(os.path.expanduser('~'), 'Desktop')
    ruta_archivo = os.path.join(ruta_escritorio, nombre_archivo)

    # Leer el archivo
    with open(ruta_archivo, 'r') as archivo:
        lineas = archivo.readlines()

    # Procesar cada línea
    valores_sql = []
    for linea in lineas:
        linea = linea.strip()  # Limpiar espacios en blanco y saltos de línea
        if '[[' in linea:
            # Dividir la línea por '[[', y limpiar cada fragmento
            partes = [parte.strip() for parte in linea.split('[[')]
        else:
            # Tratar la línea como un único valor
            partes = [linea]

        # Crear la cadena de la forma ('valor1', 'valor2', ...)
        valor = "(" + ", ".join(f"'{parte}'" for parte in partes) + ")"
        valores_sql.append(valor)

    # Guardar los valores en un nuevo archivo en el escritorio, con el formato correcto
    ruta_salida = os.path.join(ruta_escritorio, 'output_values.txt')
    with open(ruta_salida, 'w') as archivo_salida:
        # Escribir la instrucción inicial INSERT INTO
        archivo_salida.write(f"INSERT INTO {nombre_tabla} VALUES\n")

        # Unir todos los valores con comas, excepto el último que lleva punto y coma
        for i, valor in enumerate(valores_sql):
            if i < len(valores_sql) - 1:
                archivo_salida.write(valor + ",\n")
            else:
                archivo_salida.write(valor + ";")

    return "Valores generados y guardados en: " + ruta_salida

# Uso del código
nombre_archivo = 'prueba.txt'  # Cambia esto por el nombre de tu archivo en el escritorio
nombre_tabla = 'gasolinera'          # Cambia esto por el nombre de tu tabla en la base de datos
resultado = procesar_archivo(nombre_archivo, nombre_tabla)
print(resultado)
