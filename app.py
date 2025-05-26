from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/calculate", methods=["POST"])
def calculate():
    # Get user input from the form
    distance = float(request.form["distance"])
    emission = distance * 0.21  # Example calculation: 0.21 kg CO2 per km
    return render_template("result.html", emission=emission)

if __name__ == "_main_":  # Corrected line
    app.run(debug=True)