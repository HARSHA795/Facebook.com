from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

locations = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/location', methods=['POST'])
def location():
    data = request.get_json()
    locations.append(data)
    return jsonify({"status": "saved"})

@app.route('/view')
def view():
    return jsonify(locations)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
