from flask import Flask, request, render_template
app = Flask(__name__)
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