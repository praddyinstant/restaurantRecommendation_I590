from pymongo import MongoClient
from Tkinter import *
import sys
import tkMessageBox
import tkFont

def quit():
    top.destroy()

def recommendCallBack():
	city_selection = cities.curselection()

	city_value = cities.get(city_selection[0])

	if var1.get() == 0:
		tim_value = "breakfast"
	elif var1.get() == 1:
		tim_value = "lunch"
	elif var1.get() == 2:
		tim_value = "dinner"
	elif var1.get() == 3:
		tim_value = "latenight"
	print city_value
	print tim_value
	str1 = usr.get() + " Needs Recommendations for " + str(tim_value) + " in " + str(city_value)


	#user_id = raw_input("Please enter your Yelp user id: ")
	#city = raw_input("Please enter your city preference: ")
	#time = raw_input("Please enter your preference for time: ").lower()
	user_id = usr.get()
	city = str(city_value)
	time = str(tim_value)
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
	elif city == "Karlsruhe":
		cityCol = dBase.yelp_test_Karlsruhe
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
	recommendList = []
	maximum = 1

	print "We recommend these restaurants based on your city, time and previous food preferences: "
	for i in finalList:
		if maximum <= 8:
			for r in res:
				if i == r["business_id"]:
					print "Restaurant name: ",r['name']," Value: ",finalDict[r['business_id']]
					recommendList.append(str(maximum) + ". Name: "+ r['name'] + " \n" + " " + "Address: " + r['full_address']+ "\n \n")
		maximum += 1
	tkMessageBox.showinfo( "Recommendation System", ' '.join(recommendList))
	#print cityCol.count()

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

	top = Tk()
	# Code to add widgets will go here...
	var_text = StringVar()
	simpleLabel = Label(top, textvariable=var_text, relief=RAISED)
	arial36 = tkFont.Font(family='Arial',size=34, weight='bold')
	simpleLabel['font'] = arial36
	var_text.set("Restaurant Recommender System")
	simpleLabel.place(x = 90, y = 10)
	var_user = StringVar()
	usr_label = Label(top, textvariable=var_user, relief=RAISED)
	var_user.set("User ID")
	usr_label.place(x = 40, y = 90)
	usr = StringVar()
	usr_txt = Entry(top,textvariable=usr, bd =5)
	usr_txt.place(x = 150, y= 90)
	var = StringVar()
	label = Label( top, textvariable=var, relief=RAISED )
	var.set("Cities")
	label.place(x = 40, y = 170)
	tim = StringVar()
	label_tim = Label( top, textvariable=tim, relief=RAISED )
	tim.set("Time Preference")
	label_tim.place(x = 40, y = 350)

	frame = Frame(top)
	scrollbar = Scrollbar(frame, orient=VERTICAL)
	cities = Listbox(frame, yscrollcommand=scrollbar.set)

	scrollbar.pack(side=RIGHT, fill=Y)
	cities.pack(side=LEFT, fill=BOTH, expand=1)
	cities.insert(0,"Edinburgh","Karlsruhe","Montreal","Waterloo","Pittsburgh","Charlotte","Urbana-Champaign", "Phoenix","Las Vegas","Madison")
	frame.place(x = 150, y = 130)

	var1 = IntVar()
	R1 = Radiobutton(top, text="Breakfast", variable=var1, value=0)
	R2 = Radiobutton(top, text="Lunch", variable=var1, value=1)
	R3 = Radiobutton(top, text="Dinner", variable=var1, value=2)
	R4 = Radiobutton(top, text="Latenight Spots", variable=var1, value=3)

	R1.place(x=150, y = 300)
	R2.place(x=150, y = 325)
	R3.place(x=150, y = 350)
	R4.place(x=150, y = 375)


	B = Button(top, text ="Submit", command = recommendCallBack)
	B.place(x = 90, y = 440)
	close = Button(top, text = 'Close', command = quit)
	close.place(x = 150 , y = 440)
	top.overrideredirect(True)
	top.geometry("{0}x{1}+0+0".format(top.winfo_screenwidth(), top.winfo_screenheight()))
	top.mainloop()
