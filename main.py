import sys
import csv

def procesar_transacciones(nombre_archivo):
    try:
        balance_final = 0
        transaccion_mayor_monto = {'id': None, 'monto': 0}
        conteo_credito = 0
        conteo_debito = 0

        # Intentamos abrir el archivo CSV
        with open(nombre_archivo, mode='r') as archivo:
            lector_csv = csv.DictReader(archivo, delimiter=';')

            for fila in lector_csv:
                tipo = fila['tipo']
                monto = float(fila['monto'])
                if tipo == 'Crédito':
                    balance_final += monto
                    conteo_credito += 1
                elif tipo == 'Débito':
                    balance_final -= monto
                    conteo_debito += 1

                # Identificamos la transacción con el mayor monto
                if monto > transaccion_mayor_monto['monto']:
                    transaccion_mayor_monto['id'] = fila['id']
                    transaccion_mayor_monto['monto'] = monto

        # Mostramos el reporte
        print("Reporte de Transacciones")
        print("---------------------------------------------")
        print(f"Balance Final: {balance_final:.2f}")
        print(f"Transacción de Mayor Monto: ID {transaccion_mayor_monto['id']} - {transaccion_mayor_monto['monto']:.2f}")
        print(f"Conteo de Transacciones: Crédito: {conteo_credito} Débito: {conteo_debito}")

    except FileNotFoundError:
        print(f"Error: El archivo '{nombre_archivo}' no fue encontrado.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

# Verificar que se haya pasado el nombre del archivo como argumento
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso incorrecto del script.")
        print("Por favor, proporciona el nombre del archivo CSV como argumento.")
        print("Ejemplo: python script.py transacciones.csv")
        sys.exit(1)

    # Obtener el nombre del archivo desde los argumentos
    nombre_archivo = sys.argv[1]
    
    # Llamada a la función para procesar el archivo CSV
    procesar_transacciones(nombre_archivo)