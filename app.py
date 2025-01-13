from flask import Flask
from flask_wtf.csrf import CSRFProtect
from blueprints.general import app as general
from blueprints.admin import app as admin
from blueprints.user import app as user
import confing
import extentions
from flask_login import LoginManager
from models.user import User

app = Flask(__name__)
app.register_blueprint(general)
app.register_blueprint(user)
app.register_blueprint(admin)

app.config["SQLALCHEMY_DATABASE_URI"] = confing.SQLALCHEMY_DATABASE_URI
app.config['SECRET_KEY'] = confing.SECRET_KEY
extentions.db.init_app(app)


with app.app_context():
    extentions.db.create_all()
csrf = CSRFProtect(app)
login_manager = LoginManager()
login_manager.init_app(app)
@login_manager.user_loader
def load_user(user_id):
    return User.query.filter(User.id == user_id).first()



if __name__ == '__main__':
    app.run(debug=True)
