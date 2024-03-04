#!/usr/bin/env python3
""" basic Flask app"""
from flask import Flask, render_template, request
from flask_babel import Babel
app = Flask(__name__)
babel = Babel(app)


class Config:
    """ bable configuration """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@babel.locale_selector
def get_locale():
    """ select best match """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def home_page():
    """ home page"""
    return render_template('1-index.html')


if __name__ == "__main__":
    app.run()
