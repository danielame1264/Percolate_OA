import unittest
import os
from src.rolodex import run_rolodex

class RolodexTest(unittest.TestCase):

	def test_run_rolodex(self):
		"""
		Test if result file is created
		"""
		run_rolodex("data.in", "data.out")
		self.assertTrue(os.path.isfile("data.out"))
