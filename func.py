''' Perform _d[key] = value '''
def assoc(_d, key, value):
	from copy import deepcopy
	d = deepcopy(_d)
	d[key] = value
	return d

''' Sequentially apply a list of functions to data '''
def pipeline_each(data, fns):
	return reduce(lambda a,x: map(x, a), fns, data)

''' Apply fn to key before assoc '''
def call(fn, key):
	def apply_fn(record):
		return assoc(record, key, fn(record.get(key)))
	return apply_fn

''' Get first element of list or None '''
def first(data):
	return data[0] if data else None

''' Get all but last element of list '''
def initial(data):
	return data[:-1]

''' Get last element of list or None '''
def last(data):
	return data[-1] if data else None

''' Get all but first element of list '''
def rest(data):
	return data[1:]

# Let's recreate Underscore.js in Python

''' Apply fn to all elements in data '''
def each(data, fn):
	map(lambda x: fn(x), data)

# Python already has map and reduce :)

''' Return first item in data that satisfies fn '''
def find(fn, data):
	return first(filter(fn, data))

''' 
	Check if d contains props
	A blank property list is contained by all d
	Check that props is a subset of d
'''
def contains_props(d, props):
	if not props:
		return True
	return set(props.items()).issubset(set(d.items()))

''' Return all dicts in data take contain all properties '''
def where(data, properties):
	return filter(lambda d: contains_props(d, properties), data)

''' Find first dict that contains properties '''
def find_where(data, properties):
	return first(where(data, properties))

''' Return items that do not satisfy fn '''
def reject(fn, data):
	return filter(lambda x: not fn(x), data)

'''
Return True is fn of every item is True
No items => True
'''
def every(fn, data):
	return reduce(lambda a,x: a and fn(x), data, True)

'''
Return True is fn of any item is True
No items => False
'''
def some(fn, data):
	return reduce(lambda a,x: a or fn(x), data, False)

''' Create a list of an attribute for a list of dicts '''
def pluck(data, key):
	return map(lambda x: x.get(key), data)


