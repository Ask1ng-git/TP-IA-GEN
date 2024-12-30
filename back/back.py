from flask import Flask, request, jsonify
import pickle
import pandas as pd

# Initialiser l'application Flask
app = Flask(__name__)

# Charger le modèle
MODEL_PATH = "pipeline.pkl"

try:
    with open(MODEL_PATH, "rb") as file:
        model = pickle.load(file)
    print("Modèle chargé avec succès.")
except Exception as e:
    print(f"Erreur lors du chargement du modèle : {e}")

# Route pour vérifier si le serveur est opérationnel
@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Backend opérationnel"}), 200

# Route pour effectuer une prédiction
@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Extraire les données JSON envoyées dans la requête
        input_data = request.json
        
        # Convertir les données en DataFrame
        df = pd.DataFrame([input_data])
        
        # Effectuer une prédiction
        prediction = model.predict(df)
        
        # Retourner la prédiction sous forme de JSON
        return jsonify({"prediction": float(prediction[0])}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Lancer le serveur Flask
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8000)
