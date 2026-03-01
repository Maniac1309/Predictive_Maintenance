🔧 Predictive Maintenance System

A machine learning powered web application that predicts potential industrial machine failures using real-time sensor inputs.

This system uses historical IoT sensor data to train a Logistic Regression model that classifies machine condition into:

0 → Normal Operation (No Failure Expected)

1 → Failure Likely (Maintenance Required)

The trained model is deployed through a Flask web interface where users can input live sensor readings and receive instant predictive insights.

🎯 Project Purpose

This project was developed as a college academic project to demonstrate how machine learning can be applied to industrial predictive maintenance.

It aims to:

Analyse IoT-based industrial equipment data

Predict machine failures using sensor parameters

Provide a real-time web interface for predictions

Reduce downtime and improve maintenance planning

⚙️ Features

Machine failure prediction using ML

Real-time sensor input through web UI

Probability-based risk output

Logistic Regression based classification

Data preprocessing pipeline

Clean and simple Flask deployment

🧠 System Workflow

The system works in the following stages:

1. Data Acquisition

Sensor data such as:

Air Temperature

Process Temperature

Rotational Speed

Torque

Tool Wear

Machine Type (L / M / H)

is collected from industrial equipment.

For this project, the AI4I Dataset is used to simulate real-world IoT sensor readings.

2. Data Preprocessing

Before feeding into the model:

Missing values are handled

Machine type is encoded

Numerical features are scaled using StandardScaler

Dataset is split into training & testing sets

3. Model Training

A Logistic Regression model is trained to learn the relationship between sensor values and machine failure.

The model determines how each parameter contributes to failure probability.

4. Deployment

The trained model is saved as:

model.pkl

A Flask web application loads this model and allows users to input real-time machine data.

5. Output

The system predicts machine condition with a probability score.

Example outputs:

✅ No Failure Expected (Risk: 2.6%)

⚠️ Failure Expected (Risk: 86.4%)

🏗️ Project Structure
Predictive_Maintenance/
│
├── dataset/
│   └── ai4i2020.csv
│
├── static/
│   └── css/
│       └── styles.css
│
├── templates/
│   └── index.html
│
├── app.py
├── train_model.py
├── model.pkl
├── requirements.txt
└── README.md
🛠️ Tech Stack

Frontend

HTML

CSS

Backend

Flask (Python)

Machine Learning

Scikit-learn

Logistic Regression

Data Processing

Pandas

NumPy

🚀 How to Run Locally
Step 1: Clone the Repository
git clone https://github.com/Maniac1309/Predictive_Maintenance.git
cd Predictive_Maintenance
Step 2: Install Dependencies
pip install -r requirements.txt
Step 3: Train Model (Optional)

If you want to retrain the model:

python train_model.py
Step 4: Run Flask App
python app.py
Step 5: Open in Browser
http://127.0.0.1:5000/
📊 Example Inputs
Parameter	Example
Air Temperature	600 K
Process Temperature	610 K
Rotational Speed	1800 rpm
Torque	100 Nm
Tool Wear	700 min
Machine Type	Type M
🔮 Future Improvements

Implement advanced ML models (Random Forest, SVM, XGBoost)

Integrate with real IoT devices (MQTT / Node-RED)

Add anomaly detection (LSTM Autoencoders)

Deploy cloud dashboard (AWS / Azure)

📌 Repository

GitHub Link:
👉 https://github.com/Maniac1309/Predictive_Maintenance
