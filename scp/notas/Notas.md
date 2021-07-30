# Notas sobre Scpraping y Xpath

## Expreciones



- `/` hace referencia a la raíz, o tambien significa un salto entre nodos. *e.g `/html/body`Muestra todo lo que hay dentro del body de html*
- `//` Sirve para acceder a todos los nodos con la etiqueta seleccionada. *e.g* `[*//span](//span)` muestra todas las etiquetas span*
- `..` Sirve para acceder a los nodos padre de la etiqueta *tag. e.g `//span/..` accede a todos los nodos padre de span*
- `.` Hace referencia al nodo actual. *e.g. `//span/.` es equivalent a `//span`*
- `@` Sirve para traer los atributos. *e.g `//div/@class` Nos da las clases de todos los divs*

## Predicados

Sirven para encontrar información especificas.

- n : Hace referencia al n elemento de la lista.
- last(): Al último elemento de la lista.
- @atribute_name : Al usarse como predicado me trae todos los nodos
  que contienen este atributo
- @atribute_name="" : Al usarse como predicado me trae todos los nodos
  que contienen este atributo, incluso el value de este atributo.

