# perform _d[key] = value
def assoc(_d, key, value):
	from copy import deepcopy
	d = deepcopy(_d)
	d[key] = value
	return d

# sequentially apply a list of functions to data
def pipeline_each(data, fns):
	return reduce(lambda a,x: map(x, a), fns, data)

# apply fn to key before assoc
def call(fn, key):
	def apply_fn(record):
		return assoc(record, key, fn(record.get(key)))
	return apply_fn

def first(data):
	return data[0]

def initial(data):
	return data[:-1]

def last(data):
	return data[-1]

def rest(data):
	return data[1:]

# Let's recreate Underscore.js in Python

def each(data, fn):
	map(lambda x: fn(x), data)

# Python already has map and reduce :)

def find(predicate, data):
	return first(filter(predicate, data))

# check if d contains key-value pair prop
# a blank key value pair is contained by all d
def contains_prop(d, prop):
	if not prop.keys():
		return True
	key = first(prop.keys())
	return d.get(key) == prop.get(key)

# a blank property list is contained by all d
# check d for each property
# if any are not in d, return false
def contains_props(d, props):
	if not props:
		return True
	elif not contains_prop(d, first(props)):
		return False
	else:
		return contains_props(d, rest(props))

def where(data, properties):
	if type(properties) != type(list()):
		properties = [properties]
	return filter(lambda d: contains_props(d, properties), data)

# create a list of an attribute for a list of dicts  
def pluck(data, key):
	return map(lambda x: x.get(key), data)


