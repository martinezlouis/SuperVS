import pyodbc

db_file = r"C:\Users\louis\OneDrive - Year Up- BOS\YearUp\Mod 2\Capstone\Super\SuperVS.accdb"
connection = (r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
			  f'DBQ={db_file};')

conn = pyodbc.connect(connection)
cursor = conn.cursor()


class FetchData:
	def __init__(self, table_name, column_name, search_value):
		self.table_name = table_name
		self.column_name = column_name
		self.search_value = search_value

	"""
	    Searches for rows in the given table where column_name 
	    matches search_value.

		table_name: Name of the table to search
	  	column_name: Name of the column to filter
	  	search_value: Value to search for (supports wildcards for LIKE queries)
	    List of rows matching the criteria
	   """

	def src_data(self):
		try:
			query = (f"SELECT * FROM {self.table_name} WHERE "
					 f"{self.column_name} LIKE ?")
			cursor.execute(query, (f'{self.search_value}',))

			rows = cursor.fetchall()
			return rows

			"""
			if rows:
				print(f"Found {len(rows)} matching rows:")
				for row in rows:
					print(row)
			else:
				print("No matching rows found")
			"""

		except Exception as e:
			print("An error occurred: ", e)
			return None

	def src_attrib(self):
		attributes = ["Intelligence", "Strength", "Speed",
					  "Durability", "Powered", "Combat"]

		all_attrib = []
		try:
			for attribute in attributes:
				query = (f"SELECT {attribute} FROM {self.table_name} "
						 f"WHERE {self.column_name} = ?")

				cursor.execute(query, (f'{self.search_value}',))

				rows = cursor.fetchall()

				"""
				if rows:
					print(f"Found {len(rows)} matching rows:")
					for row in rows:
						print(row)

				else:
					print("No matching rows found")
				"""
				if rows:
					attribute_values = [row[0] for row in rows]
					all_attrib.append((attribute, attribute_values))
				else:
					all_attrib.append((attribute, []))

			return all_attrib
		except Exception as e:
			print("An error occurred: ", e)
			return None

	def load_img(self):
		"""
		Retrieves the image URL from the table at index 9 (assuming the image URL is stored there).

		Returns:
			The image URL as a string, or None if not found.
		"""
		try:
			# Query to fetch the column at index 9
			query = (f"SELECT * FROM {self.table_name} WHERE {self.column_name} = ?")
			cursor.execute(query, (f'{self.search_value}',))

			# Fetch the row
			row = cursor.fetchone()

			if row:
				# Assuming index 9 contains the URL
				img_url = row[9]
				return img_url
			else:
				print("No matching row found.")
				return None
		except Exception as e:
			print("An error occurred while loading the image URL: ", e)
			return None

	def fetch_random_hero(self):
		"""Fetch a random hero from the table."""
		try:
			query = f"SELECT TOP 1 * FROM {self.table_name} ORDER BY NEWID()"
			cursor.execute(query)
			row = cursor.fetchone()
			if row:
				return {
					"name": row[1],  # Assuming the name is in the second column
					"Intelligence": row[2],
					"Strength": row[3],
					"Speed": row[4],
					"Durability": row[5],
					"Power": row[6],
					"Combat": row[7]
				}
			else:
				return None
		except Exception as e:
			print(f"Error fetching random hero: {e}")
			return None
