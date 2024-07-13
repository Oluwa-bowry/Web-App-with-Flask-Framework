from flask import Flask, request, render_template
app = Flask(__name__, template_folder='templates', static_folder='static')
username = "o____a"
description = "I love developing web applications."
description += " And this text was created with Jinja"

projects = [
    {
        'id': 1,
        'title': 'E-commerce Website',
        'description': 'A website where you can buy and sell stuffs',
        'author': 'o____a',
        'category': 'Web Development'
    },
    {
        'id': 2,
        'title': 'Flask Website',
        'description': 'A website made with Flask framework',
        'author': 'o____a',
        'category': 'Web Development'
    },
    {
        'id': 3,
        'title': 'Cool Mobile App',
        'description': 'An app that does cool stuffs',
        'author': 'o____a',
        'category': 'Mobile Development'
    },
    {
        'id': 4,
        'title': 'My Portfolio App',
        'description': 'The app displays information about my self carrerwise.',
        'author': 'o____a',
        'category': 'Web Development'
    },
    {
        'id': 5,
        'title': 'Blog on Backend development framework',
        'description': 'The blog entails detail evaluation of different backend framework.',
        'author': 'o____a',
        'category': 'Web Development'
    },
    {
        'id': 6,
        'title': 'Model deployment',
        'description': 'Machine learning model deploy for,forecasting the volatility in India',
        'author': 'o____a',
        'category': 'Mobile Development'
    },
]

@app.route('/')
def hello_world():
    return render_template('index.html', username = username, description = description, projects = projects)

@app.route('/about')
def about():
    return 'About Page'

@app.route('/contact', methods = ['POST', 'GET'])
def contact():
    if request.method == 'POST':
        return 'You are using POST'
    elif request.method == 'GET':
        return 'You are using GET'

if __name__ == '__main__':
    app.run()