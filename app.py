from flask import Flask, render_template

app = Flask(__name__)

# Sample blog posts (later we can store them in a database)
posts = [
    {
        'title': 'My First Blog Post',
        'content': 'This is my first post on Flask!',
        'author': 'Vinny'
    },
    {
        'title': 'Learning Flask',
        'content': 'Today I learned how to use templates in Flask.',
        'author': 'Vinny'
    }
]

@app.route('/')
def home():
    return render_template('home.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html')
