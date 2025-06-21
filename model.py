from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import pickle

# Load data
X, y = load_iris(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Train model
model = DecisionTreeClassifier()
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# ✅ Log accuracy
accuracy = accuracy_score(y_test, y_pred)
print("✅ Training complete!")
print(f"🎯 Accuracy: {accuracy}")

# ✅ Save model
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)
