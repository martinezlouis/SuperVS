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
