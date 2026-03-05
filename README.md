# 🔧 Predictive Maintenance System

A **Machine Learning powered web application** that predicts potential industrial machine failures using real-time sensor inputs.

The system uses historical **IoT sensor data** to train a **Logistic Regression model** that classifies machine condition into:

- **0 → Normal Operation (No Failure Expected)**
- **1 → Failure Likely (Maintenance Required)**

The trained model is deployed through a **Flask web interface** where users can input sensor readings and receive instant predictive insights.

---

# 🎯 Project Purpose

This project was developed as a **college academic project** to demonstrate how **Machine Learning can be applied to industrial predictive maintenance.**

### Objectives

- Analyse **IoT-based industrial equipment data**
- Predict machine failures using **sensor parameters**
- Provide a **real-time web interface for predictions**
- Reduce **downtime and improve maintenance planning**

---

# ⚙️ Features

- Machine failure prediction using **Machine Learning**
- **Real-time sensor input** through a web UI
- **Probability-based risk output**
- **Logistic Regression classification**
- **Data preprocessing pipeline**
- Simple **Flask deployment**

---

# 🧠 System Workflow

## 1️⃣ Data Acquisition

Sensor data collected from industrial equipment includes:

- Air Temperature  
- Process Temperature  
- Rotational Speed  
- Torque  
- Tool Wear  
- Machine Type (L / M / H)

For this project, the **AI4I Dataset** is used to simulate real-world IoT sensor readings.

---

## 2️⃣ Data Preprocessing

Before feeding the data into the model:

- Missing values are handled  
- Machine type is **encoded**  
- Numerical features are **scaled using StandardScaler**  
- Dataset is split into **training and testing sets**

---

## 3️⃣ Model Training

A **Logistic Regression model** is trained to learn the relationship between sensor values and machine failure.

The model determines how each parameter contributes to **failure probability**.

---

## 4️⃣ Deployment

The trained model is saved as:

```
model.pkl
```

A **Flask web application** loads this model and allows users to input real-time machine data.

---

## 5️⃣ Prediction Output

The system predicts machine condition with a probability score.

Example outputs:

```
✅ No Failure Expected (Risk: 2.6%)
⚠️ Failure Expected (Risk: 86.4%)
```

---

# 🏗️ Project Structure

```
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
```

---

# 🛠️ Tech Stack

### Frontend
- HTML  
- CSS  

### Backend
- Flask (Python)

### Machine Learning
- Scikit-learn  
- Logistic Regression  

### Data Processing
- Pandas  
- NumPy  

---

# 🚀 How to Run Locally

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/Maniac1309/Predictive_Maintenance.git
cd Predictive_Maintenance
```

---

## 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 3️⃣ Train the Model (Optional)

If you want to retrain the model:

```bash
python train_model.py
```

---

## 4️⃣ Run the Flask Application

```bash
python app.py
```

---

## 5️⃣ Open in Browser

```
http://127.0.0.1:5000/
```

---

# 📊 Example Inputs

| Parameter | Example |
|----------|--------|
| Air Temperature | 600 K |
| Process Temperature | 610 K |
| Rotational Speed | 1800 rpm |
| Torque | 100 Nm |
| Tool Wear | 700 min |
| Machine Type | Type M |

---

# 🔮 Future Improvements

- Implement advanced ML models (**Random Forest, SVM, XGBoost**)  
- Integrate with **real IoT devices (MQTT / Node-RED)**  
- Add **anomaly detection (LSTM Autoencoders)**  
- Deploy **cloud dashboard (AWS / Azure)**  

---

# 📌 Repository

**GitHub Link:**  
👉 https://github.com/Maniac1309/Predictive_Maintenance
