'''

This file builds a MongoDB collection for storing all the reviews from the Yelp Academic Dataset

'''
import json
from pymongo import MongoClient

def decode_json(line):
	try:
		return json.loads(line)
	except:
		return None

with open("yelp_academic_dataset_review.json") as g:
	yelp_data_review = [decode_json(line) for line in g]

if __name__ == '__main__':
	client = MongoClient()

	# Access the yelp_test database
	dBase = client.yelp_test_recommend

	# Build a new collection for storing the reviews from the review json file
	review = dBase.yelp_test_review

	# To clear the review collection for not printing old values
	review.remove({})

	# Populate the review collection
	count = 1
	for item in yelp_data_review:
		print count
		review.insert(item)
		count = count + 1
	# Print total number of reviews in the collection
	print review.count()