# There should be thousands of csv parsers out there, but I'm lazy you know ;)
# @author: @javierhonduco
import sys

class CsvParser:
	
	def __init__(self, file, becool=0):
		self.becool = becool
		self.dataStream = open(file, "r").read()
		self.date_format = "%d/%M/%Y, %H:%S"

	def proprocess(self):

		return [{int(line.split(",")[0]): self.prettify(int(line.split(",")[1]))} for line in self.dataStream.split("\n")] # creates the list...

	def jsonize(self):
		import json
		return json.dumps(self.proprocess()) # converts into a json string

	def prettify(self, WAT):
		from datetime import datetime
		if self.becool == 1:
			return datetime.fromtimestamp(WAT).strftime(self.date_format) # You hate *NIX timestamps madafaka? ;)
		else:
			return WAT
if __name__ == "__main__":
		parser = CsvParser(sys.argv[1].split("::")[0], int(sys.argv[1].split("::")[1]))  # LOL
		print parser.jsonize()


