'''

This file builds a collection that stores a list of categories(possibily having some redundancy) against each user_id in the yelp_test_reduced_user collection. This list corresponds to all the various categories the user has reviewed. 

'''


from pymongo import MongoClient

if __name__ == '__main__':

    client = MongoClient()
    dBase = client.yelp_test_recommend
    business = dBase.yelp_test_business
    restaurants = dBase.yelp_test_restaurant
    checkin = dBase.yelp_test_checkin
    reviews = dBase.yelp_test_review
    restaurantReviews = dBase.yelp_test_res_review
    users = dBase.yelp_test_user
    reducedUser = dBase.yelp_test_reduced_user

    print "Business count: " + str(business.count())
    print "Restaurant count: " + str(restaurants.count())
    print "Check in count: " + str(checkin.count())
    print "Restaurant Review count: " + str(restaurantReviews.count())
    print "Review count: " + str(reviews.count())
    userCat = dBase.yelp_test_user_cat

    userCat.remove({})

    user_list = []
    for item in reducedUser.find():
        userCat.insert({"user_id" : item["user_id"], "categories" : []})
        user_list.append(item['user_id'])

    print "User category collection initialization done!!"
    

    res_dict = {}

    for item in restaurants.find():
        res_dict[item["business_id"]] = item["categories"]

    print "Restaurant Dictionary creation done!!"
    
    
    for user in user_list:
        for review in restaurantReviews.find({"user_id" : user}):
                for i in userCat.find({"user_id": user}):
                    tempL = i['categories'][:]
                    tempL = tempL + res_dict[review["business_id"]]
                    userCat.remove({"user_id" : user})
                    userCat.insert({"user_id": user, "categories" : tempL})


