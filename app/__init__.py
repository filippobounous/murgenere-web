from flask import Flask, render_template, redirect, request, Response
from functools import wraps
from os import getenv


def create_app():
    app = Flask(__name__)

    def check_auth(username, password):
        user = getenv('MY_USERNAME')
        pw = getenv('MY_PASSWORD')
        if user and pw:
            return username == user and password == pw
        return True  # auth disabled if creds missing

    def authenticate():
        return Response('Authentication required', 401,
                        {'WWW-Authenticate': 'Basic realm="Login"'})

    def requires_auth(f):
        @wraps(f)
        def decorated(*args, **kwargs):
            auth = request.authorization
            if not check_auth(*(auth or (None, None))):
                return authenticate()
            return f(*args, **kwargs)
        return decorated

    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/my')
    @requires_auth
    def my():
        # Redirects to the local streamlit app
        streamlit_url = getenv('STREAMLIT_URL', 'http://localhost:8501')
        return redirect(streamlit_url)

    return app
