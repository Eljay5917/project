from flask import Flask, render_template
import requests 


app = Flask(__name__)



import requests
api_key="ee2798328aa7160fd1a37d3ad3a29b1a"
url =f'http://api.openweathermap.org/data/2.5/weather?q=Koforidua&appid={api_key}'

get_requests=requests.get(url)




@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        country = request.form['country']
        weather = request.form['weather']
        return render_template('results.html', country=country, weather=weather)
    return render_template("index.html")

@app.route('/results', methods=['GET', 'POST'])
def results():
    if request.method == 'POST':
        country = request.form['country']
        weather = request.form['weather']
        return render_template("results.html", country=country, weather=weather)
    return "Invalid request"

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
