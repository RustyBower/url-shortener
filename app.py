from flask import Flask, redirect
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///urls.db'
db = SQLAlchemy(app)

# MAKE SURE TO INITIALIZE
# from yourapplication import db
# db.create_all()
class url(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    shorturl = db.Column(db.String, unique=True)
    longurl = db.Column(db.String, unique=True)

    def __init__(self, shorturl, longurl):
        self.shorturl = shorturl
        self.longurl = longurl

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/<path>')
def shortener(path):
    shorturl = url.query.filter_by(shorturl=path).first()
    #shorturl = url.query.get(1)
    return redirect(shorturl.longurl)

if __name__ == '__main__':
    app.run(debug=True)