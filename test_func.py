import unittest
from func import *

class TestFuncFunctions(unittest.TestCase):

	def setUp(self):
		self.bands = [
		{
			'name': 'Skrillex',
			'country': 'USA',
			'active': True
		},{
			'name': 'Dillon Francis',
			'country': 'USoA',
			'active': True
		},{
			'name': 'Madeon',
			'country': 'France',
			'active': True
		},{
			'name': 'Sparce'
		}
	]

	def test_assoc(self):
		self.bands[0] = assoc(self.bands[0], 'country', 'Canada')
		self.assertEqual(self.bands[0]['country'], 'Canada')

	def test_pipeline_each(self):
		self.bands = pipeline_each(self.bands, [
			lambda x: assoc(x, 'name', 'Dan'),
			lambda x: assoc(x, 'active', False),
		])

		# are all names 'Dan'?
		map(lambda x: self.assertEqual(x['name'], 'Dan'), self.bands)
		# are all bands not active?
		map(lambda x: self.assertEqual(x['active'], False), self.bands)

	def test_call(self):
		self.bands = pipeline_each(self.bands, [
			call(lambda x: 'Canada', 'country'),
			call(lambda x: False, 'active')
		])

		# are all countries 'Canada'?
		map(lambda x: self.assertEqual(x['country'], 'Canada'), self.bands)
		# are all bands not active?
		map(lambda x: self.assertEqual(x['active'], False), self.bands)

	def test_each(self):
		arr = []
		def push(x):
			arr.append(x)
		each(self.bands, push)

		# compare the dictionaries, zero if identical
		self.assertEqual(cmp(arr, self.bands), 0)

	def test_first(self):
		# get first element
		self.assertEqual(3, first([3,4,5,6]))
		# empty list returns None
		self.assertEqual(None, first([]))

	def test_initial(self):
		# get all but last value
		self.assertEqual([3,4,5], initial([3,4,5,6]))
		# empty list returns empty list
		self.assertEqual([], initial([]))

	def test_last(self):
		# get list item
		self.assertEqual(6, last([3,4,5,6]))
		# empty list returns None
		self.assertEqual(None, last([]))

	def test_rest(self):
		# get all but first value
		self.assertEqual([4,5,6], rest([3,4,5,6]))
		# empty list returns empty list
		self.assertEqual([], rest([]))

	def test_find(self):
		arr = [2,3,4,5,6,7,8]
		# first item divisible by 4
		self.assertEqual(4, find(lambda x: x%4==0, arr))
		# first item greater than 7
		self.assertEqual(7, find(lambda x: x>6, arr))


	def test_where(self):
		# get all active bands
		bands_where = where(self.bands, {'active': True})
		bands_where_for = [b for b in self.bands if b.get('active')]
		self.assertEqual(cmp(bands_where, bands_where_for), 0)

		# get all inactive bands
		bands_where = where(self.bands, {'active': False})
		bands_where_for = [b for b in self.bands if b.get('active') == False]
		self.assertEqual(cmp(bands_where, bands_where_for), 0)

		# get all active bands from France
		bands_where2 = where(self.bands, {'active': True, 'country': 'France'})
		bands_where_for2 = [b for b in self.bands if b.get('active') and b.get('country') == 'France']
		self.assertEqual(cmp(bands_where2, bands_where_for2), 0)

		# get all bands
		bands_where = where(self.bands, {})
		self.assertEqual(cmp(bands_where, self.bands), 0)

	def test_find_where(self):
		# get first inactive band
		bands_where = find_where(self.bands, {'active': False})
		bands_where_for = first([b for b in self.bands if b.get('active') == False])
		self.assertEqual(bands_where, bands_where_for)

		# get first active band from France
		bands_where = find_where(self.bands, {'active': True, 'country': 'France'})
		bands_where_for = first([b for b in self.bands if b.get('active') and b.get('country') == 'France'])
		self.assertEqual(bands_where, bands_where_for)

		# try to find some other property
		bands_where = find_where(self.bands, {'monster': True})
		bands_where_for = first([b for b in self.bands if b.get('monster')])
		self.assertEqual(bands_where, bands_where_for)
		self.assertEqual(bands_where, None)

	def test_reject(self):
		# reject numbers that are even
		ls = [1,2,3,4,5,6,7]
		odds = [l for l in ls if l%2==1]
		reject_odds = reject(lambda x: x%2==0, ls)
		self.assertEqual(odds, reject_odds)

	def test_every(self):
		self.assertFalse(every(lambda x: x, [True, True, False]))
		self.assertTrue(every(lambda x: x, [True, True]))
		# are all numbers even
		def even(n):
			return n%2==0
		self.assertTrue(every(even, [2, 10, 200]))
		# every x in [] is true
		self.assertTrue(every(lambda x: x, []))

	def test_some(self):
		# some number is even
		self.assertTrue(some(lambda x: x%2==0, [1,3,5,7,8]))
		# no number is a multiple of 5
		self.assertFalse(some(lambda x: x%5==0, [1,3,7,8]))
		# no element is even
		self.assertFalse(some(lambda x: x%2==0, []))

	def test_contains(self):
		self.assertTrue(contains([2,3,5], 3))
		self.assertTrue(contains([(2,3),3,5], (2,3)))
		self.assertFalse(contains([False, []], [1]))
		self.assertTrue(contains([False, [1]], [1]))

	def test_pluck(self):
		# get list of bands' countries
		countries = pluck(self.bands, 'country')
		self.assertEqual(countries, [b.get('country') for b in self.bands])

	def test_compact(self):
		li = [[], {}, False, True, 1, [2]]
		for_li = [l for l in li if bool(l)]
		compact_li = compact(li)
		self.assertEqual(for_li, compact_li)

	def test_partition(self):
		nums = [1,2,3,4,5,6]
		def odd(n):
			return n%2==1
		odds = [n for n in nums if odd(n)]
		evens = [n for n in nums if not odd(n)]
		manual = [odds, evens]

		partitioned = partition(odd, nums)

		self.assertEqual(manual, partitioned)

	def test_flatten(self):
		f = [1,[2]]
		flat_f = flatten(f)
		self.assertEqual(flat_f, [1,2])

		f = [1, 2, [3, 4, [5, [6]]], [2]]
		flat_f = flatten(f)

		self.assertEqual(flat_f, [1,2,3,4,5,6,2])

if __name__ == '__main__':
	unittest.main()


