if __name__ == "__main__":
	parser = argparse.ArgumentParser(description='finds longitude and latitude coordinates for addresses in a given CSV file')
	parser.add_argument('file')
	parser.add_argument('rowName')
	args = parser.parse_args()
	c = Geocoding2.Geocoding()
	c.getCoordinates( args.file, args.rowName )
