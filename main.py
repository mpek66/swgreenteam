from flask import Flask, redirect, url_for, render_template, jsonify, request

app = Flask(__name__, static_url_path="/static")

@app.route("/", methods=["GET"])
def main():
    return render_template("main.html", url="home", page="home", html="hello")

@app.route("/load_page/", methods=["GET"])
def load_page():
    print("here")
    return jsonify(url=request.args["goal"], page=request.args["goal"], html="<p>WORKED</p>")

if __name__ == "__main__":
    app.run(debug=True, threaded=True)
