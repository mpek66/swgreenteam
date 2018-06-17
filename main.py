from flask import Flask, redirect, url_for, render_template, jsonify, request

app = Flask(__name__, static_url_path="/static")



if __name__ == "__main__":
    app.run(debug=True, threaded=True)
