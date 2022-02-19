from flask import Flask
from flask import render_template
import random as rand
import datetime as dt
import requests as req

jinja_101_app = Flask(__name__)


@jinja_101_app.route("/")
def hello_world():

    random_number = rand.randint(0, 10)

    current_year = dt.datetime.now().year

    return render_template('index.html', rnd_nr=random_number, current_year=current_year)


@jinja_101_app.route("/guess/<in_name>")
def guess(in_name):

    a_response = req.get(f'https://api.agify.io?name={in_name}')
    a_age = a_response.json()['age']

    a_response = req.get(f'https://api.genderize.io?name={in_name}')
    a_gender = a_response.json()['gender']

    return render_template('guess.html', name=in_name, age=a_age, gender=a_gender)


@jinja_101_app.route('/blog/<num>')
def blog(num):

    print(num)
    a_response = req.get('https://api.npoint.io/c790b4d5cab58020d391')
    all_posts = a_response.json()

    return render_template('blog.html', posts=all_posts)


if __name__ == '__main__':
    jinja_101_app.run(debug=True)