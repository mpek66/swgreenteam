from flask import Flask, redirect, url_for, render_template, jsonify, request
import os

app = Flask(__name__, static_url_path="/static")

@app.route("/", methods=["GET"])
def blank():
    return redirect("/whoops/")

@app.route("/<string:location>/", methods=["GET"])
def main(location):
    pages = ["home", "upcoming_events", "current_members", "contact_us"]
    if location not in pages:
        location = "whoops"
    cocntents = ""
    realpath = os.path.dirname(os.path.realpath(__file__))+"/templates/"
    with open(realpath+location+".html", "r") as fin:
        contents = fin.read()
    pretty = {
        "home": "Home",
        "upcoming_events": "Upcoming Events",
        "current_members": "Current Members",
        "contact_us": "Contact Us",
        "whoops": "Whoops"
    }
    return render_template("index.html", url=location, page=pretty[location], html=contents)

@app.route("/load_page/", methods=["GET"])
def load_page():
    print("here")
    return jsonify(url=request.args["goal"], page=request.args["goal"], html="<p>WORKED</p>")

if __name__ == "__main__":
    app.run(debug=True, threaded=True)
