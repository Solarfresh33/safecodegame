from flask import Flask, render_template, request
import random

app = Flask(__name__)

# Code à trouver (3 chiffres)
SECRET_A = random.randint(0, 9)
SECRET_B = random.randint(0, 9)
SECRET_C = random.randint(0, 9)

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/check", methods=["POST"])
def check():
    try:
        a = int(request.form.get("a", -1))
        b = int(request.form.get("b", -1))
        c = int(request.form.get("c", -1))
    except ValueError:
        return render_template("index.html", error="Format invalide.")

    if a == SECRET_A and b == SECRET_B and c == SECRET_C:
        return render_template("win.html")
    else:
        return render_template("index.html", error="Mauvaise combinaison, réessaie !")

if __name__ == "__main__":
    app.run(debug=True)
