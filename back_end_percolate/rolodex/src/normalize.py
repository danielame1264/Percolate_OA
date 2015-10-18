import re
import logging
import pattern, constant


class NormalizationException(Exception):
	"""
	Custom exception on txt normalizing failure
	@param  The failing entry
	"""
	def __init__(self, message, entry):
		Exception.__init__(self, message)
		self.entry = entry


class Normalizer(object):
	"""
	Defines a parser from a list of accpeted patterns
	"""

	def __init__(self):

		self.accepted_patterns = [
			pattern.Pattern([constant.LAST_NAME_PATTERN, 
							 constant.FIRST_NAME_PATTERN,
							 constant.PHONE_NUMBER_PATTERN,
							 constant.COLOR_PATTERN,
							 constant.ZIP_CODE_PATTERN]),

			pattern.Pattern([constant.FIRST_NAME_PATTERN+" "+constant.LAST_NAME_PATTERN,
							 constant.COLOR_PATTERN,
							 constant.ZIP_CODE_PATTERN,
							 constant.PHONE_NUMBER_PATTERN]),

			pattern.Pattern([constant.FIRST_NAME_PATTERN,
							 constant.LAST_NAME_PATTERN,
							 constant.ZIP_CODE_PATTERN,
							 constant.PHONE_NUMBER_PATTERN,
							 constant.COLOR_PATTERN])	
		]


	def normalize(self, entry):
		"""
		Try normalizing each entry by all accpeted patterns
		@param Text to be mormalized
		@return A data model object for later processing
		"""
		for pattern in self.accepted_patterns:
			person = pattern.match_pattern(entry)
			if person:
				logging.info("Normalized %s" % entry)
				return person
		raise NormalizationException("Normalizing %s failed" % entry, entry)		
