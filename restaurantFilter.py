'''

This file filters out the restaurants from all different kind of businesses that are there in the business json file.

'''
import json
from pymongo import MongoClient

def decode_json(line):
	try:
		return json.loads(line)
	except:
		return None

with open("yelp_academic_dataset_business.json") as f:
	yelp_data_business = [decode_json(line) for line in f]

if __name__ == '__main__':
	client = MongoClient()

	dBase = client.yelp_test_recommend

	business = dBase.yelp_test_business

	# To clear the business collection for not printing old values
	business.remove({})

	# Populate the business collection
	for item in yelp_data_business:
		business.insert(item)

	
	# CREATE SEPARATE COLLECTIONS FOR EACH BUSINESS CATEGORY TO BE EXAMINED

	# For Indian restaurants create collection
	restaurant = dBase.yelp_test_restaurant

	# Get rid of the old documents inside the collection
	restaurant.remove({})

	# populate the newly created empty collection
	for item in business.find({"categories": "Restaurants"}):
		restaurant.insert(item)

	# print Restaurant counts
	print "Total number of documents inside Restaurant collection: "
	print restaurant.count()
	print "Total number of distinct documents inside indianRestaurant collection: "