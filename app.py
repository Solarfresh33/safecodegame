from flask import Flask, render_template, request
import random

app = Flask(__name__)

# Le code secret : un nombre entre 0 et 9999
SECRET = random.randint(0, 9999)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/check", methods=["POST"])
def check():
    try:
        code = int(request.form.get("code", -1))
    except ValueError:
        return render_template("index.html", error="Entre un nombre entier.")

    if code == SECRET:
        return render_template("win.html")
    else:
        return render_template("index.html", error="Mauvais code, réessaie !")

if __name__ == "__main__":
    app.run(debug=True)
