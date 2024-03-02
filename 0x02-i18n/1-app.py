#!/usr/bin/env python3
""" basic Flask app"""
from flask import Flask, render_template
app = Flask(__name__)


class Config:
    LANGUAGES = ["en", "fr"]
    DEFAULT_LANGUAGE = 'en'
    TIMEZONE = 'UTC'


app.config.from_object(Config)


@app.route('/')
def home_page():
    """ home page"""
    return render_template('1-index.html')


if __name__ == "__main__":
    app.run()
