from flask import Flask, jsonify, render_template, request

from euclidean.rhythm import EuclideanRhythm


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/calculate', methods=('POST',))
def calculate():
    gates = request.json.get('gates')
    if gates is None:
        return jsonify({'error': 'missing argument "gates" in request'}), 400
    rhythm = EuclideanRhythm.from_gates(gates)
    return jsonify({'result': rhythm.as_dict()}), 200
