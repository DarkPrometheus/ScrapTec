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

## Operadores

- !=
- position()
- and
- or
- not()

## Wildcards

- /* : Con asterisco le estoy diciendo que me traiga todos los nodos inmediatamente después de la expresión.
- //* : En este caso le estoy diciendo que estoy saltando en todos los niveles en todas las direcciones.
- @*: Traer todos los atributos de todos los nodos
- /node() : Nos trae además de nodos el contenido, difiere de asterisco.

## Funciones

Para buscar cadenas de caracteres especificas dentro de un texto.

- start-with( **.**, “Texto a buscar”): Empezar con, el punto hace referencia al nodo actual
- end-with(.,""): Termina en.
- contains (**.**, “Texto a buscar”) : Sirve para llamar por el texto contenido en.
- matches(**.**,""): Sirve para hacer una búsqueda en el texto de un nodo que coincida con una expresión regular.

## Axes

**Azucar sintáctica:** se refiere a los añadidos a la sintaxis de un lenguaje de programación diseñados para hacer algunas construcciones más fáciles de leer o expresar.
`self::div` -> se abrevia con . y se refiere al mismo nodo o div en este caso
`child::div` -> Trae los hijos del div
`descendant::div` -> Trae todos los nodos que están en niveles inferiores
`descendant-or-self::div` -> Trae la unión entre los descendientes y el mismo nodo div