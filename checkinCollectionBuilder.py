'''

This file builds a collection that can store the checkin counts for various meal times for each business.

'''


import json
from pymongo import MongoClient

def decode_json(line):
	try:
		return json.loads(line)
	except:
		return None

with open("yelp_academic_dataset_checkin.json") as f:
	yelp_data_checkin = [decode_json(line) for line in f]


if __name__ == '__main__':

    bf = lun = din = latenight = 0
    client = MongoClient()
    dBase = client.yelp_test_recommend
    restaurant = dBase.yelp_test_restaurant
    checkin = dBase.yelp_test_checkin

    checkin.remove({})

    for item in yelp_data_checkin:
        if restaurant.find_one({"business_id": item["business_id"]}) != None:
            for i in item["checkin_info"]:
                if i in ["4-0","4-1","4-2", "4-3", "4-4", "4-5","4-6"]:
                    bf += item["checkin_info"][i]
                if i in ["5-0","5-1","5-2", "5-3", "5-4", "5-5","5-6"]:
                    bf += item["checkin_info"][i]
                if i in ["6-0","6-1","6-2", "6-3", "6-4", "6-5","6-6"]:
                    bf += item["checkin_info"][i]
                if i in ["7-0","7-1","7-2", "7-3", "7-4", "7-5","7-6"]:
                    bf += item["checkin_info"][i]
                if i in ["8-0","8-1","8-2", "8-3", "8-4", "8-5","8-6"]:
                    bf += item["checkin_info"][i]
                if i in ["9-0","9-1","9-2", "9-3", "9-4", "9-5","9-6"]:
                    bf += item["checkin_info"][i]
                if i in ["10-0","10-1","10-2", "10-3", "10-4", "10-5","10-6"]:
                    bf += item["checkin_info"][i]
                if i in ["11-0","11-1","11-2", "11-3", "11-4", "11-5","11-6"]:
                    lun += item["checkin_info"][i]
                if i in ["12-0","12-1","12-2", "12-3", "12-4", "12-5","12-6"]:
                    lun += item["checkin_info"][i]
                if i in ["13-0","13-1","13-2", "13-3", "13-4", "13-5","13-6"]:
                    lun += item["checkin_info"][i]
                if i in ["14-0","14-1","14-2", "14-3", "14-4", "14-5","14-6"]:
                    lun += item["checkin_info"][i]
                if i in ["15-0","15-1","15-2", "15-3", "15-4", "15-5","15-6"]:
                    lun += item["checkin_info"][i]
                if i in ["16-0","16-1","16-2", "16-3", "16-4", "16-5","16-6"]:
                    din += item["checkin_info"][i]
                if i in ["17-0","17-1","17-2", "17-3", "17-4", "17-5","17-6"]:
                    din += item["checkin_info"][i]
                if i in ["18-0","18-1","18-2", "18-3", "18-4", "18-5","18-6"]:
                    din += item["checkin_info"][i]
                if i in ["19-0","19-1","19-2", "19-3", "19-4", "19-5","19-6"]:
                    din += item["checkin_info"][i]
                if i in ["20-0","20-1","20-2", "20-3", "20-4", "20-5","20-6"]:
                    din += item["checkin_info"][i]
                if i in ["21-0","21-1","21-2", "21-3", "21-4", "21-5","21-6"]:
                    din += item["checkin_info"][i]
                if i in ["22-0","22-1","22-2", "22-3", "22-4", "22-5","22-6"]:
                    latenight += item["checkin_info"][i]
                if i in ["23-0","23-1","23-2", "23-3", "23-4", "23-5","23-6"]:
                    latenight += item["checkin_info"][i]
                if i in ["0-0","0-1","0-2", "0-3", "0-4", "0-5","0-6"]:
                    latenight += item["checkin_info"][i]
                if i in ["1-0","1-1","1-2", "1-3", "1-4", "1-5","1-6"]:
                    latenight += item["checkin_info"][i]
                if i in ["2-0","2-1","2-2", "2-3", "2-4", "2-5","2-6"]:
                    latenight += item["checkin_info"][i]
                if i in ["3-0","3-1","3-2", "3-3", "3-4", "3-5","3-6"]:
                    latenight += item["checkin_info"][i]

            checkin.insert({"business_id" : item["business_id"], "breakfast" : bf, "lunch": lun, "dinner": din, "latenight": latenight})
            bf = lun = din = latenight = 0


    print checkin.count()