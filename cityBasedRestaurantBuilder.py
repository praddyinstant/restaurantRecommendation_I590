"""
This code builds collections for all restaurants that are in the same city. So as many collections will be built as
there are cities in the Yelp academic dataset.
"""
from pymongo import MongoClient

if __name__ == "__main__":
	client = MongoClient()
	dBase = client.yelp_test_recommend

	restaurant = dBase.yelp_test_restaurant

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

	Edinburgh.remove({})
	Karlsruhe.remove({})
	Montreal.remove({})
	Waterloo.remove({})
	Pittsburgh.remove({})
	Charlotte.remove({})
	Urbana_Champaign.remove({})
	Phoenix.remove({})
	Las_Vegas.remove({})
	Madison.remove({})

	for item in restaurant.find():
		if item["city"] == "Edinburgh":
			Edinburgh.insert_one(item)
		if item["city"] == "Karlsruhe":
			Karlsruhe.insert_one(item)
		if item["city"] == "Montreal":
			Montreal.insert_one(item)
		if item["city"] == "Waterloo":
			Waterloo.insert_one(item)
		if item["city"] == "Pittsburgh":
			Pittsburgh.insert_one(item)
		if item["city"] == "Charlotte":
			Charlotte.insert_one(item)
		if item["city"] == "Urbana":
			Urbana_Champaign.insert_one(item)
		if item["city"] == "Phoenix":
			Phoenix.insert_one(item)
		if item["city"] == "Las Vegas":
			Las_Vegas.insert_one(item)
		if item["city"] == "Madison":
			Madison.insert_one(item)

	print Edinburgh.count()
	print Karlsruhe.count()
	print Montreal.count()
	print Waterloo.count()
	print Pittsburgh.count()
	print Charlotte.count()
	print Urbana_Champaign.count()
	print Phoenix.count()
	print Las_Vegas.count()
	print Madison.count()