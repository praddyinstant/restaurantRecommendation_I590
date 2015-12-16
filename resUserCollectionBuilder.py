from pymongo import *

if __name__ == '__main__':
	client = MongoClient()

	dBase = client.yelp_test_recommend

	user = dBase.yelp_test_user

	restaurantReviews = dBase.yelp_test_res_review

	reducedUser = dBase.yelp_test_reduced_user

	reducedUser.remove({})

	reducedUser_list = []
	user_list = []

	count = 0
	for item in user.find():
		if item['review_count'] >= 1000:
			user_list.append(item["user_id"])

			
	for item in user_list:
		if restaurantReviews.find_one({'user_id' : item}):
			reducedUser_list.append(item)


	print "Resturant review user list size: ", len(reducedUser_list)

	for item in reducedUser_list:
		reducedUser.insert(user.find_one({'user_id': item}))

	print "After insert reducedUser count: ", reducedUser.count()