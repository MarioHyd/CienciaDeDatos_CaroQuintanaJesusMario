Proyecto realizado por: Jesus Mario Caro Quintana.

Paso 1: lo primero que hice fue analizar el archivo txt, manualmente quite los encabezados ya que no aportaban nada para el dataframe, además quite el nombre de cada columna ya que tenia unos caracteres especiales ya que podría generar problemas.

Paso 2: ya que quedo solamente la tabla con los datos relevantes, hice un algoritmo utilizando la librería de pandas para transformar el archivo txt a un archivo csv asignando un nombre a cada columna que eran los mismos nombres que elimine en el paso anterior.

Paso 3: una vez tenia ya el archivo csv listo lo cargue utilizando la librería de pandas.

Paso 4: inicio la limpieza de datos, asignando el tipo de dato que le corresponde a cada columna.

Paso 5: Empiezo con el análisis de los datos, primero verifico cuantos nulos hay en cada una de las columnas del dataframe.

Paso 6: Después cuento cuantos nulos hay por fecha.

Paso 7: Siguiente a eso, saco la media de cada una de las columnas y a todos los valores nulos de cada una de las columnas las sustituyo por la media de la columna correspondiente.

Paso 8: vuelvo a ver cuantos nulos hay en cada una de las columnas para verificar que el paso anterior se hizo correctamente.