
from flask import render_template, request, app

from flask import Flask
from DataGraph import graph_stats
from FetchScale import FetchData

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home_page():
    cards = []  # Initialize the cards list
    if request.method == "POST":
        hero_name = request.form.get("hero_name")  # Get the hero name from the form

        # Create an instance of FetchData
        fetch_data = FetchData("SuperVs", "Alias", hero_name)

        # Fetch data for the hero's attributes
        hero_data = fetch_data.src_data()  # Fetch general data (e.g., name, race)
        stats_data = fetch_data.src_attrib()  # Fetch attribute data like intelligence, strength, etc.

        if hero_data:
            hero_alias, hero_race = hero_data[0]  # Assuming hero_data returns a list of tuples
            # Build the card data for the template
            cards.append({
                'title': hero_alias,  # Hero name
                'text': f'Race: {hero_race}',  # Add descriptive text as needed
                'attributes': stats_data  # Pass attributes for the card
            })

            # Optionally, you could add logic here to fetch and append additional cards

        # Generate the chart
        chart_path = graph_stats("SuperVs", hero_name)
        return render_template("home.html", chart_url=chart_path, cards=cards)

    # For GET requests, just render the template without cards
    return render_template("home.html", cards=cards)

