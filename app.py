from flask import Flask
from routes.bookroutes import book_bp
from db import db

app = Flask(__name__)
app.register_blueprint(book_bp)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///forum.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

from models.bookmodel import BookModel
from models.postmodel import PostModel

db.init_app(app)
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
