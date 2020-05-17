import os
from flask import Flask
from flask import render_template
import requests

app = Flask(__name__)


@app.route("/", methods = ['GET'])
def call_url():

    URL = os.environ.get("PYCON_EXAMPLE_URL")
    r = requests.get(url = URL)
    data = r.json()

    return render_template("result.html", **locals())


if __name__ == "__main__":
    app.run()
