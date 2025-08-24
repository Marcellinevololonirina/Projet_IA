from flask import Flask, request, jsonify, render_template
from pyswip import Prolog
import os

app = Flask(__name__)
prolog = Prolog()

prolog_file = os.path.abspath("enquete.pl").replace("\\", "/")
print("Chargement de :", prolog_file)
prolog.consult(prolog_file)

@app.route("/")
def index():
    return render_template("index.html")  

@app.route("/verifier", methods=["POST"])
def verifier():
    data = request.json
    suspect = data["suspect"].lower()
    crime = data["crime"].lower()
    query = f"is_guilty({suspect}, {crime})"
    print("Requête Prolog:", query)
    
    result = list(prolog.query(query))
    return jsonify({"guilty": bool(result)})

if __name__ == "__main__":
    app.run(debug=True)
