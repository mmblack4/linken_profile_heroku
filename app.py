import os
from models.schema import *
from flask import Flask, render_template


app = Flask(__name__)
app.secret_key = 'my-secret-key'
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False



@app.route('/')
def home():
    profiles = Link.query.all()
    return render_template("link_table.html",profiles = profiles)


if __name__ == "__main__":
    from db import db
    db.init_app(app)
    app.run(debug=True)