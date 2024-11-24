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
			self.search_value = input("hero: ")
			cursor.execute(query, (f'{self.search_value}',))

			rows = cursor.fetchall()

			if rows:
				print(f"Found {len(rows)} matching rows:")
				for row in rows:
					print(row)
			else:
				print("No matching rows found")

			return rows
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
trial = FetchData("SuperVs", "Alias", "Flash")
print(trial.src_data())


