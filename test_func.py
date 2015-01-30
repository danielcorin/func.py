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
		},
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
		self.assertEqual(3, first([3,4,5,6]))

	def test_initial(self):
		self.assertEqual([3,4,5], initial([3,4,5,6]))

	def test_last(self):
		self.assertEqual(6, last([3,4,5,6]))

	def test_rest(self):
		self.assertEqual([4,5,6], rest([3,4,5,6]))

	def test_find(self):
		arr = [2,3,4,5,6,7,8]

		self.assertEqual(4, find(lambda x: x%4==0, arr))

		self.assertEqual(7, find(lambda x: x>6, arr))


	def test_contains_prop(self):
		d = {'active':True, 'prop2':'hello'}
		self.assertTrue(contains_prop(d, {'active':True}))
		self.assertTrue(contains_prop(d, {'prop2':'hello'}))

		self.assertFalse(contains_prop(d, {'active':False}))
		self.assertFalse(contains_prop(d, {'prop3':'testing'}))

	def test_where(self):
		bands_where = where(self.bands, [{'active': True}])
		bands_where_for = [b for b in self.bands if b.get('active')]
		self.assertEqual(cmp(bands_where, bands_where_for), 0)

		bands_where = where(self.bands, [{'active': False}])
		bands_where_for = [b for b in self.bands if not b.get('active')]
		self.assertEqual(cmp(bands_where, bands_where_for), 0)

		bands_where = where(self.bands, {'active': False})
		bands_where_for = [b for b in self.bands if not b.get('active')]
		self.assertEqual(cmp(bands_where, bands_where_for), 0)

		bands_where2 = where(self.bands, [{'active': True}, {'country':'France'}])
		bands_where_for2 = [b for b in self.bands if b.get('active') and b.get('country') == 'France']
		self.assertEqual(cmp(bands_where2, bands_where_for2), 0)

		bands_where = where(self.bands, {})
		self.assertEqual(cmp(bands_where, self.bands), 0)

	def test_pluck(self):
		countries = pluck(self.bands, 'country')
		self.assertEqual(countries, [b['country'] for b in self.bands])

if __name__ == '__main__':
	unittest.main()