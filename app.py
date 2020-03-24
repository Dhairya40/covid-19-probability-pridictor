from flask import Flask, render_template, request
import datetime
import random
app = Flask(__name__)
import pickle

file = open('model.pkl', 'rb')
clf = pickle.load(file)
file.close()

@app.route('/', methods = ['GET', 'POST'])
def hello_world():
	infProb = 0
	if request.method == 'POST': 
		myDict = request.form
		# test input Values
		# print(request.form)

		fever        = int(myDict['fever'])
		bodyPain     = int(myDict['bodyPain'])
		age          = int(myDict['age'])
		runnyNose    = int(myDict['runnyNose'])
		diffBreath   = int(myDict['diffBreath'])
		if 98 <= fever <= 104:
			pass
		else:
			message = "OPPS!! Don't cheat me! Enter valid fever value!"
			return render_template('index.html', message = message)

		if 1 <= age <= 100:
			pass
		else:
			messageAge = "OPPS!! Don't cheat me! Enter valid age!"
			return render_template('index.html', message = messageAge)

		inputFeature = [fever, bodyPain, age, runnyNose, diffBreath]
		infProb = clf.predict_proba([inputFeature])[0][1]
		# print(infProb)
		# return render_template('result.html', infProb = round(infProb) * 100)

	# return 'Hello, World!' + str(infProb)
	return render_template('index.html', Prob = round(infProb * 100), today_date = datetime.date.today()) 

@app.route('/corona', methods = ['GET'])
def about_corona():
	lst = ['2.jpg', '3.jpeg', 'c1.jpg', 'c2.jpg', 'c3.jpg', 'c4.png', 'c5.jpg', 'c6.jpg', 'c7.jpg', 'c8.jpg','1800x1200_coronavirus_1.jpg','9.png','7.jpg','6.jpg','5.jpg','4.png']
	randImg = random.sample(lst, 6)
	return render_template('result.html', randImg = randImg)

if __name__ == "__main__":
	app.run(debug= True)

