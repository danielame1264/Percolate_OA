import unittest
import re
import constant
from src.pattern import Pattern, PatternException
from src.person import Person

class PatternTest(unittest.TestCase):

	def test_pattern_constructor(self):
		"""
		Test if pattern constructor works
		"""
		pattern = Pattern(["\w+","\w+","\w+","\w+"])

		self.assertEqual(pattern.final_line_pattern, "\w+, \w+, \w+, \w+")
		self.assertEqual(pattern.delimiter, ", ")
		self.assertEqual(pattern.regex, re.compile("^" + pattern.final_line_pattern + "$"))

	def test_match_pattern_success_return_person(self):
		entry = "Clary, Blair, (463)-118-2451, red, 07256"

		pattern = Pattern([constant.LAST_NAME_PATTERN, 
						   constant.FIRST_NAME_PATTERN,
						   constant.PHONE_NUMBER_PATTERN,
						   constant.COLOR_PATTERN,
						   constant.ZIP_CODE_PATTERN])


		result = pattern.match_pattern(entry)
		self.assertTrue(isinstance(result, Person))

	def test_match_pattern_fail_no_match_return_none(self):
		entry = "Clary, Blair, (463)-112118-2451, red, 027256"

		pattern = Pattern([constant.LAST_NAME_PATTERN, 
						   constant.FIRST_NAME_PATTERN,
						   constant.PHONE_NUMBER_PATTERN,
						   constant.COLOR_PATTERN,
						   constant.ZIP_CODE_PATTERN])
		result = pattern.match_pattern(entry)
		self.assertEqual(result, None)

	def test_match_pattern_raise_exception(self):
		entry = "Clary, Blair, (463)-118-2451, red"
		pattern = Pattern([constant.LAST_NAME_PATTERN, 
						   constant.FIRST_NAME_PATTERN,
						   constant.PHONE_NUMBER_PATTERN,
						   constant.COLOR_PATTERN])
		self.assertRaises(PatternException, pattern.match_pattern, entry)
