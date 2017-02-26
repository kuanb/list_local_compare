from functools import reduce

def clean(word):
	return word.lower().strip()

def compare(x, y, s):
	return abs(x - y) > s

def operation(arr, sensitivity=1):
	# lookup dict, will describe the array
	ref = {}

	# fill the lookup table with list values
	for i, item in enumerate(arr):
		item = clean(item)
		if item in ref:
			ref[item]['indices'].append(i)
		else:
			ref[item] = { 'indices': [i] }

	# drop 'duplicates' based on sensitivity
	deduped = []
	for key in ref:
		reduced = []
		for i in ref[key]['indices']:
			if len(reduced) > 0:
				if compare(i, reduced[-1], sensitivity):
					reduced.append(i)
			else:
				reduced.append(i)

		for r in reduced:
			deduped.append((key, r))

	deduped.sort(key=lambda x:x[1])
	return list(map(lambda x: x[0], deduped))

case1 = ['foo', 'can', 'bar', ' Bar']
assert operation(case1) == ['foo', 'can', 'bar']

case2 = ['foo', 'bar', ' Bar', 'tal']
assert operation(case2) == ['foo', 'bar', 'tal']

case3 = ['foo', 'bar', 'soon', ' Bar']
assert operation(case3) == ['foo', 'bar', 'soon', 'bar']
