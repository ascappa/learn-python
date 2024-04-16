from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/<my_route>")
def hello_world(my_route="casuccia"):
  return render_template("index.html", my_route=my_route, name="hello", testo_random="wrewwe we r")

@app.route("/jordan")
def show_jordan():
  return 