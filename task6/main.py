import pandas


df = pandas.read_csv('data_task3.csv', sep='\t')
df['suc'] = (df['jud'] == df['cjud']) * 1


t1 = df[['uid', 'suc']].groupby(
	'uid'
	).sum()

t1.sort_values('suc', inplace=True)


t2 = df[['uid', 'jud']].groupby(
	'uid').aggregate(['sum', 'count'])

t2 = t2['jud']

t2['pos'] = t2['sum'] / t2['count'] 

avg_pos = t2['pos'].mean()

t2['pos_rel_avg'] = t2['pos'] / avg_pos
t2.sort_values('pos_rel_avg', inplace=True)

print t2


t3 = df[['docid', 'jud', 'suc']].groupby(
	[
		'docid',
	]
	).aggregate(['sum', 'count'])


t3.loc[:, ('jud', 'pos')] = t3['jud']['sum'] / t3['jud']['count'] 
avg_jud_pos = t3[('jud', 'pos')].mean()
t3.loc[:, ('jud', 'pos_rel_avg')] = t3['jud']['pos'] / avg_jud_pos


t3.loc[:, ('suc', 'pos')] = t3['suc']['sum'] / t3['suc']['count'] 
avg_suc_pos = t3[('jud', 'pos')].mean()
t3.loc[:, ('jud', 'suc_rel_avg')] = t3['suc']['pos'] / avg_suc_pos

print t3

# then merge the t3 df to groupby [docid, userid] table on docid
# then calculate user success/failture weight relative to average success among all users
# sum weights by user
