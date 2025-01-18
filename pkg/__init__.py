from flask import Flask
from flask_wtf.csrf import CSRFProtect
from flask_migrate import Migrate

from flask_mail import Mail,Message


csrf= CSRFProtect()
mail = Mail()
def create_app():
    """keep all imports that may cause conflicts within this function so that anytime we write "from debapp... import... none of these statements will be executed" """
    from pkg.models import db
    from pkg import config
    app=Flask(__name__,instance_relative_config=True)
    app.config.from_pyfile("config.py", silent=True)
    app.config.from_object(config.TestConfig)
    db.init_app(app)
    csrf.init_app(app)
    mail.init_app(app)
    migrate = Migrate(app,db)
    return app

app = create_app()
from pkg import routes,admin_routes