# Poke Api

Un pequeño ejemplo en el cual se consume la API de pokemon desde su sitio oficial <a href="https://pokeapi.co" target="_blank" style="color: #ef5350;">https://pokeapi.co</a> y se presenta un breve resumen al estilo de la pokedex de un pokemon buscado.

Se pone en práctica el uso del modulo <a href="https://click.palletsprojects.com/en/8.1.x/" target="_blank" style="color: #c90;">click</a>, usado para crear aplicaciones de línea de comandos (CLI) con python.

## Ejecución

Para ejecutar este programa deben seguir los siguientes pasos

1. Descargar el código desde el repositorio en formato ZIP o clonar el
   repositorio usando el comando

<pre>
    <code>
        git clone https://github.com/omararch48/pyjemplos_pokeapi.git
    </code>
</pre>

2. Crear un ambiente virtual e instalar los modulos requests y click usando los siguientes comandos

<pre>
    <code>
        pip install requests
        pip install click
    </code>
</pre>

3. Ejecutar la aplicación usando el comando

<pre>
    <code>
        python main.py
    </code>
</pre>

También se pude ejecutar con las opciones --pokemon (-p) y --json (-j), la primera es usada para buscar el pokemon desde la linea de comandos y la segunda para mostrar el resultado en formato json

<pre>
    <code>
        python main.py --pokemon pikachu
        python main.py -p 8 -j
    </code>
</pre>
