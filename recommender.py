from pymongo import MongoClient
import sys

if __name__ == "__main__":
	client = MongoClient()
	dBase = client.yelp_test_recommend

	userPref = dBase.yelp_test_user_pref

	checkin = dBase.yelp_test_checkin

	Edinburgh = dBase.yelp_test_Edinburgh
	Karlsruhe = dBase.yelp_test_Karlsruhe
	Montreal = dBase.yelp_test_Montreal
	Waterloo = dBase.yelp_test_Waterloo
	Pittsburgh = dBase.yelp_test_Pittsburgh
	Charlotte = dBase.yelp_test_Charlotte
	Urbana_Champaign = dBase.yelp_test_Urbana_Champaign
	Phoenix = dBase.yelp_test_Phoenix
	Las_Vegas = dBase.yelp_test_Las_Vegas
	Madison = dBase.yelp_test_Madison
	user_id = raw_input("Please enter your Yelp user id: ")
	city = raw_input("Please enter your city preference: ")
	time = raw_input("Please enter your preference for time: ").lower()

	print "Please wait while we find you some nice restaurants . . ."

	if userPref.find_one({"user_id" : user_id}) == None:
		print "Sorry invalid user id."
		sys.exit(0)

	preferences = []

	for item in userPref.find({"user_id" : user_id}):
		if len(item["categories"]) >= 4:
			preferences = item["categories"][0:4]
		else:
			preferences = item["categories"][:]
	if city == "Pittsburgh":
		cityCol = dBase.yelp_test_Pittsburgh
	elif city == "Edinburgh":
		cityCol = dBase.yelp_test_Edinburgh
	elif city == "Carlsruhe":
		cityCol = dBase.yelp_test_Carlsruhe
	elif city == "Montreal":
		cityCol = dBase.yelp_test_Montreal
	elif city == "Waterloo":
		cityCol = dBase.yelp_test_Waterloo
	elif city == "Charlotte":
		cityCol = dBase.yelp_test_Charlotte
	elif city == "Urbana-Champaign":
		cityCol = dBase.yelp_test_Urbana_Champaign
	elif city == "Phoenix":
		cityCol = dBase.yelp_test_Phoenix
	elif city == "Las Vegas":
		cityCol = dBase.yelp_test_Las_Vegas
	elif city == "Madison":
		cityCol = dBase.yelp_test_Madison
	else:
		print "Invalid City."
		sys.exit(0)

	if time not in ["breakfast","lunch","dinner","latenight"]: 
		print "Invalid time!"
		sys.exit(0)
	
	res = []

	print "Your preferences are: ", preferences

	for item in cityCol.find({"categories" : {'$in' : preferences}}):
		res.append(item)

	checkin_value = 0

	finalDict = {}

	for r in res:
		rating_value = float(float(r["stars"] / 5) * 7)
		for item in checkin.find({"business_id": r["business_id"]}):
			checkin_value =  float(3*(float(item[time]) / float(item["breakfast"] + item["lunch"] + item["dinner"] + item["latenight"])))
		totalValue = rating_value + checkin_value
		finalDict[r["business_id"]] = totalValue
		#print "Name: ",r["name"],"Address: ",r["full_address"]," Value : ", totalValue
	
	finalList = [k for k,v in sorted(finalDict.items(), key = lambda x:x[1], reverse = True)]

	maximum = 1
	print "We recommend these restaurants based on your city, time and previous food preferences: "
	for i in finalList:
		if maximum <= 10:
			for r in res:
				if i == r["business_id"]:
					print "Restaurant name: ",r['name']," Value: ",finalDict[r['business_id']]
		maximum += 1
	#print cityCol.count()