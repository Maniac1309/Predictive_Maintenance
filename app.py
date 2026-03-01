from flask import Flask, render_template, request
import numpy as np
import pickle

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Load model, scaler, encoder
    model, scaler, le = pickle.load(open('model.pkl', 'rb'))

    # Read user input
    values = [float(x) for x in request.form.values()]
    final_input = np.array(values).reshape(1, -1)

    # Scale input data
    scaled_input = scaler.transform(final_input)

    # Predict
    pred = model.predict(scaled_input)[0]
    prob = model.predict_proba(scaled_input)[0][1]

    if pred == 1:
        result = f"⚠️ Failure Expected (Risk: {prob*100:.1f}%)"
    else:
        result = f"✅ No Failure Expected (Risk: {prob*100:.1f}%)"

    return render_template('index.html', prediction_text=result)

if __name__ == '__main__':
    app.run(debug=True)
