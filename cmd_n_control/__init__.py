from flask import Flask

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/data.db'
from cmd_n_control.models import db
import cmd_n_control.models
db.init_app(app)
import cmd_n_control.views
with app.app_context():
    db.create_all()
    house = cmd_n_control.models.Location()
    house.name = "The Big Blue House"
    db.session.add(house)
    db.session.commit()
    locations = models.Location.query.all()
    print(locations)
