# Importación de librías a ser usadas en el código
import sys
import csv
import os

# Función secundaria para la validación del correcto ingreso del archivo csv
def validar_archivocsv(nombre_archivo):
    
    # Verifica que el archivo tenga extensión .csv
    if not nombre_archivo.lower().endswith('.csv'):
        print("Error: El archivo debe tener extensión .csv.")
        return None

    # Verifica que el archivo exista
    if not os.path.isfile(nombre_archivo):
        print(f"Error: El archivo '{nombre_archivo}' no fue encontrado.")
        return None

    # Se inicia un bloque try para manejar excepciones durante la ejecución del código 
    try:
        # Se abre el archivo especificado por 'nombre_archivo' en modo de lectura ('r')
        with open(nombre_archivo, mode='r') as archivo:
            # Se crea un lector de CSV usando la librería csv, que leerá el archivo con delimitador ';'
            lector_csv = csv.DictReader(archivo, delimiter=';')

            # Definición de un conjunto con los encabezados esperados en el archivo CSV
            encabezados_esperados = {'id', 'tipo', 'monto'}

            # Verifica si los encabezados de el archivo csv son los correctos
            if lector_csv.fieldnames is None or not encabezados_esperados.issubset(lector_csv.fieldnames):
                print("Error: El archivo CSV no tiene los encabezados esperados.")
                return None

            # Se convierte el contenido del archivo CSV en una lista de diccionarios (cada fila es un diccionario)
            transacciones = list(lector_csv)

            # Verifica si el archivo contiene transacciones
            if not transacciones:
                print("Error: El archivo CSV no contiene transacciones.")
                # Si no contiene transacciones, se devuelve None y se termina la ejecución
                return None
            
            # Si todo está correcto, se devuelven las transacciones
            return transacciones
        
    # Menajo de cualquier otro error no anticipado en la ejecución del programa
    except Exception as e:
        print(f"Error: Ocurrió un error al validar el archivo: {e}")
        return None

# Función principal para el procesamiento de las transacciones bancarias
def procesar_tbancarias(nombre_archivo):
    # Se inicia un bloque try para manejar excepciones durante la ejecución del código
    try:
        # LLamado a la función secundaria "validar_archivocsv" que valida el archivo ingresado a nivel de extensión, existencia del archivo, uso correcto de cabeceras y presencia de trasacciones"
        transacciones = validar_archivocsv(nombre_archivo)
        # Validador del resultado de la función secundaria "validar_archivocsv"
        if transacciones is None:
            return

        # Luego de validado correctamente el archivo procedemos con la lógica de la función "procesar_tbancarios"

        # Declaración de variables
        balance = 0.0
        contador = {'Crédito': 0, 'Débito': 0}
        transaccion_mayor = {'id': None, 'monto': 0.0}

        # Bucle para el cálculo de los valores finales de las variables: balance, contador y transacción mayor
        for fila in transacciones:
            # Se obtiene el valor asociado a la cabecera 'tipo' del diccionario 'fila' y se asigna a la variable 'tipo'
            tipo = fila['tipo']            
            # Se convierte el valor asociado a la cabecera 'monto' del diccionario 'fila' a un número flotante y se asigna a la variable 'monto'
            monto = float(fila['monto'])            
            # Se obtiene el valor asociado a la cabecera 'id' del diccionario 'fila' y se asigna a la variable 'id_transaccion'
            id_transaccion = fila['id']

            # Identificador del 'balance' y del 'contador' en pares de valores "Crédito" y "Débito"
            if tipo == 'Crédito':
                balance += monto
                contador['Crédito'] += 1
            elif tipo == 'Débito':
                balance -= monto
                contador['Débito'] += 1

            # Identificador de la 'transacción mayor' en pares de valores "id" y "monto"
            if monto > transaccion_mayor['monto']:
                transaccion_mayor['id'] = id_transaccion
                transaccion_mayor['monto'] = monto

        # Estructura del reporte final requerido
        print("Reporte de Transacciones")
        print("---------------------------------------------")
        print(f"Balance Final: {balance:.2f}")
        print(f"Transacción de Mayor Monto: ID {transaccion_mayor['id']} - {transaccion_mayor['monto']:.2f}")
        print(f"Conteo de Transacciones: Crédito: {contador['Crédito']} Débito: {contador['Débito']}")

    # Manejo de errores relacionados con conversión de tipos de datos (por ejemplo, float(monto))
    except ValueError as e:
        print(f"Error: Se presentó un error en la conversión de datos: {e}")
    # Menajo de cualquier otro error no anticipado en la ejecución del programa
    except Exception as e:
        print(f"Error: Ocurrió un error inesperado: {e}")

# Punto de entrada del programa
if __name__ == "__main__":
    # Verificar que se haya pasado el nombre del archivo csv como argumento
    if len(sys.argv) != 2:
        print("Error: Uso incorrecto del script. Por favor, proporciona el nombre del archivo CSV como argumento.")
        print("Ejemplo: py script.py transacciones.csv")
        sys.exit(1)

    # Obtener el nombre del archivo desde los argumentos
    nombre_archivo = sys.argv[1]
    
    # Llamada a la función principal para procesar las transacciones bancarias del archivo CSV "procesar_tbancarias"
    procesar_tbancarias(nombre_archivo)