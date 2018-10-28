from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World from HIDE's new solution"


@app.errorhandler(500)
@app.errorhandler(404)
def errorPage(error):
    return render_template('error.html', error=error)


@app.route("/menu/")
def menu():
    return render_template('menu.html')


@app.route("/ResultsPage/")
def resultsPage():
    return render_template('ResultsPage.html')


@app.route("/SurveyLandingPage/")
def surveyLandingPage():
    return render_template('SurveyLandingPage.html')


@app.route("/ThankYouPage/")
def thankYouPage():
    return render_template('ThankYouPage.html')


if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host='127.0.0.1', debug=True, port=80)
