import pyodbc

from HomePage import app

db_file = r"C:\Users\louis\OneDrive - Year Up- BOS\YearUp\Mod 2\Capstone\Super\SuperVS.accdb"
connection = (r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
			  f'DBQ={db_file};')

conn = pyodbc.connect(connection)
cursor = conn.cursor()

if __name__ == '__main__':
	# hero_name = FetchData("SuperVS", "Alias", "Flash")
	# hero_attrib = WeightedPower()
	# hero_attrib.weighted_combat("SuperVS", "")
	app.run(debug = True)
