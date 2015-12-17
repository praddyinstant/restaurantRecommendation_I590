from pymongo import MongoClient

if __name__ == "__main__":
	client  = MongoClient()
	dBase = client.yelp_test_recommend

	userPref = dBase.yelp_test_user_pref

	for item in userPref.find():
		print item["user_id"]