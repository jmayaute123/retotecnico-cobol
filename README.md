# retotecnico-cobol

Reto Técnico: Procesamiento de Transacciones Bancarias (CLI)

## Introducción

Este proyecto, que es un script desarrollado en python, desarrolla una aplicación que procesa un archivo CSV con transacciones bancarias y genera un reporte que muestra como resultado un balance final, transacciones de mayor monto y un conteo de transacciones. Lo he creado para poder participar del reto académico de Cobol Academy y resaltar mis habilidades en el rubro de la programación y la comunicación. Este script se puede utilizar tanto en el ámbito personal para ordenar finanzas, así como también, en el ámbito empresarial para generar un resumen sencillo, pero útil de las transacciones de la empresa. 

```bash
Reporte de Transacciones
---------------------------------------------
Balance Final: 325.00
Transacción de Mayor Monto: ID 3 - 200.00
Conteo de Transacciones: Crédito: 3 Débito: 2
```

## Instrucciones de Ejecución

Se deben tener presente las siguientes instrucciones para la correcta ejecución del programa:

- Pasos previos
  - Asegúrate de tener instalado Python 3.x en tu sistema.
  - Asegúrate de tener un editor como Visual Studio Code o similares instalado en tu sistema.

- Clona este repositorio
   ```bash
   git clone https://github.com/jmayaute123/retotecnico-cobol.git
   cd retotecnico-cobol

- Para ejecutar el programa, utiliza el siguiente comando en la terminal, previamente debes ubicarte en la ruta de los archivos clonados:
  ```bash
  py main.py muestra_correcta_1.csv
  
**Nota:** Se han proporcionado dos archivos de muestras correctas y 5 archivos de muestras incorrectas para poder validar las distintas funcionalidades del código. En caso se necesite probar con otro archivo .csv se debe asegurar de agregarlo a la carpeta del proyecto

## Enfoque y Solución

La lógica implementada se estructuró en tres etapas:
  
  -  **Presencia de archivo de entrada:** Nos aseguramos que el nombre del archivo sea un imput en la línea de comando de llamada al programa, siendo un ejemplo correcto el siguiente: py main.py muestra_correcta_1.csv
     
  -  **Validación de formato del archivo de entrada:** Nos aseguramos que el archivo cuenta con una extensión csv, que exista en la ruta del proyecto, que contenga los encabezados esperados y que contenga almenos una transacción para poder darle paso a la etapa de procesamiento de datos
    
  -  **Procesamiento de datos y entrega de resultados:** Mediante un bucle que recorre fila a fila el documento, realizamos el cálculo de los valores finales de las variables: balance, contador y transacción mayor; para finalmente mostrarlos acorde al requerimiento del reto. Cabe resaltar que en esta etapa también se evalúan posibles errores al utilzar valores que no cumplen con los formatos específicos ya que trabajaremos con strings y decimales.
 
Esta lógica de diseño de tres etapas y el uso de excepts se tomó en cuenta para poder estructurar el código de una manera amigable para el usuario y para poder asegurar que el programa pueda identificar posibles errores en su uso al no definir un archivo csv correcto.

## Estructura del Proyecto

El proyecto, que cuenta con una única carpeta para todos los archivos, se estructura de la siguiente manera:

- **README:** Contiene todo el detalle de la estructura del proyecto
- **main.py:** Es el único archivo python en el que se ha definido todo el código estructurado en tres etapas
- **muestras:** Se han agregado a la carpeta un total de siete muestras, siendo la "muestra_correcta_1.csv" la solicitada en el csv. El objetivo de tener siete, es poder validar todas las buenas prácticas utilizadas en este código 



