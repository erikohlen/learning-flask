from flask import Flask, render_template, request
from forms import SignupForm
import numpy as np
import scipy
from scipy import stats

app = Flask(__name__)


app.secret_key = "development-key"

@app.route("/")
def index():
	return render_template("index.html")


@app.route("/about")
def about():
	return render_template("about.html")





@app.route("/calc", methods=['GET', 'POST'])
def signup():
	form = SignupForm()
	
	if request.method == 'POST':
		org = form.first_name.data
		var1 = form.last_name.data
		orga = np.fromstring(org, dtype=int, sep=' ')
		var1a = np.fromstring(var1, dtype=int, sep=' ')
		if form.twosided.data == "yes":
			alternative = "two-sided"
		else:
			alternative = "None"
		results = str(scipy.stats.mannwhitneyu(orga, var1a, use_continuity=True, alternative=alternative))
		return str(results)
		

	elif request.method == "GET":
		return render_template('calc.html', form=form)

	return render_template('calc.html', form=form)

if __name__ == "__main__":
	app.run(debug=True)