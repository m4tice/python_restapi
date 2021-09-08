from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)


@app.before_first_request
def create_tables():
    db.create_all()


class Drink(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(120))

    def __repr__(self):
        return f"{self.name} - {self.description}"


resource_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'description': fields.String
}

# @app.route('/drinks')
# def get_drinks():
#     return {"drinks": "drink data"}
#
#
# @app.route('/')
# def index():
#     return "Hello!"


api.add_resource(Drink, "/drink/<int:drink_id>")

if __name__ == "__main__":
    print("==" * 100)
    app.run(debug=True)
