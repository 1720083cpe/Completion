import csv
fieldnames = ['name', 'area', 'country_code2', 'country_code3']

rows = [
	{'name' : 'Japan',
	'area' : 377915,
	'country_code2' : 'JP',
	'country_code3' : 'JPN'},
	{'name' : 'South Korea',
	'area' : 100210,
	'country_code2' : 'SK',
	'country_code3' : 'SOKOR'},
	{'name' : 'Italy',
	'area' : 377915,
	'country_code2' : 'ITY',
	'country_code3' : 'ITALY'},
	{'name' : 'United States of America',
	'area' : 9857306,
	'country_code2' : 'US',
	'country_code3' : 'USA' }
	
]

with open('countries.csv', 'w', encoding = 'UTF8', newline = '\n' ) as f:
	writer = csv.DictWriter(f, fieldnames=fieldnames)
	writer.writeheader()
	writer.writerows(rows)