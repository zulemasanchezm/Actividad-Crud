from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# ──────────────────────────────────────────
#  BASE DE DATOS FALSA  (lista en memoria)
#  Se reinicia cada vez que reinicias Flask
# ──────────────────────────────────────────
productos = [
    {"id": 1,  "nombre": "Cuaderno",     "cantidad": 50,
        "precio": 2.50, "marca": "Norma"},
    {"id": 2,  "nombre": "Lápiz HB",     "cantidad": 100,
        "precio": 0.30, "marca": "Mirado"},
    {"id": 3,  "nombre": "Borrador",     "cantidad": 80,
        "precio": 0.50, "marca": "Pelikan"},
    {"id": 4,  "nombre": "Bolígrafo",    "cantidad": 60,
        "precio": 0.80, "marca": "BIC"},
    {"id": 5,  "nombre": "Regla 30cm",   "cantidad": 40,
        "precio": 1.20, "marca": "Norma"},
    {"id": 6,  "nombre": "Compás",       "cantidad": 25,
        "precio": 3.50, "marca": "Staedtler"},
    {"id": 7,  "nombre": "Tijeras",      "cantidad": 30,
        "precio": 2.00, "marca": "Maped"},
    {"id": 8,  "nombre": "Colores x12",  "cantidad": 45,
        "precio": 4.50, "marca": "Crayola"},
    {"id": 9,  "nombre": "Marcadores",   "cantidad": 20,
        "precio": 5.00, "marca": "Pelikan"},
    {"id": 10, "nombre": "Cartuchera",   "cantidad": 15,
        "precio": 6.00, "marca": "Totto"},
]
siguiente_id = 11


# ── READ ──────────────────────────────────
@app.route("/")
def index():
    return render_template("index.html", productos=productos)


# ── CREATE ────────────────────────────────
@app.route("/agregar", methods=["POST"])
def agregar():
    global siguiente_id
    productos.append({
        "id":       siguiente_id,
        "nombre":   request.form["nombre"],
        "cantidad": int(request.form["cantidad"]),
        "precio":   float(request.form["precio"]),
        "marca":    request.form["marca"],
    })
    siguiente_id += 1
    return redirect(url_for("index"))


# ── UPDATE ────────────────────────────────
@app.route("/editar/<int:id>", methods=["POST"])
def editar(id):
    for p in productos:
        if p["id"] == id:
            p["nombre"] = request.form["nombre"]
            p["cantidad"] = int(request.form["cantidad"])
            p["precio"] = float(request.form["precio"])
            p["marca"] = request.form["marca"]
    return redirect(url_for("index"))


# ── DELETE ────────────────────────────────
@app.route("/eliminar/<int:id>")
def eliminar(id):
    productos[:] = [p for p in productos if p["id"] != id]
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
