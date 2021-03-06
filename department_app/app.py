from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://app:app@localhost/app'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'any secret string'
db = SQLAlchemy(app)
migrate = Migrate(app, db)


import department_app.views
import department_app.rest.api_views

if __name__ == '__main__':
    app.run(debug=True)



