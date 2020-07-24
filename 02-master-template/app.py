from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.template.html')


@app.route('/about')
def about():
    return render_template('about.template.html')


@app.route('/faq')
def show_faq():
    return render_template('faq.template.html')


# "magic code" -- boilerplate
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)