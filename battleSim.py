import joblib
import random

class BattleSimulator:
    def __init__(self, model_path):
        # Load the trained ML model
        self.model = joblib.load(model_path)
        # Predefined opponent heroes
        self.heroes = [
            {"name": "Superman", "Intelligence": 90, "Strength": 100, "Speed": 95, "Durability": 100, "Power": 100, "Combat": 90},
            {"name": "Batman", "Intelligence": 100, "Strength": 50, "Speed": 60, "Durability": 70, "Power": 60, "Combat": 100},
            {"name": "Wonder Woman", "Intelligence": 85, "Strength": 90, "Speed": 80, "Durability": 95, "Power": 85, "Combat": 95},
            {"name": "Flash", "Intelligence": 75, "Strength": 40, "Speed": 100, "Durability": 70, "Power": 80, "Combat": 85},
            {"name": "Thor", "Intelligence": 80, "Strength": 95, "Speed": 85, "Durability": 95, "Power": 100, "Combat": 90},
        ]

    def select_random_opponent(self):
        """Randomly selects an opponent from the predefined heroes."""
        return random.choice(self.heroes)

    def predict_winner(self, user_hero, opponent):
        """Predicts the winner using the ML model."""
        # Prepare data for prediction
        user_features = [[
            user_hero["Intelligence"], user_hero["Strength"], user_hero["Speed"],
            user_hero["Durability"], user_hero["Power"], user_hero["Combat"]
        ]]
        opponent_features = [[
            opponent["Intelligence"], opponent["Strength"], opponent["Speed"],
            opponent["Durability"], opponent["Power"], opponent["Combat"]
        ]]

        # Predict probabilities for each hero
        user_prob = self.model.predict_proba(user_features)[0][1]  # Probability of user winning
        opponent_prob = self.model.predict_proba(opponent_features)[0][1]  # Probability of opponent winning

        # Determine the winner
        if user_prob > opponent_prob:
            return user_hero["name"], f"Win Probability: {user_prob:.2%}"
        elif opponent_prob > user_prob:
            return opponent["name"], f"Win Probability: {opponent_prob:.2%}"
        else:
            return "It's a tie!", "Equal probabilities"
