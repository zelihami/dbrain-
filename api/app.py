from flask import Flask, jsonify
import json
app = Flask(__name__)

# Kaydedilen verileri okuyacak fonksiyon
def read_data_from_file(file_path):
    data = []
    with open(file_path, 'r') as file:
        for line in file:
            data.append(json.loads(line.strip()))
    return data

@app.route('/data', methods=['GET'])
def get_data():
    data = read_data_from_file('kafka_data.txt')
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
