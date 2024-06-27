from flask import redirect, url_for
from flskr.create_app import create_app

app = create_app()

@app.route('/')
def index():
    return redirect(url_for('colabs.gerir.login_colab'))