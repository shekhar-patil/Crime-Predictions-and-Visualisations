from flask import Flask,render_template, request, flash
from selection_validator import ContactForm

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


@app.route('/Predict.html', methods=['GET', 'POST'])
def Predicts():
	form = ContactForm()
	if request.method == 'POST':
		if form.validate() == False:
			flash('All fields are required.')
			return render_template('Predict.html', form=form)
		else:
			return render_template('D3_bar.html')
	elif request.method == 'GET':
		return render_template('Predict.html', form=form)

@app.route('/D3_bar.html')
def BarChart():
	return render_template("D3_bar.html")

if __name__=='__main__':
	app.run(debug=True)
