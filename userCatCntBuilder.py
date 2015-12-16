from pymongo import MongoClient

if __name__ == "__main__":
	
	client = MongoClient()
	dBase = client.yelp_test_recommend

	userCat = dBase.yelp_test_user_cat

	userCatCnt = dBase.yelp_test_user_cat_cnt

	userCatCnt.remove({})

	print userCat.count()

	userCatCntDict = {}
	userCatCntList = []

	for item in userCat.find():
		catCount = {}
		distCat = list(set(item["categories"]))
		distCat.remove("Restaurants")
		for cat in distCat:
			catCount[cat] = item["categories"].count(cat)
		userCatCntDict["user_id"] = item["user_id"]
		userCatCntDict["review_count"] = catCount
		userCatCntList.append(userCatCntDict.copy())
	
	userCatCnt.insert(userCatCntList)

	for item in userCatCnt.find():
		print item

	