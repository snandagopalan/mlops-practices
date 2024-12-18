import pickle

# Dummy model training
model = {"weights": [0.1, 0.2, 0.3]}
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model trained and saved as model.pkl")
