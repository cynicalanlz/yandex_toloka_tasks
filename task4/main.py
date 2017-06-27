import json
import pandas as pd

with open('test_tasks.json') as f:    
    f = f.read()

    f = ''.join(
    	[
	    	'[',
	    	f,
	    	']',
	    ])

    data = json.loads(f)

fields_list = [
	"created", 
	"status", 
	"coordinates", 
	"user_id"
	]

items = []

for obj in data:

	it = {}
	for f in fields_list:
		val = obj.get(f)
		if val:
			it[f] = val

	if 'tasks' in obj:
		it['tids'] = ','.join([item.get('id', '--') for item in obj['tasks']])
		it['coords'] = ','.join([item.get('input_values', {}).get('coordinates', '--') for item in obj['tasks']])

	items.append(it)

df = pd.DataFrame.from_dict(items, orient="columns")

df.to_csv('out.csv', sep='\t')
