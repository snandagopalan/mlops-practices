from flask import Flask, request, jsonify
import pickle

app = Flask(__name__)

# Load the model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    prediction = sum(model["weights"]) * data["input"]
    return jsonify({"prediction": prediction})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
