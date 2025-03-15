import os
from flask import Flask, send_file, send_from_directory
from symbol_codec import encode, decode, symbol_to_binary

app = Flask(__name__)

# Route to serve the dice.html file
@app.route('/')
def serve_html():
    return send_file('dice.html')  # Ensure dice.html exists in the same directory as app.py

# Route to serve dice symbol images
@app.route('/symbols/<filename>')
def serve_symbol(filename):
    # Use absolute path to ensure Flask finds the correct directory
    symbols_path = os.path.abspath('symbols')
    return send_from_directory(symbols_path, filename)

# Encoding route
@app.route('/encode/<string:data>', endpoint="encode_data_route")
def encode_data_route(data):
    return encode(data, symbol_to_binary)

# Decoding route
@app.route('/decode/<string:binary_string>', endpoint="decode_data_route")
def decode_data_route(binary_string):
    return decode(binary_string, symbol_to_binary)

# Main entry point to run the Flask app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
