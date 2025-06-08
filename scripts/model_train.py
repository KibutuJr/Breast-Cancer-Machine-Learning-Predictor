# scripts/model_train.py

from utils import load_and_clean_raw, split_data
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
import joblib

# Load and clean raw data
df = load_and_clean_raw(raw_path='data/breast-cancer-wisconsin.data')

# Split into train/test
X_train, X_test, y_train, y_test = split_data(df)

# Train
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluate
print(classification_report(y_test, model.predict(X_test)))

# Save model
joblib.dump(model, 'models/random_forest_model.pkl')
print(" Model saved to models/random_forest_model.pkl")
