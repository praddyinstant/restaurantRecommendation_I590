'''

This file filters out only those reviews that are for a restaurant.

'''



from pymongo import MongoClient

if __name__ == "__main__":
	client = MongoClient()

	dBase = client.yelp_test_recommend

	review = dBase.yelp_test_review

	restaurant = dBase.yelp_test_restaurant

	restaurantReviews = dBase.yelp_test_res_review

	restaurantReviews.remove({})

	for item in review.find():
		if restaurant.find_one({"business_id" : item["business_id"]}):
				restaurantReviews.insert(item)

	print "The total number of reviews for restaurants is : "
	print restaurantReviews.count()
