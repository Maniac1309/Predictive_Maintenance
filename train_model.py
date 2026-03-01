import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import precision_score, recall_score, f1_score, classification_report

import pickle

df = pd.read_csv('dataset/ai4i2020.csv')

le = LabelEncoder()
df['Type'] = le.fit_transform(df['Type'])

X = df[['Air temperature [K]', 'Process temperature [K]', 'Rotational speed [rpm]',
        'Torque [Nm]', 'Tool wear [min]', 'Type']]
y = df['Machine failure']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

model = LogisticRegression(max_iter=1000, class_weight='balanced')
model.fit(X_train_scaled, y_train)

y_pred = model.predict(X_test_scaled)

acc = model.score(X_test_scaled, y_test)
print(f"✅ Model trained successfully! Accuracy: {acc*100:.2f}%")

# Save model, scaler, and label encoder
pickle.dump((model, scaler, le), open('model.pkl', 'wb'))
print("💾 Model saved as model.pkl")

precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)

print(f"🎯 Precision: {precision*100:.2f}%")
print(f"🔁 Recall: {recall*100:.2f}%")
print(f"📊 F1 Score: {f1*100:.2f}%")