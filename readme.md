## U4: Práctica 4: Formularios Flask

### Creación de páginas HTML
Las páginas creadas en prácticas anteriores de esta materia serán usadas para comprender cómo crear direcciones que apunten a estas páginas y cómo cargarlas a una aplicación de Flask.

El método de Python `render_template()` toma como parámetro una cadena que representa la dirección de un archivo `html` para cargarlo.

Para esta práctica se genera un formato que incluye varias carpetas, donde la carpeta `templates/public` se encuentran los archivos HTML.

### Creación de Rutas

Dentro del código de la aplicación Flask debemos definir rutas con el método `@app.route()`.
En este caso se definirán cuatro rutas, una para la página principal, tres para páginas personalizadas accesibles a través de la principal.

    @app.route("/")
    def inicio():
        return render_template("public/index.html")

    @app.route("/primero")
    def primero():
        return render_template("public/pagina1.html")

    @app.route("/segundo")
    def segundo():
        return render_template("public/pagina2.html")

    @app.route("/tercero")
    def tercero():
        return render_template("public/pagina3.html")

Como se puede observar, las funciones definidas devuelven el resultado de cargar una página HTML, como se explicó en el punto anterior.

### Vincular enlaces de las páginas con rutas
Se presenta el problema de que no se puede entrar a esta ruta a través de la página principal, dado que los enlaces dentro del `HTML` hacen referencia a un archivo, y el enlace que abren hace referencia a este archivo y no coincide con las rutas definidas en el archivo `Python`.

    <a href="pagina1.html"> Enlace1 </a>
    <a href="pagina2.html"> Enlace2 </a>
    <a href="pagina3.html"> Enlace3 </a>

Para solucionar esto, se puede usar un método que active la función que necesitamos para cada caso. Este método es `url_for()`. Toma como parámetro el nombre de una función en el archivo `app.py` y genera la ruta necesaria para acceder a ella. Al rodear este método con `{{ }}` se puede ejecutar dentro de la propiedad de HTML.

Por tanto, las etiquetas quedarían como:

    <a href="{{ url_for('primero') }}"> Enlace1 </a>
    <a href="{{ url_for('segundo') }}"> Enlace2 </a>
    <a href="{{ url_for('tercero') }}"> Enlace3 </a>