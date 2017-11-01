import requests
import csv
from csv import DictWriter
from csv import DictReader
import xml.etree.ElementTree as ET

class Geocoding:

	def __init__(self):
		self.companies = []

	#getCoordinates takes in the name of a CSV file to read from and the name of the row that the address is located in
	#adds this information into a new CSV file called withCoordinates
	def getCoordinates( self, name, rowName ):
		with open(name, 'rb') as f:
			address = []
			reader = DictReader(f)
			for row in reader:
				address = row.get(rowName)
				url = 'https://maps.googleapis.com/maps/api/geocode/xml?address=' + address + '&key=AIzaSyDaPtoE0puJEHub9FQqoJAcBXibAysVjIg'
				r = requests.get(url)
				data = r.content
				root = ET.fromstring(data)
				try:
					row['latitude'] = root.find('result').find('geometry').find('location').find('lat').text
					row['longitude'] = root.find('result').find('geometry').find('location').find('lng').text
				except AttributeError:
					row['latitude'] = ''
					row['longitude'] = ''
				self.companies.append(row)
			f.close()
		keys = companies[1].keys()
		writeTo = open('withCoordinates', 'wb')
		writer = DictWriter(writeTo, keys)
		writer.writeheader()
		for company in companies:
			writer.writerow(company)
		writeTo.close()

if __name__ == "__main__":
    import doctest
    doctest.testmod()


