'''

This file creates a new collection that stores users' restaurant category preferences in sorted order, based on the total number of times he / she has reviewed that category.

'''



from pymongo import MongoClient

if __name__ == "__main__":

	client = MongoClient()
	dBase = client.yelp_test_recommend

	userCatCnt = dBase.yelp_test_user_cat_cnt

	userPref = dBase.yelp_test_user_pref

	userPref.remove({})

	userPrefDict = {}
	userPrefList = []
	for item in userCatCnt.find():
		userPrefDict["user_id"] = item["user_id"]
		catCnt = item["review_count"]
		userPrefDict["categories"] = [k for k, v in sorted(catCnt.items(), key = lambda x:x[1], reverse = True)]
		userPrefList.append(userPrefDict.copy())

	userPref.insert(userPrefList)

	for item in userPref.find():
		print item