from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/combine', methods=['POST'])
def combine():
    data = request.get_json()
    element1 = data['element1']
    element2 = data['element2']
    # Logika generowania wyniku
    if element1 == 'Fire' and element2 == 'Water':
        result = 'Steam'
    else:
        result = element1 + ' + ' + element2
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run()
