#!/usr/bin/python3
""" """

import process
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/bitcoin', strict_slashes=False)
def bitcoin():
    """ """
    price = process.btc.price
    name = process.btc.name
    suggest = process.btc.suggest
    render_template('bitcoin.html', price=price, name=name, suggest=suggest)

if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0')
