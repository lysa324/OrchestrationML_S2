from flask import Flask, request, jsonify
import torch
from PIL import Image
from ultralytics import YOLO
import json

app = Flask(__name__)

model_path = r'best.pt'
model = YOLO(model_path)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        if 'file' not in request.files:
            return jsonify(error="Aucun fichier d'image trouvé dans la demande POST")

        image_file = request.files['file']

        # Vérifier si le fichier a une extension d'image valide
        if not image_file.filename.endswith(('.jpg', '.jpeg', '.png', '.gif')):
            return jsonify(error="Le fichier n'est pas une image valide")

        # Charger  l'image depuis le fichier
        image = Image.open(image_file)

        with torch.no_grad():
            output = model(image)

        response = {
            'names': output[0].names,
        }
        json_response = json.dumps(response, indent=4)

        return jsonify(json_response)

    except Exception as e:
        return jsonify(error=str(e))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
