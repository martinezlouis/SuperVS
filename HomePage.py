from flask import Flask
from flask import render_template, request

from DataGraph import graph_stats
from FetchScale import FetchData
from battleSim import BattleSimulator

app = Flask(__name__)
app.jinja_env.globals.update(zip=zip)


@app.route("/", methods=["GET", "POST"])
def home_page():
    cards = []
    chart_paths = []

    if request.method == "POST":
        hero1_name = request.form.get("hero1_name")
        hero2_name = request.form.get("hero2_name")

        for hero_name in [hero1_name, hero2_name]:

            fetch_data = FetchData("SuperVs", "Alias", hero_name)


            hero_data = fetch_data.src_data()
            stats_data = fetch_data.src_attrib()
            img_url = fetch_data.load_img()

            if hero_data:
                # Extract hero details based on your database schema
                hero_alias = hero_data[0][1]
                hero_race = hero_data[0][8]

                # Build the card data for the template
                cards.append({
                    'title': hero_alias,
                    'text': f'Race: {hero_race}',
                    'attributes': stats_data,
                    "image": img_url
                })

                # Generate a chart for each hero
                chart_paths.append(graph_stats("SuperVs", hero_name))

    # Pass chart_urls as a list of paths
    return render_template("index.html", chart_urls=chart_paths, cards=cards)


battle_sim = BattleSimulator("models/superhero_model.pkl")

@app.route("/fight", methods=["GET", "POST"])
def battle_simulator():
    if request.method == "POST":
        race_attri = {
            "Human": 291,
            "Kryptonian": 544,
            "Demon": 334,
            "Cyborg": 356,
            "Mutant": 334
        }

        # Get user input
        race = request.form["race"]
        attributes = {
            "Intelligence": int(request.form["intelligence"]),
            "Strength": int(request.form["strength"]),
            "Speed": int(request.form["speed"]),
            "Durability": int(request.form["durability"]),
            "Power": int(request.form["power"]),
            "Combat": int(request.form["combat"]),
        }
        """
     
        Calculate the total attributes
        total_attributes = sum(race_attri.values())
        print(f"Total: {total_attributes}")
        print(f"Sum: {sum(attributes.values())}")
        print(f"Race: {race_attri}")
        """
        total_attributes = sum(race_attri.values())


        if total_attributes > race_attri.get(race, 0):
            error_message = (
                f"The total attributes for a {race} cannot exceed {race_attri[race]}. "
            )
            return render_template("Fight.html", error_message=error_message, user_hero=None)


        user_hero = {"name": request.form["name"], "race": race, **attributes}


        opponent = battle_sim.select_random_opponent()


        winner, probability = battle_sim.predict_winner(user_hero, opponent)

        return render_template(
            "Fight.html",
            user_hero=user_hero,
            opponent=opponent,
            winner=winner,
            probability=probability,
            error_message=None
        )

    return render_template("Fight.html", user_hero=None, error_message=None)
