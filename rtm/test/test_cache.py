"""
    Copyright (c) 2012 Philip Schliehauf (uniphil@gmail.com) and the
    Queen's University Applied Sustainability Centre
    
    This project is hosted on github; for up-to-date code and contacts:
    https://github.com/Queens-Applied-Sustainability/PyRTM
    
    This file is part of PyRTM.

    PyRTM is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    PyRTM is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with PyRTM.  If not, see <http://www.gnu.org/licenses/>.
"""

# import unittest
# import shutil
# import time
# from datetime import datetime
# from .. import cache

# class TestVarsToFile(unittest.TestCase):

# 	def assertClean(self, inp, res):
# 		clean = cache.vars_to_file(inp)
# 		self.assertEqual(clean, res)

# 	def testOneChar(self):
# 		self.assertClean(['a'], 'a')

# 	def testOneString(self):
# 		self.assertClean(['hello'], 'hello')

# 	def testOtherType(self):
# 		self.assertClean([1], '1')

# 	def testStringJoin(self):
# 		self.assertClean(['a', 'b'], 'a-b')

# 	def testCharReplace(self):
# 		some_illegals = ' !@#$%^&*()+=<>?;"\'[]{}~`'
# 		for illegal in some_illegals:
# 			dirty = illegal.join(['a', 'b'])
# 			self.assertClean([dirty], 'a.b')

# 	def testGeneratorIn(self):
# 		self.assertClean((str(i) for i in xrange(2)), '0-1')


# class TestGet(unittest.TestCase):

# 	def setUp(self):
# 		self.expensive_fn = lambda c: 1
# 		self.config = {
# 			'description': 'test',
# 			'longitude': -75.3,
# 			'latitude': 44.22,
# 			'time': datetime(2012, 1, 1, 0, 0, 0)
# 		}
# 		self.cachedconfig = {
# 			'description': 'cachedtest',
# 			'longitude': -75.3,
# 			'latitude': 44.22,
# 			'time': datetime(2012, 1, 1, 0, 0, 0)
# 		}
# 		cache.get(self.expensive_fn, self.cachedconfig)

# 	def testFunc(self):
# 		result = cache.get(self.expensive_fn, self.config)
# 		self.assertEqual(result, (1, False))

# 	def testCached(self):
# 		result = cache.get(self.expensive_fn, self.cachedconfig)
# 		self.assertEqual(result, (1, True))

# 	def tearDown(self):
# 		shutil.rmtree(cache.CACHE_DIR)



# if __name__ == '__main__':
# 	unittest.main()

