import re
import logging
from person import Person


class PatternException(Exception):
	"""
	Custom exception on bad pattern(Unable to construct data model from normalized result)
	@param regex	The failed regexp
	@param entry	The failed text entry
	"""

	def __init__(self, message, regex, entry):
		Exception.__init__(self, message)
		self.regex = regex
		self.entry = entry


class Pattern(object):
	"""
	Defines a valid pattern
	@param	A valid regex pattern for text entry
	"""

	def __init__(self, pattern):

		self.delimiter = ", "
		self.final_line_pattern = self.delimiter.join(pattern)
		self.regex = re.compile("^" + self.final_line_pattern + "$")

	def match_pattern(self, entry):
		"""
		Try matching the entry with pattern
		@param  Text entry
		@return A data model object if there is a match, or None otherwise
		@raise  PatternException when the entry matched but data model can't be created
		"""
		match = self.regex.match(entry)
		if match:
			group = match.groupdict()
			try:
				person = Person(group['first_name'],
								group['last_name'],
								group['phone_number'],
								group['color'],
								group['zipcode'])
				return person
			except Exception:
				raise PatternException("Found a match but can't construct person from entry", self.final_line_pattern, entry)
		else:
			return None
