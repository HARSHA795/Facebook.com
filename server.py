from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/location', methods=['POST'])
def location():
    data = request.get_json()
    print("Location received:", data)
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    app.run(debug=True)
