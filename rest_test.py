from flask import Flask, request
import json
app = Flask(__name__)

@app.route("/mivtzaim")
def mivtzaim():
    miv = {'milk':3.5, 'bread':6}
    return json.dumps(miv)

prices = {111:3.5, 222:4.6}
@app.route("/price/<int:barcode>")
def price(barcode):
    return prices[barcode]

@app.route("/price/<int:barcode>", methods=["POST"])
def price_post(barcode):
    prices[barcode] = request.form['price']
    return prices[barcode]

if __name__ == "__main__":
    app.run()