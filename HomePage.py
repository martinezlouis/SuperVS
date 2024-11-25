from flask import Flask
from flask import render_template, request

from DataGraph import graph_stats
from FetchScale import FetchData

app = Flask(__name__)
app.jinja_env.globals.update(zip=zip)


@app.route("/", methods=["GET", "POST"])
def home_page():
	cards = []  # Initialize the cards list
	chart_paths = []  # Store paths for generated charts

	if request.method == "POST":
		hero1_name = request.form.get("hero1_name")
		hero2_name = request.form.get("hero2_name")

		for hero_name in [hero1_name, hero2_name]:
			# Create an instance of FetchData
			fetch_data = FetchData("SuperVs", "Alias", hero_name)

			# Fetch data for the hero's attributes
			hero_data = fetch_data.src_data()
			stats_data = fetch_data.src_attrib()

			if hero_data:
				# Extract hero details based on your database schema
				hero_alias = hero_data[0][1]  # Assuming Alias is the second column
				hero_race = hero_data[0][8]  # Assuming Race is the ninth column

				# Build the card data for the template
				cards.append({
					'title': hero_alias,
					'text': f'Race: {hero_race}',
					'attributes': stats_data
				})

				# Generate a chart for each hero
				chart_paths.append(graph_stats("SuperVs", hero_name))

	# Pass chart_urls as a list of paths
	return render_template("home.html", chart_urls=chart_paths, cards=cards)
