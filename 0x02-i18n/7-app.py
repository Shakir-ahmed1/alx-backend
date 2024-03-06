#!/usr/bin/env python3
""" basic Flask app"""
from flask import Flask, render_template, request, g
from flask_babel import Babel
import pytz
app = Flask(__name__)
babel = Babel(app)


class Config:
    """ bable configuration """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user(user_id):
    """ get user by id """
    try:
        return users.get(user_id)
    except Exception:
        return


@app.before_request
def before_request():
    """ excute before every request"""
    user_id = request.args.get('login_as')
    g.user = get_user(int(user_id)) if user_id else None


@babel.localeselector
def get_locale():
    """ select best match for locale """
    locale_param = request.args.get('locale')
    if locale_param and locale_param in Config.LANGUAGES:
        return locale_param

    if hasattr(g, 'user') and g.user:
        user_locale = g.user.get('locale')
        if user_locale in Config.LANGUAGES:
            return user_locale

    request_locale = request.accept_languages.best_match(Config.LANGUAGES)
    if request_locale:
        return request_locale

    return Config.BABEL_DEFAULT_LOCALE

@babel.timezoneselector
def get_timezone():
    """ select best match for timezone """
    timezone_param = request.args.get('timezone')
    if timezone_param:
        try:
            pytz.timezone(timezone_param)
            return timezone_param
        except pytz.exceptions.UnknownTimeZoneError:
            pass

    if g.user and g.user.get('timezone'):
        try:
            pytz.timezone(g.user['timezone'])
            return g.user['timezone']
        except pytz.exceptions.UnknownTimeZoneError:
            pass

    return Config.BABEL_DEFAULT_TIMEZONE

@app.route('/')
def home_page():
    """ home page"""
    return render_template('6-index.html')


if __name__ == "__main__":
    app.run()
