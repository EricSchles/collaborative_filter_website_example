from flask import Flask,render_template

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def index():
    return render_template("index.html")

@app.route("/viz",methods=["GET","POST"])
def viz():
    return render_template("viz.html")

app.run(debug=True)
