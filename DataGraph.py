import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np


from FetchScale import FetchData

def graph_stats(table_name, alias):

	"""
	theta:::

	Generates N angles evenly spaced between 0 and 2π (full circle).
	Represents the angular positions of the bars in the polar chart.
	Example: If N=4, theta could be [0, π/2, π, 3π/2].

	radii:::

	Generates N random values scaled by 10.
	Represents the height (length) of each bar.

	width:
 	Generates N random values scaled by π / 4
	Represents the angular width of each bar.

	colors:::

	Uses the viridis colormap to assign colors based on radii.
	Each bar's color intensity corresponds to its height (radii / 10 normalizes the values).theta:

	Generates N angles evenly spaced between 0 and 2π (full circle).
	Represents the angular positions of the bars in the polar chart.
	Example: If N=4, theta could be [0, π/2, π, 3π/2].

	radii:
	Generates N random values scaled by 10.
	Represents the height (length) of each bar.

	width:

	Generates N random values scaled by π/4.
	Represents the angular width of each bar.

	colors:
	Uses the viridis colormap to assign colors based on radii.
	Each bar's color intensity corresponds to its height (radii / 10 normalizes the values).
	"""
	stats = FetchData(table_name, "Alias", alias )


	attributes = ["Intelligence", "Strength", "Speed",
					  "Durability", "Powered", "Combat"]
	N = len(attributes)

	#angle for bars
	theta = np.linspace(0.0, 2 * np.pi, N, endpoint=False)

	#fetch data
	stats_data = stats.src_attrib()
	radii = [sum(values) for attr, values in stats_data]
	print(stats_data)

	width = [np.pi / 6] * N

	if max(radii) == 0:
		colors = plt.cm.viridis(np.zeros(N))  # Fallback to a neutral color if max(radii) is zero
	else:
		colors = plt.cm.viridis(np.array(radii) / max(radii))

	ax = plt.subplot(projection='polar')
	ax.bar(theta, radii, width=width, bottom=0.0, color=colors, alpha=0.7)

	ax.set_xticks(theta)
	ax.set_xticklabels(attributes)


	#colors
	#The calculation for the colors is based on normalizing the radii array with max(radii).
	#If radii contains only zero values, max(radii) will be zero, and dividing by zero will cause issues,

		# save the chart as an image
	img_path = f"static/{alias}_chart.png"
	plt.savefig(img_path)

	plt.close()
	return img_path




