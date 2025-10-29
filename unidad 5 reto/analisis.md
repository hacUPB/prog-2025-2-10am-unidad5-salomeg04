# Organización del código
El programa está dividido en funciones según el tipo de archivo que se trabaja: .csv o .txt. Cada grupo tiene su propio menú, y al final hay un menú principal que permite elegir entre los dos. Esto me ayudó a mantener el código ordenado y fácil de entender.
Las funciones están separadas por tareas específicas, por ejemplo: una función para contar palabras, otra para hacer gráficos, otra para calcular estadísticas, etc. Así es más fácil modificar o revisar cada parte sin afectar las demás.

# Uso de condicionales, bucles y listas

## Condicionales (if, elif) se usan para:
- Elegir qué opción ejecutar en los menús.
- Verificar si hay datos numéricos antes de hacer cálculos.

## Bucles (for) se usan para:
- Recorrer cada fila del archivo CSV.
- Contar vocales en el texto.
- Mostrar las primeras 15 filas del archivo CSV.

## Listas se usan para:
- Guardar los valores numéricos de una columna (datos = []).
- Contar cuántas veces aparece cada vocal (cantidades = [texto.count(v) for v in vocales]).


# Métodos usados para manejar texto y datos separados por comas
- Para archivos .csv, se usó csv.DictReader() que permite acceder a los datos por nombre de columna. También se usó .get() para evitar errores si la columna no existe.
- Para manejar texto, se usaron métodos como:
- .split() para separar palabras.
- .replace() para cambiar una palabra por otra.
- .lower() para convertir todo el texto a minúsculas y contar vocales correctamente.
- .count() para saber cuántas veces aparece cada vocal.


