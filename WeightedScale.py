import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib
from sklearn.preprocessing import StandardScaler

from FetchScale import FetchData


class WeightedPower():
	def weighted_combat(self, table_name, alias):
		prowess = {"Intelligence": .25, "Strength": .10, "Speed": .10,
				   "Durability": .15, "Powered": .25, "Combat": .15}

		attrib = FetchData(table_name, "Alias", alias)
		attrib.src_data()
		arr_attrib = attrib.src_attrib()

		if arr_attrib is None:
			print("Attributes not fetched properly")
			return None

		"""
		takes the values of prowess in the first loop
		from the FetchData class function src_attributes takes the tuple format like prowess
		if both names match then it continues
		the sum type cast allows the value to be converted from [20] to 20
		"""
		weighted_prowess = 0
		for attribute, weight in prowess.items():
			for attr, values in arr_attrib:
				if attr == attribute:
					weighted_prowess += sum(values) * weight

		print(f"Weighted Combat Score: {weighted_prowess}")
		return weighted_prowess

	def versus(self):
		hero1 = WeightedPower()
		hero2 = WeightedPower()


	def stat_prediction(self):
		df = pd.read_csv("models/training.csv")

		# Features and target
		X = df[["Intelligence", "Strength", "Speed", "Durability", "Power", "Combat"]]
		y = df["Winner"].map({"Win": 1, "Lose": 0})  # Map target to binary values

		# Train-test split
		X_train, X_test, y_train, y_test = train_test_split(
			X, y, test_size=0.2, random_state=42, stratify=y
		)

		# Scale features
		scaler = StandardScaler()
		X_train = scaler.fit_transform(X_train)
		X_test = scaler.transform(X_test)

		# Train the model
		model = RandomForestClassifier(random_state=42, class_weight="balanced")
		model.fit(X_train, y_train)

		# Evaluate
		y_pred = model.predict(X_test)
		accuracy = accuracy_score(y_test, y_pred)
		print("Model Accuracy:", accuracy)
		print("X shape:", X.shape)
		print("y length:", len(y))


hero = WeightedPower()
print(hero.stat_prediction())
