from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import pickle

# Load sample dataset
data = load_iris()
X = data.data
y = data.target

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Train model
model = DecisionTreeClassifier()
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Print accuracy (This will show in GitHub logs)
accuracy = accuracy_score(y_test, y_pred)
print("✅ Training complete!")
print("🎯 Accuracy:", accuracy)

# Save model to file (for later use or download)
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)
