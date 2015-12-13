import re
import json
from pymongo import *

def decode_json(line):
	try:
		return json.loads(line)
	except:
		return None

with open("yelp_academic_dataset_user.json") as f:
	yelp_data_user = [decode_json(line) for line in f]

#print len(yelp_data_business)

if __name__ == '__main__':
	client = MongoClient()

	dBase = client.yelp_test_recommend

	user = dBase.yelp_test_user

	user.remove({})
	# Populate the User collection
	for item in yelp_data_user:
		user.insert(item)

	print user.count()