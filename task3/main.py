# -*- coding: utf-8 -*-
# untested

import httplib
import json 

api_host = "toloka.yandex.com"
oauth_token = "AQAAAAAN_c743d2832c24c299635a111f"


def make_call(method, url, body=None):
	client = httplib.HTTPSConnection(api_host)
	headers = {"Authorization": "OAuth " + oauth_token,
			   "Content-Type": "application/json"}
	client.request(method, "/api/v1" + url, body, headers)
	r = client.getresponse()
	print(r.read())
	client.close()

def save_file(method, url, filename, body=None):
	client = httplib.HTTPSConnection(api_host)
	headers = {"Authorization": "OAuth " + oauth_token,
			   "Content-Type": "application/json"}
	client.request(method, "/api/v1" + url, body, headers)
	r = client.getresponse()
	with open(filename, "wb") as f:
		while True:
			buf = r.read(1024 * 1024)
			if len(buf) == 0:
				break
			f.write(buf)
	client.close()

def edit_overlap(overlap, poolId):
	method = 'PATCH'
	client = httplib.HTTPSConnection(api_host)
	headers = {"Authorization": "OAuth " + oauth_token,
			   "Content-Type": "application/json"}

	body = json.dumps({
		'overlap' : overlap
	})

	url = ''.join([
		'/task-suites/',
		poolId
		]) 

	client.request(method, "/api/v1" + url, body, headers)
	r = client.getresponse()
	print(r.read())
	client.close()
	

def get_assignments(poolId):
	url = "/assignments?pool_id=" + poolId + "&limit=100000&sort=id"
	save_file("GET", url, poolId + "_assignments.csv")
	

print edit_overlap(5, "189591")