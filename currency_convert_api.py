from flask import Flask, jsonify, request, make_response

from currency_convert import CurrencyConvert, ErrorHandler, FileUpdate

JSON_OF_ALL_CURRENCIES = """http://data.fixer.io/api/latest?access_key=d281dc374b673b7c0976a6feeb27c2ca&format=1"""
SHORTCUT_TO_SYMBOL = """https://gist.githubusercontent.com/Fluidbyte/2973986/raw/b0d1722b04b0a737aade2ce6e055263625a0b435/Common-Currency.json"""


app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True


@app.route('/currency_converter')
def get_store():
    amount = request.args.get('amount', None)
    input_currency = request.args.get('input_currency', None)
    output_currency = request.args.get('output_currency', None)
    if input_currency is None:
        return jsonify({"error": "input currency is NONE!"}), 400
    if amount is None:
        return jsonify({"error": "amount is NONE!"}), 400
    try:
        converter = CurrencyConvert(float(amount), input_currency, output_currency)
        json_text = converter.json_it()
        return jsonify(json_text), 200
    except ErrorHandler:
        return make_response(jsonify({"error": "Invalid Currency / amount"}), 400)


@app.errorhandler(404)
def error_handler(error):
    return make_response(jsonify({"error": "Page not found"}), 404)


@app.errorhandler(500)
def error_handler(error):
    return make_response(jsonify({"error": "Server Side Error Occurred"}), 400)


if __name__ == "__main__":
    try:
        FileUpdate("backup/symbols.json", SHORTCUT_TO_SYMBOL)
        FileUpdate("backup/currency.json", JSON_OF_ALL_CURRENCIES)
    except ErrorHandler:
        print('WE COULD NOT UPDATE THE DATA, THE CURRENCY CONVERTER CAN BE NOT ACCURED')
    app.run()
