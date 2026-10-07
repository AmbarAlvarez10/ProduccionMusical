# ProduccionMusical

¡Hola! Soy Ambar Alvarez y me apasiona la producción musical.

En los procesos de producción musical, radio o diseño sonoro, sumar la duración exacta de múltiples pistas suele ser una tarea repetitiva y propensa a errores matemáticos (debido a que el tiempo se rige por bases de 60).

El objetivo de este proyecto es ofrecer una herramienta minimalista y veloz que permita a los creadores ingresar tiempos de manera fluida en formato estándar (min:seg) y obtener el cálculo total de la playlist al instante, sin formularios tediosos ni configuraciones previas.


¿Cómo Funciona el Código?

El programa está construido utilizando funciones simples de Python y un enfoque directo:

Bucle Continuo (while True): Mantiene el programa pidiendo datos de forma interactiva hasta que el usuario decida detenerlo.

Condición de Salida (fin): Detecta cuando escribes la palabra clave para romper el ciclo de entrada de datos y pasar al cálculo final.

Procesamiento de Texto (split(":")): Toma la cadena de texto ingresada (ej. 3:30), la divide en dos partes usando los dos puntos como separador, y convierte los valores de texto a números enteros.

Normalización a Segundos: Multiplica los minutos por 60 y les suma los segundos para trabajar con una sola unidad numérica consistente ((minutos * 60) + segundos).

Conversión Final (// y %): Al terminar, transforma el acumulado total de segundos de regreso a un formato legible por humanos usando división entera para los minutos y el operador módulo para los segundos sobrantes.
