import unittest
from mock import patch
from src.normalize import Normalizer, NormalizationException
from src.person import Person
from src import pattern

class NormalizerTest(unittest.TestCase):

	def test_normalizer_constructor(self):
		"""
		Test if normalizer constructor works
		"""
		normalizer = Normalizer()
		self.assertEqual(len(normalizer.accepted_patterns),3)


	@patch('src.pattern.Pattern.match_pattern')
	def test_normalize_success(self, mock_match_pattern):
		"""
		Test returning person object on success normalizing
		"""
		mock_person = Person("a","b","123456789","c","2")
		mock_match_pattern.return_value = mock_person
		normalizer = Normalizer()
		entry = "Aura, Eilers, 39358, 489 634 9504, pink"
		res = normalizer.normalize(entry)
		mock_match_pattern.assert_called_with(entry)
		self.assertEqual(res, mock_person)

	@patch('src.pattern.Pattern.match_pattern')
	def test_normalize_raise_exception(self, mock_match_pattern):
		"""
		Test no match for all patterns raises exception
		"""
		mock_match_pattern.return_value = None
		entry = "doesn't matter"
		normalizer = Normalizer()
		self.assertRaises(NormalizationException, normalizer.normalize, entry)
