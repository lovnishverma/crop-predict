from flask import Flask, render_template, request, jsonify
import joblib
import numpy as np
import os

app = Flask(__name__)

# Load model at startup
MODEL_PATH = 'crop_recommendation_model.joblib'

model = None
if os.path.exists(MODEL_PATH):
    model = joblib.load(MODEL_PATH)

FEATURE_INFO = {
    'N':  {'label': 'Nitrogen (N)',       'unit': 'kg/ha', 'min': 0,    'max': 300,  'step': 1,    'placeholder': 'e.g. 175'},
    'P':  {'label': 'Phosphorus (P)',     'unit': 'kg/ha', 'min': 0,    'max': 150,  'step': 1,    'placeholder': 'e.g. 36'},
    'K':  {'label': 'Potassium (K)',      'unit': 'kg/ha', 'min': 0,    'max': 300,  'step': 1,    'placeholder': 'e.g. 216'},
    'ph': {'label': 'pH Level',           'unit': '',      'min': 0,    'max': 14,   'step': 0.01, 'placeholder': 'e.g. 5.9'},
    'EC': {'label': 'Electrical Cond.',   'unit': 'dS/m',  'min': 0,    'max': 5,    'step': 0.01, 'placeholder': 'e.g. 0.15'},
    'S':  {'label': 'Sulfur (S)',         'unit': 'mg/kg', 'min': 0,    'max': 50,   'step': 0.01, 'placeholder': 'e.g. 0.28'},
    'Cu': {'label': 'Copper (Cu)',        'unit': 'mg/kg', 'min': 0,    'max': 50,   'step': 0.01, 'placeholder': 'e.g. 15.69'},
    'Fe': {'label': 'Iron (Fe)',          'unit': 'mg/kg', 'min': 0,    'max': 300,  'step': 0.01, 'placeholder': 'e.g. 114.20'},
    'Mn': {'label': 'Manganese (Mn)',     'unit': 'mg/kg', 'min': 0,    'max': 200,  'step': 0.01, 'placeholder': 'e.g. 56.87'},
    'Zn': {'label': 'Zinc (Zn)',          'unit': 'mg/kg', 'min': 0,    'max': 100,  'step': 0.01, 'placeholder': 'e.g. 31.28'},
    'B':  {'label': 'Boron (B)',          'unit': 'mg/kg', 'min': 0,    'max': 100,  'step': 0.01, 'placeholder': 'e.g. 28.62'},
}

FEATURES = ['N', 'P', 'K', 'ph', 'EC', 'S', 'Cu', 'Fe', 'Mn', 'Zn', 'B']

@app.route('/')
def index():
    return render_template('index.html', features=FEATURES, feature_info=FEATURE_INFO)

@app.route('/predict', methods=['POST'])
def predict():
    if model is None:
        return jsonify({'error': 'Model not loaded. Please ensure crop_recommendation_model.joblib exists.'}), 500

    try:
        values = [float(request.form.get(f, 0)) for f in FEATURES]
        prediction = model.predict([values])
        crop = prediction[0]

        # Get probabilities if available
        proba = None
        if hasattr(model, 'predict_proba'):
            proba_arr = model.predict_proba([values])[0]
            classes = model.classes_
            top3_idx = proba_arr.argsort()[-3:][::-1]
            proba = [{'crop': str(classes[i]), 'prob': round(float(proba_arr[i]) * 100, 1)} for i in top3_idx]

        return jsonify({'crop': str(crop), 'top3': proba})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)