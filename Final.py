from flask import Flask,render_template, request, flash
from selection_validator import ContactForm
import pandas as pd



import numpy as np
import pandas as pd
from sklearn import cross_validation,datasets, linear_model, metrics
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression



app = Flask(__name__)

app.secret_key = 'development key'

@app.route('/')
def Index():
	return render_template("index.html")

@app.route('/index.html')
def Front():
	return render_template("index.html")

@app.route('/About.html')
def About():
	return render_template("About.html")

@app.route('/Services.html')
def Services():
	return render_template("Services.html")

@app.route('/Visualization.html')
def Visualization():
	return render_template('Visualization.html')

@app.route('/Statistics.html')
def Statistics():
	return render_template('Statistics.html')


@app.route('/Predict.html')
def Predicts():
	return render_template('Predict.html')

@app.route('/Graph.html',methods = ['POST'])
def Graph():

	Crime_type = request.form.get("type")
	year = request.form.get("Predict_Year")
	df = pd.read_csv("static/crime.csv")

	X = df[['Year']]
	y = df[[Crime_type]]
	X_train,X_test,y_train,y_test = cross_validation.train_test_split(X,y,test_size=0.2)
	regressor = LinearRegression()
	regressor.fit(X_train,y_train)
	accuracy = regressor.score(X_test,y_test)
	accuracy = accuracy * 100
	year = float(year)
	X_test1 = np.array([year])
	y_prediction1 = regressor.predict([X_test1])
	






	

	return render_template('Graph.html',data = [Crime_type,year,accuracy,X_test1,y_prediction1])
	
@app.route('/D3_bar.html')
def BarChart():
	return render_template("D3_bar.html")

if __name__=='__main__':
	app.run(debug=True)

