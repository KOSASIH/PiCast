import tensorflow as tf
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Load network traffic data
traffic_data = pd.read_csv('traffic_data.csv')

# Preprocess data
X = traffic_data.drop(['label'], axis=1)
y = traffic_data['label']

# Train AI model
model = RandomForestClassifier(n_estimators=100)
model.fit(X, y)

# Evaluate model performance
y_pred = model.predict(X)
accuracy = accuracy_score(y, y_pred)
print(f'Model accuracy: {accuracy:.3f}')
