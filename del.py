import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import joblib

# Load the dataset
df = pd.read_csv("models/training.csv")

# Handle missing values (if any)
df.fillna(0, inplace=True)  # Replace with a more suitable imputation strategy

# Prepare features and target
X = df[["Intelligence", "Strength", "Speed", "Durability", "Power", "Combat"]]
y = df["Winner"]

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test)

# Evaluate the model
print("Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))
print(confusion_matrix(y_test, y_pred))

# Save the trained model
joblib.dump(model, "models/superhero_model.pkl")


