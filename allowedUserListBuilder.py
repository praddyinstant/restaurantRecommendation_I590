'''

This file prints out all the users for whom the system can provide recommendations. The output of this file can be redirected to a text file in order to store the user_id s of all these users, using the command '$python allowedUsrrListBuilder.py > allowedUserList.txt'.

'''


from pymongo import MongoClient

if __name__ == "__main__":
	client  = MongoClient()
	dBase = client.yelp_test_recommend

	userPref = dBase.yelp_test_user_pref

	for item in userPref.find():
		print item["user_id"]