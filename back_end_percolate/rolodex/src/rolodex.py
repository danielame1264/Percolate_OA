"""
Rolodex program main file
"""

import re, sys
import argparse
import simplejson as json
import logging
from normalize import Normalizer, NormalizationException
from person import Person 


def run_rolodex(input_file, output_file):
	"""
	This program takes an input file of personal information in multiple formats
	It normalize every valid entry and dumps the ordered result into an output file
	@param string input_file	input file name with path from current dir
	@param string output_file	output file name with path from current dir

	"""
	persons = []
	error_indices = []
	normalizer = Normalizer()

	with open(input_file) as input_file:
		for line_number, line in enumerate(input_file, start=1):
			try:
				person = normalizer.normalize(line.rstrip())
				persons.append(person)
			except NormalizationException:
				error_indices.append(line_number)

	sorted_persons = sorted(persons, key=lambda person: person.__str__())

	output_dict = {
			"entries": sorted_persons,
			"errors": error_indices
		}
	logging.info("Completed, please check output file.")
	with open(output_file, 'w') as output_file:
		json.dump(output_dict, output_file, indent=2, sort_keys=True)


def main():
	"""
	Entry point for this rolodex program
	"""
	parser = argparse.ArgumentParser("Rolodex")

	verbosity = ["DEBUG", "INFO", "ERROR"]
	parser.add_argument("-i", "--input", help="input file", required=True)
	parser.add_argument("-o", "--output", help="output file", required=True)
	parser.add_argument("-v", "--verbosity", help="verbosity level: %s" % verbosity, required=False)
	args = vars(parser.parse_args())

	if args["verbosity"] and args["verbosity"].upper() in verbosity:
		logging.basicConfig(level=args["verbosity"].upper(), stream=sys.stdout)
	else:
		logging.basicConfig(level=logging.INFO, stream=sys.stdout)
	
	input_file = args["input"]
	output_file = args["output"]


	run_rolodex(input_file, output_file)


if __name__ == "__main__":
	main()